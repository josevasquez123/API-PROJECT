# API-PROJECT
Project Structure:
- main: Main code for API
- database: Store the databases
- schemas: BaseModel Structures
- utils: Encryption functions
- auth: User authentication and token user creation
- routers: router endpoints folder
  - filter: Endpoint for searching by specific filter (i.e. search by creator)
  - project: Endpoint for CRUD operations about project posts
  - user: Endpoint for Sign Up and Log In

##How to Use
Clone this repository, install all libraries from requirements.txt and write the next line in root project cmd
```
uvicorn main:app --reload
```
