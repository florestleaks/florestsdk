from typing import ClassVar

from sqlalchemy import Column, ForeignKey, Integer, String

from florestsdk.database import Base


class YaraRuleModel(Base):
    __tablename__ = "yara_rules"
    __table_args__: ClassVar = {"schema": "florest"}

    id = Column(Integer, primary_key=True)
    rule_name = Column(String, nullable=False, unique=True)
    rule_content = Column(String, nullable=False, unique=True)
    category = Column(String, nullable=False)  # Usando Enum do SQLAlchemy com o Enum Python
    company_id = Column(Integer, ForeignKey("florest.companies.id"), nullable=False)

    def __repr__(self):
        return f"<YaraRule(id={self.id}, rule_name='{self.rule_name}', category='{self.category}', company_id={self.company_id})>"
