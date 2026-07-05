from config.database import get_connection


class PaymentRepository:

    def insert_payment(self, payment):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO Payments
            (
                SubscriptionID,
                Amount,
                PaymentDate,
                PaymentMethod,
                Status
            )
            VALUES
            (%s, %s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (
                payment.subscription_id,
                payment.amount,
                payment.payment_date,
                payment.payment_method,
                payment.status
            )
        )

        connection.commit()

        cursor.close()
        connection.close()