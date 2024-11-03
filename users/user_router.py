from fastapi import APIRouter

from users.schemas import UserCreate
from users import crud

router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.post('/')
def create_user(user: UserCreate):
    return crud.create_user(user_in=user)