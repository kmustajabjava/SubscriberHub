from services.customer_service import CustomerService


class CustomerController:

    def __init__(self):

        self.service = CustomerService()

    def display_customers(self):

        customers = self.service.get_all_customers()

        print("\n===== CUSTOMER LIST =====\n")

        for customer in customers:

            print(customer)