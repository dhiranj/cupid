from typing import Dict
from models import Song, User
from routes.songs import library
from fastapi import  HTTPException
from collections import defaultdict

def similarity_index(song1: Song, song2: Song) -> float:
    attributes = ['genre', 'tempo', 'singer', 'popularity_score', 'release_year']
    same_attributes = sum(1 for attr in attributes if getattr(song1, attr) == getattr(song2, attr))
    return same_attributes / len(attributes)

def recommend_songs_for_user(user_name: str, users: Dict[str, User]):
    if user_name not in users:
        raise HTTPException(status_code=404, detail="User not found.")
    user = users[user_name]
    user_songs = {song for song in user.playlist}
    recommendations = []

    for song_name, song in library.items():
        if song_name in user_songs:
            continue
        max_si = max((similarity_index(song, library[playlist_song]) for playlist_song in user.playlist), default=0)
        recommendations.append((song_name, max_si))

    recommendations.sort(key=lambda x: x[1], reverse=True)
    return {"recommendations": [song for song, _ in recommendations]}

def recommend_songs_with_friends_for_user(user_name: str, users: Dict[str, User]):
    if user_name not in users:
        raise HTTPException(status_code=404, detail="User not found.")
    user = users[user_name]
    user_songs = {song for song in user.playlist}
    recommendations = defaultdict(float)

    for song_name, song in library.items():
        if song_name in user_songs:
            continue

        max_si = max((similarity_index(song, library[playlist_song]) for playlist_song in user.playlist), default=0)
        recommendations[song_name] = max_si

        # Friend Similarity Index (FSI)
        friend_count = sum(1 for friend in user.friends if song_name in users[friend].playlist)
        if user.friends:
            fsi = friend_count / len(user.friends)
            recommendations[song_name] += fsi

    recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return {"recommendations": [song for song, _ in recommendations]}
