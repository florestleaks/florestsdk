from florestsdk.models import CompanyModel
from florestsdk.models.yara_model import YaraRuleModel
from florestsdk.repositories.yara_manager.yara_manager_repository import YaraRuleRepository


class YaraRulesService:
    """
    Provides services for managing YARA rules including creating, updating,
    fetching, listing, and deleting YARA rules, importing rules from a directory,
    and compiling and matching YARA rules against texts.
    """

    def __init__(self, yara_rule_repository: YaraRuleRepository):
        """
        Initializes the YaraRulesService with a YaraRuleRepository.

        Parameters
        ----------
        yara_rule_repository : YaraRuleRepository
            The repository responsible for managing YARA rule data.
        """
        self.yara_rule_repository: YaraRuleRepository = yara_rule_repository

    def create_or_update_yara_rule(
        self, rule_name: str, rule_content: str, client_id: int, category: str
    ) -> YaraRuleModel:
        """
        Creates or updates a YARA rule with the given details.

        Parameters
        ----------
        rule_name : str
            The name of the YARA rule.
        rule_content : str
            The content of the YARA rule.
        client_id : int
            The ID of the client for whom the rule is being created or updated.
        category : str
            The category of the YARA rule.

        Returns
        -------
        YaraRuleModel
            The created or updated YARA rule model.
        """
        return self.yara_rule_repository.create_or_update_yara_rule(
            rule_name, rule_content, client_id, category
        )

    def get_yara_rule(self, rule_id: int) -> YaraRuleModel | None:
        """
        Fetches a YARA rule by its ID.

        Parameters
        ----------
        rule_id : int
            The ID of the YARA rule to fetch.

        Returns
        -------
        YaraRuleModel or None
            The fetched YARA rule model, or None if not found.
        """
        return self.yara_rule_repository.get_yara_rule_by_id(rule_id)

    def list_yara_rules(self) -> list[YaraRuleModel]:
        """
        Lists all YARA rules.

        Returns
        -------
        list of YaraRuleModel
            A list of all YARA rule models.
        """
        return self.yara_rule_repository.get_all_yara_rules()

    def update_yara_rule(self, rule_id: int, **kwargs) -> YaraRuleModel | None:
        """
        Updates a YARA rule with given keyword arguments.

        Parameters
        ----------
        rule_id : int
            The ID of the YARA rule to update.
        **kwargs : dict
            The fields to update in the YARA rule.

        Returns
        -------
        YaraRuleModel or None
            The updated YARA rule model, or None if the update fails.
        """
        return self.yara_rule_repository.update_yara_rule(rule_id, **kwargs)

    def remove_yara_rule(self, rule_id: int) -> bool:
        """
        Removes a YARA rule by its ID.

        Parameters
        ----------
        rule_id : int
            The ID of the YARA rule to remove.

        Returns
        -------
        bool
            True if the rule was successfully removed, False otherwise.
        """
        return self.yara_rule_repository.delete_yara_rule(rule_id)

    def import_yara_rules_from_directory(
        self, directory_path: str, all_companies: list[CompanyModel]
    ):
        """
        Imports YARA rules from a directory for all specified companies.

        Parameters
        ----------
        directory_path : str
            The path to the directory from which to import YARA rules.
        all_companies : list of CompanyModel
            A list of company models for which the YARA rules are to be imported.

        Returns
        -------
        None
        """
        return self.yara_rule_repository.import_yara_rules_from_directory(
            directory_path, all_companies
        )

    def compile_and_match_yara_rules(self, text: str):
        """
        Compiles and matches YARA rules against the provided text.

        Parameters
        ----------
        text : str
            The text to match against the YARA rules.

        Returns
        -------
        list : dict
        """
        return self.yara_rule_repository.compile_and_match_yara_rules(text)
