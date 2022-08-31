from dotenv import load_dotenv
from os import getenv

load_dotenv()

dataConnection = dict(
    dbname = getenv("DATABASE_PG"),
    user = getenv("USER_PG"),
    port = getenv("PORT_PG"),
    password = getenv("PASSWORD_PG"),
    host = getenv("HOST_PG")
)

