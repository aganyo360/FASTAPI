from fastapi import FastAPI

app = FastAPI()

users = ["Stella", "Lenny", "Annael", "Brice"]

@app.get("/users")
async def get_all_users():
    return users

@app.get("/user/{index}")
async def get_a_user(index):
    index = int(index)
    useer = users(index)
    return users

@app.post("/users")
async def add_new_users():
    return users

@app.put("/users")
async def update_users():
    return users

@app.delete("/users")
async def delete_users():
    return users