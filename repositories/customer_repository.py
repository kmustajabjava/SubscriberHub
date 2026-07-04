from config.database import get_connection
from models.customer import Customer


class CustomerRepository:

    def get_all_customers(self):

        connection = get_connection()

        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT
                CustomerID,
                FullName,
                Email,
                PhoneNumber,
                City,
                RegistrationDate,
                Status
            FROM Customers
        """)

        rows = cursor.fetchall()

        customers = []

        for row in rows:

            customers.append(
            Customer(
            customer_id=row["CustomerID"],
            full_name=row["FullName"],
            email=row["Email"],
            phone_number=row["PhoneNumber"],
            city=row["City"],
            registration_date=row["RegistrationDate"],
            status=row["Status"]
            )
         )
        cursor.close()
        connection.close()
        return customers
    
    def email_exists(self, email):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT 1 FROM Customers WHERE Email = %s",
            (email,)
        )

        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result is not None
    
    def phone_exists(self, phone):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT 1 FROM Customers WHERE PhoneNumber = %s",
            (phone,)
        )

        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result is not None
    

    def insert_customer(self, customer):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO Customers
            (
                FullName,
                Email,
                PhoneNumber,
                City,
                RegistrationDate,
                Status
            )
            VALUES
            (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (
                customer.full_name,
                customer.email,
                customer.phone_number,
                customer.city,
                customer.registration_date,
                customer.status
            )
        )

        connection.commit()

        cursor.close()
        connection.close()

