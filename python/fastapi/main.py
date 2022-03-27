from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
async def root():
    return {"message": "welcome to my api"}


@app.get("/posts")
def get_posts():
    return {"data": ["This is your post"]}


@app.get("/items/{item_name}")
async def items(item_name):
    return {"item_name": item_name}


@app.post("/createpost")
def create_posts(post: Post):
    print(post)
    return {"message": "success", "new_post": post}
