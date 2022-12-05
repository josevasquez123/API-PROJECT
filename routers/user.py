from fastapi import status, HTTPException, APIRouter, Depends
from .. import auth,utils,schemas
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from ..database import users_db

#CREATE ROUTER INSTANCE, THIS WILL CALL BY MAIN
router = APIRouter(
    tags=['Users']
)

#CREATE AN ACCOUNT TO GET ACCESS TO PROJECT END POINTS
@router.post("/signup", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCredentials):
    pwd = utils.encrypt_pwd(user.password)
    user.password = pwd
    users_db[user.email] = user

    return user


#CREATE LOGIN AND TEMPORAL TOKEN TO GIVE ACCESS TO USERS
@router.post("/login")
def login(user_credentials: OAuth2PasswordRequestForm = Depends()):
    user: schemas.UserCredentials = users_db[user_credentials.username]
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    access_token = auth.create_access_token(data={"user_id": user.email})

    return {"access_token": access_token, "token_type": "bearer"}