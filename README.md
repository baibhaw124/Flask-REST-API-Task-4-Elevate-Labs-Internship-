# Flask-REST-API-Task-4-Elevate-Labs-Internship-
This project is part of the Elevate Labs Python Developer Internship (Task 4). The goal is to build a simple but complete REST API using Flask that performs all CRUD operations (Create, Read, Update, Delete) on user data stored in memory.
The project helps in understanding:
REST API fundamentals
HTTP methods (GET, POST, PUT, DELETE)
JSON data handling
API testing using Thunder Client inside VS Code

🛠️ Tech Stack
Python
Flask
Thunder Client (API Testing)
VS Code

📂 Project Features
✔️ 1. GET – Fetch All Users
Fetches the list of all registered users.

GET /users
✔️ 2. POST – Add a New User
Adds a new user to the in-memory list.

POST /users
JSON Body:
{
  "name": "Rohit",
  "email": "rohit@example.com"
}

✔️ 3. PUT – Update Existing User
Updates the name/email of the user with a given ID.
PUT /users/<id>

JSON Body (update any field):
{
  "name": "Updated Name"
}
✔️ 4. DELETE – Remove a User
Deletes the user with a given ID.
DELETE /users/<id>

⚡ Thunder Client – Easy API Testing Inside VS Code
This project uses Thunder Client, a lightweight API testing extension inside VS Code.

🔹 How to Install:
Open VS Code
Click Extensions (4 squares icon)
Search Thunder Client
Click Install

🔹 How to Use Thunder Client:
Open the ⚡ Thunder Client icon on the left
Click New Request
Choose method → GET / POST / PUT / DELETE
Enter URL like:
http://127.0.0.1:5000/users
For POST/PUT → Add JSON body

▶️ How to Run the Project
Install Flask:
pip install flask
Run the app:
python app.py
The server starts at:
http://127.0.0.1:5000/
Test the API using Thunder Client or Postman.

📌 Project File: app.py
Contains all routes:
/ — Welcome message
/users — GET & POST
/users/<id> — PUT & DELETE
Users are stored in:
users = []
This is in-memory, meaning data resets when you restart the server.
