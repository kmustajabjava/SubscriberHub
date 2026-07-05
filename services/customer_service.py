from repositories.customer_repository import CustomerRepository
from services.audit_service import AuditService
from utils.validator import (
    is_valid_email,
    is_valid_phone,
    is_valid_status
)
class CustomerService:

    def __init__(self):

        self.repository = CustomerRepository()
        self.audit_service = AuditService()
        

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

        customer_id = self.repository.insert_customer(customer)

        if customer_id:

            customer.customer_id = customer_id

            self.audit_service.log_action(
                customer.customer_id,
                "Customer registered."
            )

            return True, "Customer registered successfully."

        return False, "Customer registration failed."
    
    def get_customer_by_id(self, customer_id):

        return self.repository.get_customer_by_id(customer_id)
    
    def get_customers_by_name(self, name):

        return self.repository.get_customers_by_name(name)
    
    def get_customer_by_email(self, email):

        return self.repository.get_customer_by_email(email)

    def get_customer_by_phone(self, phone):

        return self.repository.get_customer_by_phone(phone)