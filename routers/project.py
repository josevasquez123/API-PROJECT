from fastapi import status, HTTPException, APIRouter, Depends, Response
from .. import auth,schemas
from fastapi_pagination import Page, paginate
from ..database import projects

#CREATE ROUTER INSTANCE, THIS WILL CALL BY MAIN
router = APIRouter(
    prefix= "/projects",
    tags=['Project']
)


#TRANSFORM PROJECTS FROM DICT TYPE TO LIST TYPE
def get_all_projects(proj_dict):
    temp = []
    for proj in proj_dict:
        temp.append(projects[proj])
    return temp


#END POINT FOR CREATING A PROJECT
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ProjectOut)
def create_project(project:schemas.ProjectCreate,_: str = Depends(auth.get_current_user)):
    id = str(len(projects)+1)
    project = project.copy(update={"id":id})
    projects[id] = dict(project)
    return project


#END POINT FOR GETTING ALL PROJECTS
@router.get("/", response_model= Page[schemas.ProjectOut])
def get_projects(_: str = Depends(auth.get_current_user)):
    project_list = get_all_projects(projects)
    return paginate(project_list)


#END POINT TO DELETE ONE PROJECT BY ID
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(id: str, _: str = Depends(auth.get_current_user)):

    if not id in projects:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"project with id:{id} does not exist")
    
    del projects[id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)


#END POINT TO UPDATE A PROJECT
@router.put("/{id}")
def update_post(id: str, updated_post: schemas.ProjectUpdate, _: str = Depends(auth.get_current_user)):

    if not id in projects:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"project with id:{id} does not exist")

    projects[id].update(updated_post)
    return projects[id]