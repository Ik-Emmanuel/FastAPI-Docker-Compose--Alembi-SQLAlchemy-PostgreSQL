
pip install fastapi, fastapi-sqlalchemy, pydantic, alembic, psycopg2, uvicorn, python-dotenv


docker-compose run app alembic revision --autogenerate -m "New Migration"
docker-compose run app alembic upgrade head 

alembic init alembic

docker-compose build
docker-compose up 

## Connect to DB 

have docker postgres up  -- docker-compose up 
open pgadmin, create new server
    - hostname = localhost 
    - port = localhost port set in docker compose file - 5433:5432 = 5433    
    - enter password stored in .env or configuration 
    - save and connect 