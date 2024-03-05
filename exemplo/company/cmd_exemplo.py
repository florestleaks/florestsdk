# Continuação do exemplo anterior...
from florestsdk.database import FlorestDatabase
from florestsdk.repositories.company.company_repository import CompanyRepository
from florestsdk.repositories.person.person_repository import PersonRepository
from florestsdk.repositories.yara_manager.yara_manager_repository import YaraRuleRepository

if __name__ == "__main__":
    # Inicializando o banco de dados
    db = FlorestDatabase("postgresql+psycopg2://me:mypassword@127.0.0.1/mydb", echo=False)
    db.create_tables()

    # Criando uma sessão
    session = db.Session()
    company_repo = CompanyRepository(session)
    person_repo = PersonRepository(session)
    yara_rule_repo = YaraRuleRepository(session)
    # Inicializando o repositório da empresa

    # Listando todas as empresas
    companies = company_repo.list_companies()
    while True:
        companies = company_repo.list_companies()

        if not companies:
            print("Não há companhias cadastradas.")
            break

        for index, company in enumerate(companies, start=1):
            print(f"{index} - {company.name}")

        choice = input("\nSelecione o número da companhia (ou 'quit' para sair): ")

        if choice.lower() == "quit":
            break
        else:
            try:
                selected_index = int(choice) - 1
                selected_company = companies[selected_index]
                selected_company_id = selected_company.id
                print(
                    f"Você selecionou a companhia: {selected_company.name} com ID: {selected_company_id}"
                )

                # Adicionando uma nova pessoa à companhia escolhida
                new_person_data = {
                    "name": "Charlie",
                    "email": "charlie@datasecurity.com",
                    "company_id": selected_company_id,
                }
                person_repo.create_person(new_person_data)
                print(f"Pessoa adicionada à companhia: {selected_company.name}")

                # Adicionando uma nova regra YARA à companhia escolhida
                new_yara_rule_data = {
                    "rule_name": "Suspicious Activity",
                    "rule_content": "rule SuspiciousActivity { ... }",
                    "company_id": selected_company_id,
                }
                yara_rule_repo.create_or_update_yara_rule(new_yara_rule_data, selected_company_id)
                print("Regra YARA adicionada à companhia.")

                # Se desejar parar o loop após adicionar a pessoa e a regra, descomente a linha abaixo
                # break

            except (ValueError, IndexError):
                print("Seleção inválida. Por favor, insira um número válido da lista.")

    # Fechando a sessão
    session.close()
