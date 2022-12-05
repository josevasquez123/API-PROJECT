from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from fastapi import Depends, status, HTTPException
from . import schemas
from os.path import join, dirname
from dotenv import load_dotenv
import os

#LOAD SECRET VARIABLES FROM .ENV
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


#AUTHENTICATION METHOD FOR FASTAPI

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')              #THIS FUNCTION GET CREATED TOKEN FROM USER WHO RECENTLY LOGIN

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60*24


#CREATE AN ACCESS TOKEN WITH JWT ENCODE, (JWT = JSON WEB TOKEN)
def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


#VERIFY ACCESS TOKEN FROM USER
def verify_access_token(token: str, credentials_exception):

    try:

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception

    return token_data


#FUNCTION THAT HAS TO BE CALLED FOR EACH END POINT THAT NEEDS AUTENTHICATION BEFORE USING
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

    token = verify_access_token(token, credentials_exception)

    return token