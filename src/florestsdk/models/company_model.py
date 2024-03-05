from typing import ClassVar

from sqlalchemy import Column, Integer, String

from florestsdk.database import Base


class CompanyModel(Base):
    __tablename__ = "companies"
    __table_args__: ClassVar = {"schema": "florest"}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f"<Company(id={self.id}, name='{self.name}', email='{self.email}')>"
