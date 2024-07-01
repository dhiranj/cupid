from fastapi import APIRouter, HTTPException
from typing import Dict
from models import User,FriendRequest,RecommendSong
from services.recommendation import recommend_songs_for_user, recommend_songs_with_friends_for_user
from dependencies import validate_username
from fastapi.responses import JSONResponse
from sample_data import get_sample_users, make_sample_friends


router = APIRouter()

users: Dict[str, User] = {}

sample_users = get_sample_users()
for user in sample_users:
    users[user.name] = user

sample_connections = make_sample_friends()

for each_pairing in sample_connections:

    for user,frnds_lst in each_pairing.items():

        users[user].friends.extend(frnds_lst)




@router.post("/add_user/")
def add_user(user: User):
    if user.name in users:
        raise HTTPException(status_code=400, detail="User already exists.")
    users[user.name] = user
    return JSONResponse(status_code=200, content={"message": "User added successfully."})


@router.post("/add_friend/")
def add_friend(request: FriendRequest):
    user_name = validate_username(request.user_name)
    friend_name = validate_username(request.friend_name)
    if user_name not in users:
        raise HTTPException(status_code=404, detail="User not found")
    if friend_name not in users:
        raise HTTPException(status_code=404, detail="Friend not found")
    
    user = users[user_name]
    friend = users[friend_name]

    if friend_name not in user.friends:
        user.friends.append(friend_name)
    if user_name not in friend.friends:
        friend.friends.append(user_name)
    
    return {"message": "Friend added successfully"}

@router.post("/recommend_songs/")
def recommend_songs(request: RecommendSong):
    user_name = validate_username(request.user_name)
    return recommend_songs_for_user(user_name, users)

@router.post("/recommend_songs_with_friends/")
def recommend_songs_with_friends(request: RecommendSong):
    user_name = validate_username(request.user_name)
    return recommend_songs_with_friends_for_user(user_name, users)

