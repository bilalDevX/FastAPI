# Import the FastAPI class from the fastapi module
from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a dynamic route with a path parameter {post_id}
@app.get("/blog/{post_id}")
async def read_blog(post_id: int):  
    """
    Retrieve blog post by its ID.
    
    Args:
        post_id (int): The ID of the blog post (must be an integer).
    
    Returns:
        dict: A dictionary containing the blog post ID.
    """
    return {"data": post_id}
