from fastapi import FastAPI
from .routers import user, project, filter
from fastapi_pagination import add_pagination


app = FastAPI()

#ADD PAGINATION
add_pagination(app)

#ADD USER, PROJECT AND FILTER END POINTS
app.include_router(user.router)
app.include_router(project.router)
app.include_router(filter.router)

@app.get("/")
def root():
    return {'message':'welcome'}

