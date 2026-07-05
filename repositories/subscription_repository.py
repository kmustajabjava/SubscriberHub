from models.subscription import Subscription
from repositories.base_repository import BaseRepository


class SubscriptionRepository(BaseRepository):

    def expire_active_subscriptions(self, customer_id):

        connection = self.get_db_connection()
        cursor = connection.cursor()

        query = """
            UPDATE Subscriptions
            SET Status = 'Expired'
            WHERE CustomerID = %s
              AND Status = 'Active'
        """

        cursor.execute(query, (customer_id,))
        connection.commit()

        cursor.close()
        connection.close()


    def insert_subscription(self, subscription):

        connection = self.get_db_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO Subscriptions
            (
                CustomerID,
                PlanID,
                StartDate,
                EndDate,
                Status,
                AutoRenew
            )
            VALUES
            (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (
                subscription.customer_id,
                subscription.plan_id,
                subscription.start_date,
                subscription.end_date,
                subscription.status,
                subscription.auto_renew
            )
        )

        connection.commit()

        subscription_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return subscription_id
    

    def get_all_subscriptions(self):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()

            cursor = connection.cursor(dictionary=True)

            query = """
                SELECT
                    s.SubscriptionID,
                    s.CustomerID,
                    c.FullName,
                    p.PlanName,
                    p.SpeedMbps,
                    p.Price,
                    s.StartDate,
                    s.EndDate,
                    s.Status,
                    s.AutoRenew
                FROM Subscriptions s
                INNER JOIN Customers c
                    ON s.CustomerID = c.CustomerID
                INNER JOIN Plans p
                    ON s.PlanID = p.PlanID
                ORDER BY s.SubscriptionID
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

    def get_subscription_by_id(self, subscription_id):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()

            cursor = connection.cursor(dictionary=True)

            query = """
                SELECT
                    s.SubscriptionID,
                    s.CustomerID,
                    c.FullName,
                    p.PlanName,
                    p.SpeedMbps,
                    p.Price,
                    s.StartDate,
                    s.EndDate,
                    s.Status,
                    s.AutoRenew
                FROM Subscriptions s
                INNER JOIN Customers c
                    ON s.CustomerID = c.CustomerID
                INNER JOIN Plans p
                    ON s.PlanID = p.PlanID
                WHERE s.SubscriptionID = %s
            """

            cursor.execute(query, (subscription_id,))

            return cursor.fetchone()

        except Exception as e:

            print(f"Database Error: {e}")
            return None

        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()

    def pause_subscription(self, subscription_id):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()

            cursor = connection.cursor()

            query = """
                UPDATE Subscriptions
                SET Status = 'Paused'
                WHERE SubscriptionID = %s
                AND Status = 'Active'
            """

            cursor.execute(query, (subscription_id,))

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

    def resume_subscription(self, subscription_id):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()

            cursor = connection.cursor()

            query = """
                UPDATE Subscriptions
                SET Status = 'Active'
                WHERE SubscriptionID = %s
                AND Status = 'Paused'
            """

            cursor.execute(query, (subscription_id,))

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

    def cancel_subscription(self, subscription_id):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()

            cursor = connection.cursor()

            query = """
                UPDATE Subscriptions
                SET Status = 'Cancelled'
                WHERE SubscriptionID = %s
                AND Status IN ('Active', 'Paused')
            """

            cursor.execute(query, (subscription_id,))

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