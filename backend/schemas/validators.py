from pydantic import BaseModel


class UserRegistration(BaseModel):
    email: str
    code: str
    pwd: str
    pwd_confirm: str


class EmailRegistrationRequest(BaseModel):
    email: str


class LoginRequest(BaseModel):
    email: str
    pwd: str


class VacancyRequest(BaseModel):
    title: str
    experience: str
    work_format: str
    common_employment: str
    work_schedule: str
    work_hours: str
    name_company: str
    city: str
    address: str
    count_payments: str
    detailed_information: str
    skills: list