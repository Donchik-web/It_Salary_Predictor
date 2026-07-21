import uuid
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class VacancyInfo(Base):
    __tablename__ = 'vacancy_info'
    """Таблица, содержащая поля для описания конкретной вакансии"""
    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String(255), nullable=False)
    experience = Column(String(255), nullable=False)
    work_format = Column(String(255), nullable=False)
    common_employment = Column(String(255), nullable=False)
    work_schedule = Column(String(255), nullable=False)
    work_hours = Column(String(255), nullable=False)
    name_company = Column(String(255), nullable=False)
    city = Column(String(50), nullable=False)
    address = Column(String(255), nullable=False)
    count_payments = Column(String(255), nullable=False)
    detailed_information = Column(Text, nullable=False)
    skills = Column(ARRAY(String), nullable=False)
    salary = Column(String(255), nullable=False)


class Users(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    hash_pwd = Column(String(255), nullable=False)
    token = Column(String(255), nullable=False, unique=True)
