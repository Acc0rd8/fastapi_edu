from users.schemas import UserCreate

def create_user(user_in: UserCreate) -> dict:
    user = user_in.model_dump()
    return {
        'success': True,
        'user': user
    }