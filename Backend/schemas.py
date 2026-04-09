from pydantic import BaseModel, EmailStr, Field
from typing import Annotated

class UserRegistrationPydantic(BaseModel):
    email: Annotated[EmailStr, Field(..., description='Email of the User', examples=['string@email.com'])]
    username: Annotated[str, Field(..., description='Username of the User', examples=['string'])]
    password: Annotated[str, Field(..., min_length=8, description='Password of the User')]

class UserLoginPydantic(BaseModel):
    email: Annotated[EmailStr, Field(..., description='Email of the User', examples=['string@email.com'])]
    password: Annotated[str, Field(..., min_length=8, description='Password of the User')]