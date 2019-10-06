## install dependencies:
 - python -m venv venv
 - venv\Scripts\pip.exe install -r requirements.txt

## run on port 8100 with local db
 - set FLASK_RUN_PORT=8100
 - set NATASHA_MONGO_DB_HOST_URL=localhost
 - set NATASHA_MONGO_DB_PORT=27017
 - venv\Scripts\python.exe -m flask run