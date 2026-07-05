from datetime import date

from models.customer import Customer
from services.customer_service import CustomerService
from utils.validator import is_valid_email, is_valid_phone


class CustomerController:

    def __init__(self):

        self.service = CustomerService()

    def display_customers(self):

        customers = self.service.get_all_customers()

        print("\n===== CUSTOMER LIST =====\n")

        for customer in customers:

            print(customer)

    def register_customer(self):

        print("\n===== REGISTER CUSTOMER =====\n")

        full_name = input("Full Name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        city = input("City: ")
        status = input("Status (Active/Inactive/Suspended): ")

        customer = Customer(
            full_name=full_name,
            email=email,
            phone_number=phone,
            city=city,
            registration_date=date.today(),
            status=status
        )

        success, message = self.service.register_customer(customer)

        print(f"\n{message}")

    def search_customer_by_id(self):

        print("\n===== SEARCH CUSTOMER =====\n")

        customer_id = int(input("Enter Customer ID: "))

        customer = self.service.get_customer_by_id(customer_id)

        if customer:

            print("\nCustomer Found:\n")
            print(customer)

        else:

            print("\nCustomer not found.")

    def search_customer_by_name(self):

        print("\n===== SEARCH CUSTOMER BY NAME =====\n")

        name = input("Enter Name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return

        customers = self.service.get_customers_by_name(name)

        if customers:

            print("\nCustomers Found:\n")

            for customer in customers:

                print(customer)

        else:

            print("\nNo customers found.")

    def search_customer_by_email(self):

        print("\n===== SEARCH CUSTOMER BY EMAIL =====\n")

        email = input("Enter Email: ").strip()
        if not is_valid_email(email):

            print("Invalid email format.")
            return
        if not email:

            print("Email cannot be empty.")
            return

        customer = self.service.get_customer_by_email(email)

        if customer:

            print("\nCustomer Found:\n")
            print(customer)

        else:

            print("\nCustomer not found.")

    def search_customer_by_phone(self):

        print("\n===== SEARCH CUSTOMER BY PHONE =====\n")

        phone = input("Enter Phone Number: ").strip()
        if not is_valid_phone(phone):

            print("Invalid phone number.")
            return
        if not phone:

            print("Phone number cannot be empty.")
            return

        customer = self.service.get_customer_by_phone(phone)

        if customer:

            print("\nCustomer Found:\n")
            print(customer)

        else:

            print("\nCustomer not found.")

    def search_customer(self):

        while True:

            print("\n===== CUSTOMER SEARCH =====")

            print("1. Search by ID")
            print("2. Search by Name")
            print("3. Search by Email")
            print("4. Search by Phone")
            print("0. Back")

            choice = input("\nSelect Option: ")

            if choice == "1":

                self.search_customer_by_id()

            elif choice == "2":

                self.search_customer_by_name()

            elif choice == "3":

                self.search_customer_by_email()

            elif choice == "4":

                self.search_customer_by_phone()

            elif choice == "0":

                break

            else:

                print("Invalid option.")