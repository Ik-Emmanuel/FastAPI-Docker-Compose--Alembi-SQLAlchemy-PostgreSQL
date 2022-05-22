import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from schemas import Post as SchemaPost, Author as SchemaAuthor, AuthorIn
from models import Post, Author

from dotenv import load_dotenv

load_dotenv(".env")


app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])



@app.get("/")
async def root():
    return {"message": "Hello to postgresSQL FastAPI with Docker and docker compose"}


@app.post("/add-post/", response_model=SchemaPost)
def add_post(post:SchemaPost):
    """ This adds a new post by a given author to the db"""
    db_post = Post(title=post.title, likes=post.likes, author_id=post.author_id)
    db.session.add(db_post)
    db.session.commit()
    return db_post

    
@app.post("/add-author/", response_model=SchemaAuthor)
def add_author(author:AuthorIn):
    """ This adds a `new author` to the db"""
    db_author = Author(name=author.name, age=author.age)
    db.session.add(db_author)
    db.session.commit()
    return db_author

@app.get("/posts/")
def get_posts():
    posts = db.session.query(Post).all()
    return posts
