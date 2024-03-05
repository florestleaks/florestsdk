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

    all_company = company_repo.list_companies()

    print(all_company)
