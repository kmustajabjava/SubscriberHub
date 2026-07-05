from repositories.base_repository import BaseRepository


class PaymentRepository(BaseRepository):

    def insert_payment(self, payment):

        connection = self.get_db_connection()
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

    def get_all_payments(self):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()

            cursor = connection.cursor(dictionary=True)

            query = """
                SELECT
                    pay.PaymentID,
                    c.FullName,
                    pl.PlanName,
                    pay.Amount,
                    pay.PaymentMethod,
                    pay.PaymentDate,
                    pay.Status
                FROM Payments pay
                INNER JOIN Subscriptions s
                    ON pay.SubscriptionID = s.SubscriptionID
                INNER JOIN Customers c
                    ON s.CustomerID = c.CustomerID
                INNER JOIN Plans pl
                    ON s.PlanID = pl.PlanID
                ORDER BY pay.PaymentID DESC
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

    
    def get_payment_by_id(self, payment_id):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()

            cursor = connection.cursor(dictionary=True)

            query = """
                SELECT
                    pay.PaymentID,
                    c.FullName,
                    pl.PlanName,
                    pay.Amount,
                    pay.PaymentMethod,
                    pay.PaymentDate,
                    pay.Status
                FROM Payments pay
                INNER JOIN Subscriptions s
                    ON pay.SubscriptionID = s.SubscriptionID
                INNER JOIN Customers c
                    ON s.CustomerID = c.CustomerID
                INNER JOIN Plans pl
                    ON s.PlanID = pl.PlanID
                WHERE pay.PaymentID = %s
            """

            cursor.execute(query, (payment_id,))

            return cursor.fetchone()

        except Exception as e:

            print(f"Database Error: {e}")
            return None

        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()


    def complete_payment(self, payment_id):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()

            cursor = connection.cursor()

            query = """
                UPDATE Payments
                SET Status = 'Completed'
                WHERE PaymentID = %s
                AND Status = 'Pending'
            """

            cursor.execute(query, (payment_id,))

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

    def fail_payment(self, payment_id):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()

            cursor = connection.cursor()

            query = """
                UPDATE Payments
                SET Status = 'Failed'
                WHERE PaymentID = %s
                AND Status = 'Pending'
            """

            cursor.execute(query, (payment_id,))

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

    
    def refund_payment(self, payment_id):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()

            cursor = connection.cursor()

            query = """
                UPDATE Payments
                SET Status = 'Refunded'
                WHERE PaymentID = %s
                AND Status = 'Completed'
            """

            cursor.execute(query, (payment_id,))

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

    def get_customer_payment_history(self, customer_id):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()

            cursor = connection.cursor(dictionary=True)

            query = """
                SELECT
                    pay.PaymentID,
                    pl.PlanName,
                    pay.Amount,
                    pay.PaymentMethod,
                    pay.PaymentDate,
                    pay.Status
                FROM Payments pay
                INNER JOIN Subscriptions s
                    ON pay.SubscriptionID = s.SubscriptionID
                INNER JOIN Plans pl
                    ON s.PlanID = pl.PlanID
                WHERE s.CustomerID = %s
                ORDER BY pay.PaymentDate DESC
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