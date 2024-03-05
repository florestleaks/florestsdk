from florestsdk.database import FlorestDatabase
from florestsdk.repositories.yara_manager.yara_manager_repository import YaraRuleRepository
from florestsdk.services.yara_manager.yara_manager_services import YaraRulesService

if __name__ == "__main__":
    # Initialize database and session
    db = FlorestDatabase("postgresql+psycopg2://me:mypassword@127.0.0.1/mydb", echo=False)
    db.create_tables()  # Ensure all tables are created
    session = db.Session()  # Create a new session

    # Initialize repository and service
    yara_rule_repository = YaraRuleRepository(session)
    yara_rules_service = YaraRulesService(yara_rule_repository)

    # Example data for a new YARA rule
    rule_name = "ExampleRule"
    rule_content = "rule ExampleRule { condition: true }"
    client_id = 1  # Assuming a client with ID 1 exists in the database
    category = "Malware"  # Example category for the new YARA rule
    # Adding the YARA rule
    new_rule = yara_rules_service.create_or_update_yara_rule(
        rule_name=rule_name, rule_content=rule_content, client_id=client_id, category=category
    )
    print(f"New YARA rule added: {new_rule.id}")
