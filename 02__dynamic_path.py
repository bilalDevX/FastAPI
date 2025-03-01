from fastapi import FastAPI

app = FastAPI()

@app.get("/blog/{post_id}")
def read_blog(post_id: int):
    return {"data": post_id}
    
