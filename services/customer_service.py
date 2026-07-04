from repositories.customer_repository import CustomerRepository


class CustomerService:

    def __init__(self):

        self.repository = CustomerRepository()

    def get_all_customers(self):

        return self.repository.get_all_customers()