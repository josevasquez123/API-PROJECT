# API-PROJECT

API to create, read, update and delete project posts for each user previously logged, also has a fast searching by filter tags.

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

## Some Endpoints Structure

### Create Project
Example for json format to create a project
```
{
  "creator": "jose",
  "project_name": "POKEMON",
  "status": "IN PROGRESS",
  "tag": "APP GAMES",
  "created_at": "2022-12-05T14:36:32.162461",
  "date_creation": "2022-12-05",
  "content": {
    "ADD NEW POKEMONS": [
      "ADD LEGENDARY POKEMONS",
      "ADD MORE WATER POKEMON"
    ],
    "EDIT POKEMON POWERS": [
      "INCREASE FIRE POWER DAMAGE"
    ]
  }
}
```
In content, you can add as many entities as you want but with same example format

### Update Project
Each project has an id, you can see this information in **Get Project** endpoint, write project id you want to update and complete all you want to change

### Filter By
This endpoint need two values, your filter tag and its value. Filter tag can be creator, project_name, date_creation, etc. (Keep in mind you have to write the same filter tag word used in Creation Project endpoint)

Examples:

```
{
  "filter_tag": "creator",
  "value": "jose"
}
```
```
{
  "filter_tag": "date_creation",
  "value": "2022-12-05"
}
```
```
{
  "filter_tag": "project_name",
  "value": "POKEMON"
}
```

That's all, have fun and test all endpoints :smile:
