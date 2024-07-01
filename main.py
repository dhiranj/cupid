from fastapi import FastAPI
from routes import songs, users
from sample_data import get_sample_songs, get_sample_users, make_sample_friends

app = FastAPI()

app.include_router(songs.router, prefix="/songs", tags=["songs"])
app.include_router(users.router, prefix="/users", tags=["users"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
