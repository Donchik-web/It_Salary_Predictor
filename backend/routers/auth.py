from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

from database.connection import get_db_session
from settings.main_utils import verify_token
from backend.schemas.validators import EmailRegistrationRequest, UserRegistration, LoginRequest, VacancyRequest
from backend.services.helpers import generate_send_confirm_code, process_registration_fastAPI, process_login_fastAPI, process_vacancy_data

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login-token")


@router.post("/send-email-code")
async def send_email_code(email_req: EmailRegistrationRequest):
    return generate_send_confirm_code(email_req)


@router.post("/registration")
async def registration(user_data: UserRegistration, session: Session = Depends(get_db_session)):
    return process_registration_fastAPI(user_data, session)


@router.post("/login-token")
async def login_for_access_token(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Неверный токен")
    return {"message": "Токен верный", "user_id": payload.get("sub")}


@router.post("/login-pwd")
async def login_with_pwd(data: LoginRequest, session: Session = Depends(get_db_session)):
    return process_login_fastAPI(data, session)


@router.post("/vacancy-data")
async def specify_vacancy_data(vacancy_data: VacancyRequest):
    return process_vacancy_data(vacancy_data)
