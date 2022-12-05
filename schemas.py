from pydantic import BaseModel, EmailStr
from datetime import datetime, date
from typing import Optional, Dict, Union

class UserCredentials(BaseModel):
    email: EmailStr
    password: str

class Filter(BaseModel):
    filter_tag: str
    value: Union[str,date]

class Token(BaseModel):
    access_token: str
    token_type: str

class ProjectCreate(BaseModel):
    id: str = None
    creator: str
    project_name:  str
    status: str
    tag: str
    created_at: datetime = datetime.now()
    date_creation: date = date.today().strftime('%Y-%m-%d')
    content: Optional[Dict[str, list]] = None

class ProjectUpdate(BaseModel):
    creator: str
    project_name:  str
    status: str
    tag: str
    content: Optional[Dict[str, list]] = None

class ProjectOut(ProjectCreate):
    pass

class TokenData(BaseModel):
    id: Optional[str] = None