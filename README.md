# Flask Microblog

### Setting up the application on a Windows machine

1. Checking Python installation

```
python --version
```

2. Create a folder

```
mkdir microblog
```

3. Create a virtual Environment

```
python -m venv venv
```

4. Activate the virtual environment

```
venv\Scripts\activate
```

5. Set the Flash environment variable

```
set FLASK_APP=microblog.py
```

6. Run the application

```
flask run
```

7. Run Flask in a custom port

```
flask run --port 5001
```

