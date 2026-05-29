from fastapi import APIRouter
from app.schemas.user_schema import (
    UserRegisterRequestDTO,
    UserLoginRequestDTO
)
from app.services.user_services import (
    register_user,
    login_user
)
from app.utils.response import success_response

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
def register(
    user: UserRegisterRequestDTO
):

    result = register_user(user)

    return success_response(
        message="User registered successfully",
        data=result
    )

@router.post("/login")
def login(
    user: UserLoginRequestDTO
):

    result = login_user(user)

    return success_response(
        message="Login successful",
        data=result
    )