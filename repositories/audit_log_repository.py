from repositories.base_repository import BaseRepository


class AuditRepository(BaseRepository):

    def log_action(self, customer_id, action):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()

            cursor = connection.cursor()

            query = """
                INSERT INTO AuditLogs
                (
                    CustomerID,
                    ActionPerformed
                )
                VALUES
                (%s, %s)
            """

            cursor.execute(
                query,
                (
                    customer_id,
                    action
                )
            )

            connection.commit()
            return True

        except Exception as e:

            print(f"Database Error: {e}")
            return False

        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()