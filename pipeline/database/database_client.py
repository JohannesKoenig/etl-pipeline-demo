from psycopg2.extensions import connection
from psycopg2 import connect


def get_database_connection(
    host: str, port: str, user: str, password: str, database: str
) -> connection:
    return connect(
        f"postgresql://{user}:{password}@{host}:{port}/{database}"
    )

class DatabaseClient:
    def __init__(self, database_connection: connection) -> None:
        self._database_connection = database_connection

    def run_query(self, query: str) -> None:
        with self._database_connection.cursor() as cursor:
            cursor.execute(query)
            self._database_connection.commit()