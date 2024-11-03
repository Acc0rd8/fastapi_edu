from pydantic import BaseModel, EmailStr, Field
from typing import Annotated


class UserCreate(BaseModel):
    username: Annotated[str, Field(min_length=3, max_length=20)]
    email: EmailStr

