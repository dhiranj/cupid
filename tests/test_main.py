import pytest
from fastapi.testclient import TestClient
from main import app
from routes.songs import library

client = TestClient(app)

def test_add_user():
    response = client.post("/users/add_user/", json={
        "name": "testuser",
        "playlist": ["Song1", "Song2"],
        "friends": []
    })

    assert response.status_code == 200
    assert response.json() == {"message": "User added successfully."}

def test_add_song():
    response = client.post("/songs/add_song/", json={
        "name": "NewSong",
        "genre": "Pop",
        "tempo": "Medium",
        "singer": "NewSinger",
        "popularity_score": 85.0,
        "release_year": 2022
    })
    assert response.status_code == 200
    assert response.json() == {"message": "Song added successfully."}

def test_add_user_exists():
    response = client.post("/users/add_user/", json={
        "name": "user1",
        "playlist": ["song1", "song2"],
        "friends": []
    })

    assert response.status_code == 400
    assert response.json() == {"detail": "User already exists."}

def test_add_friend():
    response = client.post("/users/add_friend/", json={
        "user_name": "user1",
        "friend_name": "user7"
    })

    assert response.status_code == 200
    assert response.json() == {"message": "Friend added successfully"}

def test_add_friend_not_found():
    response = client.post("/users/add_friend/", json={
        "user_name": "user1",
        "friend_name": "nonexistent"
    })

    assert response.status_code == 404
    assert response.json() == {"detail": "Friend not found"}

def test_recommend_songs():
    response = client.post("/users/recommend_songs/", json = {"user_name":"user1"})
    print(response.json())
    assert response.status_code == 200
    # Adjust this based on your recommendation logic
    assert "recommendations" in response.json()

def test_recommend_songs_with_friends():
    response = client.post("/users/recommend_songs_with_friends/",json = {"user_name":"user1"})
    print(response.json())
    assert response.status_code == 200
    # Adjust this based on your recommendation logic
    assert "recommendations" in response.json()
