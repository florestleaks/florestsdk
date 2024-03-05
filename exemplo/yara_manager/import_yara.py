from florestsdk.database import FlorestDatabase
from florestsdk.repositories.company.company_repository import CompanyRepository
from florestsdk.repositories.yara_manager.yara_manager_repository import YaraRuleRepository
from florestsdk.services.yara_manager.yara_manager_services import YaraRulesService

if __name__ == "__main__":
    # Initialize database and session
    db = FlorestDatabase("postgresql+psycopg2://me:mypassword@127.0.0.1/mydb", echo=False)
    db.create_tables()  # Ensure all tables are created
    db.create_schema()
    session = db.Session()  # Create a new session

    # Initialize repository and service
    yara_rule_repository = YaraRuleRepository(session)
    yara_rules_service = YaraRulesService(yara_rule_repository)
    company_repo = CompanyRepository(session)
    all_company = company_repo.list_companies()
    yara_rules = yara_rules_service.import_yara_rules_from_directory(
        all_companies=all_company, directory_path="."
    )
