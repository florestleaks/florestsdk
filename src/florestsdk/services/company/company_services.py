from florestsdk.interfaces.company.services.company_services import (
    ICompanyServices,  # Assuming ICompanyServices exists and is the correct interface
)
from florestsdk.repositories.company.company_repository import CompanyRepository


class CompanyServices(ICompanyServices):
    def __init__(self, repository: CompanyRepository):
        self.repository = repository

    def create_company(self, company_data: dict):
        return self.repository.create_company(company_data)

    def get_company_by_id(self, company_id: int):
        return self.repository.get_company_by_id(company_id)

    def update_company(self, company_id: int, update_data: dict):
        return self.repository.update_company(company_id, update_data)

    def delete_company(self, company_id: int):
        return self.repository.delete_company(company_id)

    def add_person_to_company(self, company_id: int, person_data: dict):
        return self.repository.add_person_to_company(company_id, person_data)

    def list_companies(self):
        return self.repository.list_companies()
