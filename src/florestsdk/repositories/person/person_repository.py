from sqlalchemy.orm import Session

from florestsdk.models.company_model import CompanyModel
from florestsdk.models.person_model import PersonModel


class PersonRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_person(self, person_data: dict) -> PersonModel:
        person = PersonModel(**person_data)
        self.session.add(person)
        self.session.commit()
        return person

    def get_person_by_id(self, person_id: int) -> PersonModel | None:
        return self.session.query(PersonModel).filter(PersonModel.id == person_id).first()

    def update_person(self, person_id: int, update_data: dict) -> type[PersonModel] | None:
        person = self.session.query(PersonModel).filter(PersonModel.id == person_id).first()
        if person:
            for key, value in update_data.items():
                setattr(person, key, value)
            self.session.commit()
            return person
        return None

    def delete_person(self, person_id: int) -> bool:
        person = self.session.query(PersonModel).filter(PersonModel.id == person_id).first()
        if person:
            self.session.delete(person)
            self.session.commit()
            return True
        return False

    def associate_person_with_company(self, person_id: int, company_id: int) -> PersonModel | None:
        person = self.get_person_by_id(person_id)
        company = self.session.query(CompanyModel).filter(CompanyModel.id == company_id).first()
        if person and company:
            person.company = company
            self.session.commit()
            return person
        return None
