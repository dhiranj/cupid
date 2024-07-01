from pydantic import BaseModel, Field, validator, root_validator
from typing import List
from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

class Song(BaseModel):
    name: str = Field(..., max_length=50)
    genre: str
    tempo: str
    singer: str = Field(..., max_length=50)
    popularity_score: float = Field(..., ge=0, le=100)
    release_year: int

    @validator('name', 'genre', 'tempo', 'singer', pre=True, always=True)
    def lower_case_strings(cls, value: str) -> str:
        return value.lower()

    @validator('genre')
    def validate_genre(cls, value):
        known_genres = {"pop", "rock", "jazz", "classical", "hiphop"}
        if value not in known_genres:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=f'Genre must be one of {known_genres}')
        return value


    @validator('tempo')
    def validate_tempo(cls, value):
        known_tempos = {"fast", "medium", "slow"}
        if value not in known_tempos:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=f'Tempo must be one of {known_tempos}')
        return value


class User(BaseModel):
    name: str = Field(..., max_length=50)
    playlist: List[str]
    friends: List[str]

    @validator('name', pre=True, always=True)
    def lower_case_name(cls, value: str) -> str:
        return value.lower()

    @root_validator(pre=True)
    def validate_playlist_and_friends(cls, values):
        from routes.songs import library
        from routes.users import users as user_dict

        playlist = [song.lower() for song in values.get('playlist', [])]
        friends = [friend.lower() for friend in values.get('friends', [])]

        # Validate that all songs in the playlist are in the library
        for song in playlist:
            if song not in library:
                raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=f'Song "{song}" is not present in the library')


        # Validate that all friends are existing users
        for friend in friends:
            if friend not in user_dict:
                raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=f'User "{friend}" is not a known user')


        values['playlist'] = playlist
        values['friends'] = friends
        return values

class FriendRequest(BaseModel):
    user_name: str
    friend_name: str

class RecommendSong(BaseModel):
    user_name: str