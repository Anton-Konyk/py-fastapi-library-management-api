import datetime

from pydantic import BaseModel
class BookBase(BaseModel):
    title: str
    summary: str
    publication_date: datetime.date



class AuthorBase(BaseModel):
    name: str
    bio: str


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int
    books:  list[Book]

    class Config:
        orm_mode = True
