import os
from pathlib import Path

import yara
from sqlalchemy.orm import Session

from florestsdk.models.company_model import CompanyModel
from florestsdk.models.yara_model import YaraRuleModel


class YaraRuleRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_or_update_yara_rule(
        self, rule_name: str, rule_content: str, client_id: int, category: str
    ) -> YaraRuleModel:
        yara_rule = (
            self.session.query(YaraRuleModel)
            .filter_by(rule_name=rule_name, company_id=client_id)
            .first()
        )

        if yara_rule:
            yara_rule.rule_content = rule_content
            yara_rule.category = category
        else:
            # Cria uma nova regra se não existir
            yara_rule = YaraRuleModel(
                rule_name=rule_name,
                rule_content=rule_content,
                company_id=client_id,
                category=category,
            )
            self.session.add(yara_rule)

        self.session.commit()
        return yara_rule

    def get_yara_rule_by_id(self, yara_rule_id: int) -> YaraRuleModel | None:
        return self.session.query(YaraRuleModel).filter(YaraRuleModel.id == yara_rule_id).first()

    def update_yara_rule(self, yara_rule_id: int, update_data: dict) -> YaraRuleModel | None:
        yara_rule = self.get_yara_rule_by_id(yara_rule_id)
        if yara_rule:
            for key, value in update_data.items():
                setattr(yara_rule, key, value)
            self.session.commit()
            return yara_rule
        return None

    def delete_yara_rule(self, yara_rule_id: int) -> bool:
        yara_rule = self.get_yara_rule_by_id(yara_rule_id)
        if yara_rule:
            self.session.delete(yara_rule)
            self.session.commit()
            return True
        return False

    def associate_yara_rule_with_company(
        self, yara_rule_id: int, company_id: int
    ) -> YaraRuleModel | None:
        yara_rule = self.get_yara_rule_by_id(yara_rule_id)
        if yara_rule and yara_rule.company_id != company_id:
            company = self.session.query(CompanyModel).filter(CompanyModel.id == company_id).first()
            if company:
                yara_rule.company_id = company_id
                self.session.commit()
                return yara_rule
        return None

    def import_yara_rules_from_directory(
        self, directory_path: str, all_companies: list[CompanyModel]
    ):
        for filename in os.listdir(directory_path):
            if filename.endswith(".yar"):
                # Extrair componentes do nome do arquivo
                parts = filename[:-4].split("_")
                if len(parts) >= 3:
                    category = parts[0]
                    company_name = parts[1]
                    unique_identifier = "_".join(
                        parts[2:]
                    )  # Considerando que o identificador único pode conter sublinhados

                    # Encontrar o ID da empresa correspondente ao nome da empresa no nome do arquivo
                    company_id = None
                    for company in all_companies:
                        if company.name == company_name:
                            company_id = company.id
                            break

                    if company_id is None:
                        print(f"Empresa não encontrada para o nome: {company_name}")
                        continue  # Pula este arquivo se a empresa não for encontrada

                    # Construir o nome da regra a partir dos componentes extraídos
                    rule_name = f"{category}_{company_name}_{unique_identifier}"

                    directory_path = Path(directory_path)

                    # Usando o operador `/` para juntar caminhos de forma mais limpa
                    file_path = directory_path / filename

                    # Usando `Path.open()` para abrir o arquivo
                    with file_path.open() as file:
                        rule_content = file.read()

                    # Verificar se a regra já existe
                    existing_rule = (
                        self.session.query(YaraRuleModel)
                        .filter(
                            YaraRuleModel.rule_name == rule_name,
                            YaraRuleModel.company_id == company_id,
                        )
                        .first()
                    )

                    if existing_rule:
                        # Atualizar regra existente
                        self.create_or_update_yara_rule(
                            rule_name, rule_content, company_id, category
                        )
                    else:
                        # Criar nova regra
                        self.create_or_update_yara_rule(
                            rule_name, rule_content, company_id, category
                        )
                else:
                    print(f"Formato de nome de arquivo inválido: {filename}")

    def compile_and_match_yara_rules(self, text: str):
        # Buscar todas as regras YARA do banco de dados
        rules = self.session.query(YaraRuleModel).all()
        sources = {}
        for rule in rules:
            sources[rule.rule_name] = rule.rule_content

        # Compilar todas as regras de uma vez usando o dicionário de fontes
        try:
            rules_namespace = yara.compile(sources=sources)
        except yara.SyntaxError as e:
            print(f"Erro de sintaxe ao compilar regras: {e}")
            return None

        # Testar o texto fornecido contra as regras compiladas
        matches = rules_namespace.match(data=text)

        # Processar e gerar os resultados das correspondências
        results = []
        for match in matches:
            rule = self.session.query(YaraRuleModel).filter_by(rule_name=match.rule).first()
            if rule:
                company = self.session.query(CompanyModel).filter_by(id=rule.company_id).first()
                results.append(
                    {
                        "rule_name": match.rule,
                        "category": rule.category,  # Usar a categoria da regra
                        "company_name": company.name if company else "Desconhecida",
                    }
                )

        # Retorna os resultados em vez de imprimir, para melhor integração
        return results
