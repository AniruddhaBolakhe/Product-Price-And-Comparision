from pydantic import BaseModel,EmailStr

class UserRegistrationPydantic(BaseModel):
    
    email:EmailStr
    username:str
    password:str

class UserLoginPydantic(BaseModel):
    email: EmailStr
    password: str