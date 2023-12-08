# itc-flask
## How to run
1. Install virtualenv
```
pip install virtualenv
```
2. Open a terminal and go to the project directory, run
```
python -m venv venv
```
3. Run
```
.\venv\Scripts\activate
```
4. Within the virtual environment, install dependencies using
```
(venv) pip install -r requirements
```
5. Start the server
```
(venv) python task1.py
```
# Send POST, GET, DELETE, and PUT requests using POSTMAN
## Tested requests:
### POST:
```
  /todos
    {
      "title": "title 1",
      "description": "example"
    }
```
### GET:
```
/todos (with no query)

/todos
{
  "completed": true
}

/todos
{
  "completed": false
}
/todos/1 (with no query)
```
### PUT:
```
/todos/1
{
  "title": "title 1",
  "description": "updated",
  "completed": true
}
```
### DELETE:
```
/todos/1 (with no query)
```

      
