from pydantic import BaseModel


class MyModel(BaseModel):
    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    username: str
    email: str
    matricule: int
    password: str


class RecorBase(BaseModel):
    name: str
    description: str

class RecorCreate(RecorBase):
    pass

class Recor(RecorBase):
    id: int

    class Config:
        from_attributes = True
