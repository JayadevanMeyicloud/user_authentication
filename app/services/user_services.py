from app.repository.user_repository import(
    get_user_by_email,
    create_user,
    get_all_users,
    get_user_by_id,
    update_user_repo,
    update_user_partial_repo,
    delete_user_repo
)
from app.utils.auth import(
    hash_password,
    verify_password,
    create_access_token
)
from app.utils.constants import DEFAULT_ROLE
from app.utils.exceptions import AppException

import logging

logger = logging.getLogger(__name__)

def serialize_user(user):
    logger.debug(f"Serializing user: {user['id']}")
    return {
        "id": user["id"],
        "username": user["username"],
        "email": user["email"],
        "role": user["role"]
    }

def register_user(user_data):
    existing_user = get_user_by_email(
        user_data.email
    )
    if existing_user:
        raise AppException(
            "User already Exists"
        )
    hashed_password = hash_password(
        user_data.password
    )
    role = getattr(user_data, "role", None) or DEFAULT_ROLE
    user = create_user(
        username=user_data.username,
        email=user_data.email,
        password=hashed_password,
        role=role
    )
    return serialize_user(user)

def login_user(user_data):
    user = get_user_by_email(
        user_data.email
    )
    if not user:
        raise AppException(
            "Invalid email"
        )
    if not verify_password(
        user_data.password,
        user["password"]
    ):
        raise AppException(
            "Invalid password"
        )    
    token = create_access_token(
        {
            "user_id": user["id"],
            "role": user["role"]
        }
    )
    return {
        "access_token": token,
        "token_type": "bearer"
    }

def fetch_all_users():
    users = get_all_users()
    return [
        serialize_user(user)
        for user in users
    ]

def fetch_user_by_id(user_id):
    user = get_user_by_id(user_id)
    if not user:
        raise AppException(
            "User not found"
        )
    return serialize_user(user)

def update_user_full(user_id, user_data):
    user = get_user_by_id(user_id)
    if not user:
        raise AppException("User not found")
    
    updated_user = update_user_repo(
        user_id,
        user_data.username,
        user_data.email,
        hash_password(user_data.password),
        user_data.role
    )

    return serialize_user(updated_user)

def update_user_partial_repo(user_id, user_data):

    user = get_user_by_id(user_id)
    if not user:
        raise AppException("User not found")
    updated_user = update_user_repo(
        user_id=user_id,

        username=user_data.username or user["username"],
        email=user_data.email or user["email"],
        password=hash_password(user_data.password) if user_data.password else None,
        role=user_data.role or user["role"]
    )

    return serialize_user(updated_user)

def delete_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        raise AppException("User not found")

    return delete_user_repo(user_id)