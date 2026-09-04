from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pathlib import Path
posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even b",
        "date_posted": "April 21, 2025",
    }
]

app = FastAPI()

templates = Jinja2Templates(directory=Path(__file__).parent/"templates")

@app.get("/")
@app.get("/posts")

def home():
    return f"<h1> {posts[0]['title']}, {posts[1]['title']}</h1>"

@app.get("/api/posts", include_in_schema=False)
def get_posts(request: Request):
    return templates.TemplateResponse(request,"home.html",{"posts":posts})