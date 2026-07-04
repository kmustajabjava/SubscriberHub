from datetime import date

from models.customer import Customer
from services.customer_service import CustomerService


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