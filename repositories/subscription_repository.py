from config.database import get_connection
from models.subscription import Subscription


class SubscriptionRepository:

    def expire_active_subscriptions(self, customer_id):

        connection = get_connection()
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

        connection = get_connection()
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