from florestsdk.database import FlorestDatabase
from florestsdk.repositories.company.company_repository import CompanyRepository

if __name__ == "__main__":
    # Inicializando o banco de dados
    db = FlorestDatabase("postgresql+psycopg2://me:mypassword@127.0.0.1/mydb", echo=False)

    # Cria a schema antes de tentar criar tabelas
    db.create_schema()  # Cria a schema 'florest' se ela não existir
    db.create_tables()  # Agora cria as tabelas dentro da schema 'florest'

    session = db.get_session()  # Create a new session usando o método correto

    # Inicializando o repositório da empresa
    company_repo = CompanyRepository(session)

    # Criando uma nova empresa
    company_data = {"name": "AcmeCorp", "email": "AcmeCorp@example.com"}
    new_company = company_repo.create_company(company_data)
    print(new_company)
    # Adicionando uma pessoa à empresa
    person_data = {"name": "dsa", "email": "dsa@example.com"}
    added_person = company_repo.add_person_to_company(new_company.id, person_data)

    # Listando todas as empresas
    companies = company_repo.list_companies()
    for company in companies:
        print(f"Empresa: {company.name}, E-mail: {company.email}")

    # Fechando a sessão
    session.close()
