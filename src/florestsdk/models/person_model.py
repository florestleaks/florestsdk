from typing import ClassVar

from sqlalchemy import Column, ForeignKey, Integer, String

from florestsdk.database import Base


class PersonModel(Base):
    __tablename__ = "people"
    __table_args__: ClassVar = {"schema": "florest"}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    company_id = Column(Integer, ForeignKey("florest.companies.id"))

    def __repr__(self):
        return f"<Person(id={self.id}, name='{self.name}', email='{self.email}', company_id={self.company_id})>"
