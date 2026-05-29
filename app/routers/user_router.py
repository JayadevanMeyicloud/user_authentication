from fastapi import APIRouter, Depends
from app.services.user_services import (
    fetch_all_users,
    fetch_user_by_id,
    update_user_full,
    update_user_partial_repo,
    delete_user
)
from app.utils.response import success_response
from app.utils.dependencies import require_admin
from app.schemas.user_schema import (
    UserUpdateDTO,
    UserDataResponseDTO,
    UserListResponseDTO
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/", response_model=UserListResponseDTO)
def get_users(
    page: int = 1,
    limit: int = 10,
    current_user: dict = Depends(require_admin)
    ):

    result = fetch_all_users(page,limit)

    return success_response(
        message="Users fetched successfully",
        data=result
    )

@router.get("/{user_id}", response_model=UserDataResponseDTO)
def get_user(user_id: int, current_user: dict = Depends(require_admin)):

    result = fetch_user_by_id(user_id)

    return success_response(
        message="User fetched successfully",
        data=result
    )

@router.put("/{user_id}", response_model=UserDataResponseDTO)
def update_user(
    user_id: int,
    user: UserUpdateDTO,
    current_user: dict = Depends(require_admin)
):
    result = update_user_full(user_id, user)

    return success_response(
        message="User updated successfully",
        data=result
    )

# PATCH (PARTIAL UPDATE)
@router.patch("/{user_id}", response_model=UserDataResponseDTO)
def patch_user(
    user_id: int,
    user: UserUpdateDTO,
    current_user: dict = Depends(require_admin)
):
    result = update_user_partial_repo(
        user_id, 
        user.username,
        user.email,
        user.password,
        user.role
)

    return success_response(
        message="User partially updated successfully",
        data=result
    )

# DELETE
@router.delete("/{user_id}", response_model=UserDataResponseDTO)
def delete_user_route(
    user_id: int,
    current_user: dict = Depends(require_admin)
):
    result = delete_user(user_id)

    return success_response(
        message="User deleted successfully",
        data=result
    )