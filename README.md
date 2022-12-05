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

## How to Use
Clone this repository, install all libraries from requirements.txt and write the next line in root project cmd
```
uvicorn main:app --reload
```
## Testing
Type **http://127.0.0.1:8000/filter** in your browser (I used Google Chrome) and you will get this interface

![image](https://user-images.githubusercontent.com/55626381/205750077-c38bd037-273f-49ca-a914-22bd8b0e653d.png)

Before to use Project and Filter By endpoints, you have to Sign Up to create a user account. If you don't have an account, you can't use the endpoints.

Steps:
- Clic in signup endpoint, then clic in **Try it out** and write your email and password (this information is in json format, don't change email or password words)
- Clic in **Authorize** and complete username and password, then clic in **Authorize**

That's all, have fun and test all endpoints :smile:
