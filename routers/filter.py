from fastapi import status, HTTPException, APIRouter, Depends
from .. import auth,schemas
from ..database import projects
from fastapi_pagination import Page, paginate

#CREATE ROUTER INSTANCE, THIS WILL CALL BY MAIN
router = APIRouter(
    prefix= "/filter",
    tags=['Filter By']
)


#FILTER FUNCTION TO GET A FASTER PROJECT SEARCH
@router.post("/", response_model=Page[schemas.ProjectOut])
def filter_by(filter:schemas.Filter,_: str = Depends(auth.get_current_user)):
    
    project_list = []
    for id in projects:
        project = projects[id]
        if not filter.filter_tag in project:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Filter selections does not exist")
        if project[filter.filter_tag] == filter.value:
            project_list.append(project)
    
    return paginate(project_list)
