from repositories.base_repository import BaseRepository


class SupportTicketRepository(BaseRepository):
    
    def insert_ticket(self, ticket):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()

            cursor = connection.cursor()

            query = """
                INSERT INTO SupportTickets
                (
                    CustomerID,
                    IssueType,
                    Description,
                    Priority,
                    Status,
                    CreatedDate
                )
                VALUES
                (%s, %s, %s, %s, %s, %s)
            """

            cursor.execute(
                query,
                (
                    ticket.customer_id,
                    ticket.issue_type,
                    ticket.description,
                    ticket.priority,
                    ticket.status,
                    ticket.created_date
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

        
    def get_all_tickets(self):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()

            cursor = connection.cursor(dictionary=True)

            query = """
                SELECT
                    t.TicketID,
                    c.FullName,
                    t.IssueType,
                    t.Description,
                    t.Priority,
                    t.Status,
                    t.CreatedDate
                FROM SupportTickets t
                INNER JOIN Customers c
                    ON t.CustomerID = c.CustomerID
                ORDER BY t.TicketID DESC
            """

            cursor.execute(query)

            return cursor.fetchall()

        except Exception as e:

            print(f"Database Error: {e}")
            return []

        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()

    def get_ticket_by_id(self, ticket_id):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()

            cursor = connection.cursor(dictionary=True)

            query = """
                SELECT
                    t.TicketID,
                    c.FullName,
                    t.IssueType,
                    t.Description,
                    t.Priority,
                    t.Status,
                    t.CreatedDate
                FROM SupportTickets t
                INNER JOIN Customers c
                    ON t.CustomerID = c.CustomerID
                WHERE t.TicketID = %s
            """

            cursor.execute(query, (ticket_id,))

            return cursor.fetchone()

        except Exception as e:

            print(f"Database Error: {e}")
            return None

        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()

            
    def update_ticket_status(self, ticket_id, status):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()

            cursor = connection.cursor()

            query = """
                UPDATE SupportTickets
                SET Status = %s
                WHERE TicketID = %s
            """

            cursor.execute(
                query,
                (
                    status,
                    ticket_id
                )
            )

            connection.commit()

            return cursor.rowcount > 0

        except Exception as e:

            print(f"Database Error: {e}")
            return False

        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()


    def close_ticket(self, ticket_id):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()

            cursor = connection.cursor()

            query = """
                UPDATE SupportTickets
                SET Status = 'Closed'
                WHERE TicketID = %s
                AND Status != 'Closed'
            """

            cursor.execute(query, (ticket_id,))

            connection.commit()

            return cursor.rowcount > 0

        except Exception as e:

            print(f"Database Error: {e}")
            return False

        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()


    def get_customer_ticket_history(self, customer_id):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()

            cursor = connection.cursor(dictionary=True)

            query = """
                SELECT
                    TicketID,
                    IssueType,
                    Description,
                    Priority,
                    Status,
                    CreatedDate
                FROM SupportTickets
                WHERE CustomerID = %s
                ORDER BY CreatedDate DESC
            """

            cursor.execute(query, (customer_id,))

            return cursor.fetchall()

        except Exception as e:

            print(f"Database Error: {e}")
            return []

        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()