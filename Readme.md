# FastAPI Music Recommendation System

This project implements a simple music recommendation system using FastAPI. Users can add songs, add friends, and receive song recommendations based on their preferences and friends' playlists.

## Features

- **Add User**: Register new users with playlists and friends.
- **Add Song**: Add new songs to the library with details like genre, tempo, and singer.
- **Add Friend**: Connect users as friends.
- **Recommend Songs**: Get song recommendations based on SI.
- **Recommend Songs with Friends**: Get personalized song recommendations based on FSI.

## Setup

### Prerequisites

- Python 3.10.9
- pip (Python package installer)
- Virtual environment (recommended)

### Installation

1. **Clone the repository:**

   ```bash
   git clone git@github.com:dhiranj/cupid.git
   cd cupid
   python3 -m venv myenv
   source myenv/bin/activate
   pip install -r requirements.txt


### Running the Server
1. **Start the FastAPI server:**

   ```bash
   uvicorn main:app --reload

### Example Requests
1. **Add User:**

   ```bash
   curl -X POST "http://localhost:8000/users/add_user/" \
     -H "Content-Type: application/json" \
     -d '{
           "name": "testuser",
           "playlist": ["Song1", "Song2"],
           "friends": []
         }'

2. **Add Friend:**

   ```bash
   curl -X POST "http://localhost:8000/users/add_friend/" \
     -H "Content-Type: application/json" \
     -d '{
           "user_name": "user1",
           "friend_name": "user7"
         }'

3. **Recommend Songs SI:**

   ```bash
   curl -X POST "http://localhost:8000/users/recommend_songs/" \
     -H "Content-Type: application/json" \
     -d '{
           "user_name": "user1"
         }'

4. **Recommend Songs FSI:**

   ```bash
   curl -X POST "http://localhost:8000/users/recommend_songs_with_friends/" \
     -H "Content-Type: application/json" \
     -d '{
           "user_name": "user1"
         }'

5. **Add Song:**

   ```bash
   curl -X POST "http://localhost:8000/songs/add_song/" \
     -H "Content-Type: application/json" \
     -d '{
           "name": "NewSong",
           "genre": "Pop",
           "tempo": "Medium",
           "singer": "NewSinger",
           "popularity_score": 85.0,
           "release_year": 2022
         }'


### Testing
1. **Run tests using pytest:**

   ```bash
   pytest







