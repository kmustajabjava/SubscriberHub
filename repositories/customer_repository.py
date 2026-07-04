from config.database import get_connection
from models.customer import Customer


class CustomerRepository:

    def get_all_customers(self):

        connection = get_connection()

        cursor = connection.cursor()

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

            customer = Customer(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6]
            )

            customers.append(customer)

        cursor.close()
        connection.close()

        return customers