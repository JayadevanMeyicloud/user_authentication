from pydantic import BaseModel, EmailStr
from typing import Optional,List

class UserRegisterRequestDTO(BaseModel):
    username:str
    password:str
    email:EmailStr
    role:Optional[str] = None

class UserLoginRequestDTO(BaseModel):
    email:EmailStr
    password:str


class UserUpdateDTO(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    role: Optional[str] = None

class TokenResponseDTO(BaseModel):
    access_token: str
    token_type: str

class UserResponseDTO(BaseModel):
    id:int
    username:str
    email:EmailStr
    role:str

class LoginResponseDTO(BaseModel):
    message: str
    data: TokenResponseDTO

class UserListResponseDTO(BaseModel):
    message: str
    data: List[UserResponseDTO]

class UserDataResponseDTO(BaseModel):
    message: str
    data: UserResponseDTO
