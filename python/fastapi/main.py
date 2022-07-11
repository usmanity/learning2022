from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {"title": "num 1", "content": "first post", "id": 1},
    {"title": "second post", "content": "this is the second post", "id": 2},
]


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
        else:
            return None


@app.get("/")
async def root():
    return {"message": "welcome to my api"}


@app.get("/posts")
def get_posts():
    return {"data": ["This is your post"]}


@app.get("/items/{item_name}")
async def items(item_name):
    return {"item_name": item_name}


@app.post("/post")
def create_posts(post: Post):
    print(post)
    return {"message": "success", "new_post": post}


@app.get("/posts/{id}")
def get_posts(id: int):
    post = find_post(int(id))
    return {"post": post}
