from sqlalchemy.orm import Session

from florestsdk.models.company_model import CompanyModel
from florestsdk.models.person_model import PersonModel


class CompanyRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_company(self, company_data: dict) -> CompanyModel:
        company = CompanyModel(**company_data)
        self.session.add(company)
        self.session.commit()
        return company

    def get_company_by_id(self, company_id: int) -> CompanyModel | None:
        return self.session.query(CompanyModel).filter(CompanyModel.id == company_id).first()

    def update_company(self, company_id: int, update_data: dict) -> CompanyModel | None:
        company = self.session.query(CompanyModel).filter(CompanyModel.id == company_id).first()
        if company:
            for key, value in update_data.items():
                setattr(company, key, value)
            self.session.commit()
        return company

    def delete_company(self, company_id: int) -> bool:
        company = self.session.query(CompanyModel).filter(CompanyModel.id == company_id).first()
        if company:
            self.session.delete(company)
            self.session.commit()
            return True
        return False

    def add_person_to_company(self, company_id: int, person_data: dict) -> PersonModel | None:
        company = self.session.query(CompanyModel).filter(CompanyModel.id == company_id).first()
        if company:
            person = PersonModel(**person_data, company=company)
            self.session.add(person)
            self.session.commit()
            return person
        return None

    def list_companies(self):
        return self.session.query(CompanyModel).all()
