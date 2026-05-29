from app.repository.user_repository import(
    get_user_by_email,
    create_user,
    get_all_users,
    get_user_by_id,
    update_user_repo,
    delete_user_repo,
    update_user_partial_repo,
)
from app.utils.auth import(
    hash_password,
    verify_password,
    create_access_token
)
from app.utils.constants import DEFAULT_ROLE
from app.utils.exceptions import AppException
from app.utils.logger import logger

def serialize_user(user):

    logger.debug(f"Serializing user: {user['id']}")
    return {
        "id": user["id"],
        "username": user["username"],
        "email": user["email"],
        "role": user["role"]
    }

def register_user(user_data):

    logger.info(f"Register attempt for email: {user_data.email}")
    existing_user = get_user_by_email(
        user_data.email
    )
    if existing_user:
        logger.warning(f"User already exists: {user_data.email}")
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
    logger.info(f"User registered successfully: {user_data.email}")
    return serialize_user(user)

def login_user(user_data):

    logger.info(f"Login attempt: {user_data.email}")
    user = get_user_by_email(
        user_data.email
    )
    if not user:
        logger.error(f"Invalid email login attempt: {user_data.email}")
        raise AppException(
            "Invalid email"
        )
    if not verify_password(
        user_data.password,
        user["password"]
    ):
        logger.error(f"Invalid password login attempt: {user_data.email}")
        raise AppException(
            "Invalid password"
        )    
    token = create_access_token(
        {
            "user_id": user["id"],
            "role": user["role"]
        }
    )
    logger.info(f"User logged in successfully: {user_data.email}")
    return {
        "access_token": token,
        "token_type": "bearer"
    }

def fetch_all_users(page, limit):

    logger.info("Fetching all users")

    offset = (page - 1) * limit
    users = get_all_users(limit, offset)
    
    logger.info(f"Retrieved {len(users)} users")
    return [
        serialize_user(user)
        for user in users
    ]

def fetch_user_by_id(user_id):

    logger.info(f"Fetching user by ID: {user_id}")
    user = get_user_by_id(user_id)
    if not user:
        logger.error(f"User not found: {user_id}")
        raise AppException(
            "User not found"
        )
    
    return serialize_user(user)

def update_user_full(user_id, user_data):

    logger.info(f"Updating user completely: {user_id}")
    user = get_user_by_id(user_id)

    if not user:
        logger.error(f"User not found for update: {user_id}")
        raise AppException("User not found")
    
    updated_user = update_user_repo(
        user_id,
        user_data.username,
        user_data.email,
        hash_password(user_data.password),
        user_data.role
    )
    logger.info(f"User updated successfully: {user_id}")

    return serialize_user(updated_user)

def update_user_partial(user_id, username, email, password, role):

    logger.info(f"Updating user partially: {user_id}")

    user = get_user_by_id(user_id)
    if not user:
        logger.error(f"User not found for partial update: {user_id}")
        raise AppException("User not found")

    updated_user = update_user_partial_repo(
        user_id,
        username,
        email,
        hash_password(password) if password else None,
        role
    )
    logger.info(f"User partially updated: {user_id}")

    return serialize_user(updated_user)

def delete_user(user_id):

    logger.info(f"Delete request for user_id: {user_id}")
    user = get_user_by_id(user_id)

    if not user:
        logger.error(f"User not found for delete: {user_id}")
        raise AppException("User not found")

    delete_user_repo(user_id)
    logger.info(f"User deleted successfully: {user_id}")

    return {
        "message": "User deleted successfully",
        "user_id": user_id
    }