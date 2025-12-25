from pydantic import BaseModel
class userBase(BaseModel):
    name:str
    age:int
class UserCreate(userBase):
    pass 
class UserResponse(userBase):
    id:int

    class Config:
        orm_mode=True
