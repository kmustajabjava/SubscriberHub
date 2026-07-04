from repositories.customer_repository import CustomerRepository
from utils.validator import (
    is_valid_email,
    is_valid_phone,
    is_valid_status
)
class CustomerService:

    def __init__(self):

        self.repository = CustomerRepository()

    def get_all_customers(self):

        return self.repository.get_all_customers()
    
    def register_customer(self, customer):

        if not is_valid_email(customer.email):
            return False, "Invalid email format."

        if not is_valid_phone(customer.phone_number):
            return False, "Invalid phone number."

        if not is_valid_status(customer.status):
            return False, "Invalid customer status."

        if self.repository.email_exists(customer.email):
            return False, "Email already exists."

        if self.repository.phone_exists(customer.phone_number):
            return False, "Phone number already exists."

        self.repository.insert_customer(customer)

        return True, "Customer registered successfully."