from sqlalchemy.orm import Session

import schemas
from db import models


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.DBAuthor(
        name=author.name,
        description=author.bio,
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)

    return db_author
