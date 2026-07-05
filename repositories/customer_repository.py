from models.customer import Customer

from repositories.base_repository import BaseRepository


class CustomerRepository(BaseRepository):

    def _build_customer(self, row):

        return Customer(
            customer_id=row["CustomerID"],
            full_name=row["FullName"],
            email=row["Email"],
            phone_number=row["PhoneNumber"],
            city=row["City"],
            registration_date=row["RegistrationDate"],
            status=row["Status"]
        )

    def get_all_customers(self):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()

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

                customers.append(self._build_customer(row))

            return customers

        except Exception as e:

            print(f"Database Error: {e}")
            return []

        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()
    
    def email_exists(self, email):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()
            cursor = connection.cursor()

            cursor.execute(
                "SELECT 1 FROM Customers WHERE Email = %s",
                (email,)
            )

            return cursor.fetchone() is not None

        except Exception as e:

            print(f"Database Error: {e}")
            return False

        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()


    def phone_exists(self, phone):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()
            cursor = connection.cursor()

            cursor.execute(
                "SELECT 1 FROM Customers WHERE PhoneNumber = %s",
                (phone,)
            )

            return cursor.fetchone() is not None

        except Exception as e:

            print(f"Database Error: {e}")
            return False

        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()
            
    def customer_exists(self, customer_id):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()
            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT 1
                FROM Customers
                WHERE CustomerID = %s
                """,
                (customer_id,)
            )

            return cursor.fetchone() is not None

        except Exception as e:

            print(f"Database Error: {e}")
            return False

        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()

    def get_customer_by_id(self, customer_id):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()

            cursor = connection.cursor(dictionary=True)

            query = """
                SELECT
                    CustomerID,
                    FullName,
                    Email,
                    PhoneNumber,
                    City,
                    RegistrationDate,
                    Status
                FROM Customers
                WHERE CustomerID = %s
            """

            cursor.execute(query, (customer_id,))

            row = cursor.fetchone()

            if row:

                return self._build_customer(row)

            return None

        except Exception as e:

            print(f"Database Error: {e}")
            return None

        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()

    def get_customers_by_name(self, name):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()

            cursor = connection.cursor(dictionary=True)

            query = """
                SELECT
                    CustomerID,
                    FullName,
                    Email,
                    PhoneNumber,
                    City,
                    RegistrationDate,
                    Status
                FROM Customers
                WHERE FullName LIKE %s
                ORDER BY FullName
            """

            cursor.execute(query, ("%" + name + "%",))

            rows = cursor.fetchall()

            customers = []

            for row in rows:

                customers.append(self._build_customer(row))

            return customers

        except Exception as e:

            print(f"Database Error: {e}")
            return []

        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()

    def get_customer_by_email(self, email):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()

            cursor = connection.cursor(dictionary=True)

            query = """
                SELECT
                    CustomerID,
                    FullName,
                    Email,
                    PhoneNumber,
                    City,
                    RegistrationDate,
                    Status
                FROM Customers
                WHERE Email = %s
            """

            cursor.execute(query, (email,))

            row = cursor.fetchone()

            if row:

                return self._build_customer(row)

            return None

        except Exception as e:

            print(f"Database Error: {e}")
            return None

        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()

    def get_customer_by_phone(self, phone):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()

            cursor = connection.cursor(dictionary=True)

            query = """
                SELECT
                    CustomerID,
                    FullName,
                    Email,
                    PhoneNumber,
                    City,
                    RegistrationDate,
                    Status
                FROM Customers
                WHERE PhoneNumber = %s
            """

            cursor.execute(query, (phone,))

            row = cursor.fetchone()

            if row:

                return self._build_customer(row)

            return None

        except Exception as e:

            print(f"Database Error: {e}")
            return None

        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()

    def insert_customer(self, customer):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()
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

            return cursor.lastrowid

        except Exception as e:

            print(f"Database Error: {e}")
            return None

        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()              