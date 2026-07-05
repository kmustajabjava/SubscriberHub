from config.database import get_connection


class BaseRepository:

    def get_db_connection(self):
        return get_connection()