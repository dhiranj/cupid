from fastapi import APIRouter, HTTPException
from typing import Dict
from models import Song
from pprint import pprint
from sample_data import get_sample_songs
from fastapi.responses import JSONResponse

router = APIRouter()

library: Dict[str, Song] = {}


sample_songs = get_sample_songs()
for song in sample_songs:
    library[song.name] = song

@router.post("/add_song/")
def add_song(song: Song):
    if song.name in library:
        raise HTTPException(status_code=400, detail="Song already exists in the library.")
    library[song.name] = song
    return JSONResponse(status_code=200, content={"message": "Song added successfully."})
