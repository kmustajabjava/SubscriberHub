from repositories.customer_repository import CustomerRepository
from repositories.ticket_repository import SupportTicketRepository


class SupportTicketService:

    def __init__(self):

        self.customer_repository = CustomerRepository()

        self.ticket_repository = SupportTicketRepository()

    def create_ticket(self, ticket):

        if not self.customer_repository.customer_exists(
            ticket.customer_id
        ):

            return False, "Customer not found."

        success = self.ticket_repository.insert_ticket(ticket)

        if success:

            return True, "Support ticket created successfully."

        return False, "Unable to create support ticket."

    def get_all_tickets(self):

        return self.ticket_repository.get_all_tickets()
    
    def get_ticket_by_id(self, ticket_id):

        return self.ticket_repository.get_ticket_by_id(ticket_id)
    
    def update_ticket_status(self, ticket_id, status):

        return self.ticket_repository.update_ticket_status(
            ticket_id,
            status
        )
    
    def close_ticket(self, ticket_id):

        return self.ticket_repository.close_ticket(ticket_id)
    
    def get_customer_ticket_history(self, customer_id):

        return self.ticket_repository.get_customer_ticket_history(
            customer_id
        )