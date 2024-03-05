from abc import ABC, abstractmethod

from florestsdk.models.company_model import CompanyModel
from florestsdk.models.person_model import PersonModel


class ICompanyServices(ABC):
    @abstractmethod
    def create_company(self, company_data: dict) -> CompanyModel:
        pass

    @abstractmethod
    def get_company_by_id(self, company_id: int) -> CompanyModel | None:
        pass

    @abstractmethod
    def update_company(self, company_id: int, update_data: dict) -> CompanyModel | None:
        pass

    @abstractmethod
    def delete_company(self, company_id: int) -> bool:
        pass

    @abstractmethod
    def add_person_to_company(self, company_id: int, person_data: dict) -> PersonModel | None:
        pass

    @abstractmethod
    def list_companies(self) -> list[CompanyModel]:
        pass
