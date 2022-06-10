# attend
lab. aplicativos híbridos

https://python-poetry.org/docs/master#installing-with-the-official-installer

# commands
poetry shell

poetry install

python -m uvicorn src.main:app --reload --host 0.0.0.0

# db
create a local postgresql instance

create a db named 'attend'

update the connection_string in src/infra/config/db -> DATABASE_URL = "postgresql://USER:PASSWORD@localhost/attend"
