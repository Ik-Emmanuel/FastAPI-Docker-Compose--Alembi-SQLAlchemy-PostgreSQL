from pydantic import BaseModel
from typing import Optional

class Post(BaseModel):
    title: str
    likes: int
    author_id: int

    class Config:
        orm_mode = True



class AuthorIn(BaseModel):
    name: str
    age: int

    class Config:
        orm_mode = True


class Author(AuthorIn):
    id: int
