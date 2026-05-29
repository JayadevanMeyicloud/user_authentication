from dataclasses import dataclass


@dataclass
class UserModel:

    id: int
    username: str
    email: str
    password: str
    role: str