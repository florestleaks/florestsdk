from sqlalchemy.orm import relationship

from florestsdk.models.company_model import CompanyModel
from florestsdk.models.person_model import PersonModel
from florestsdk.models.yara_model import YaraRuleModel

# Configurando as relações
CompanyModel.people = relationship("PersonModel", back_populates="company")
PersonModel.company = relationship("CompanyModel", back_populates="people")
CompanyModel.yara_rules = relationship(
    "YaraRuleModel", back_populates="company", cascade="all, delete-orphan"
)
YaraRuleModel.company = relationship("CompanyModel", back_populates="yara_rules")
