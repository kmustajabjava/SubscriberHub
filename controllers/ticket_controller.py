from datetime import date

from models.ticket import SupportTicket
from services.ticket_service import SupportTicketService


class SupportTicketController:

    def __init__(self):

        self.service = SupportTicketService()

    def ticket_menu(self):

        while True:

            print("\n===== SUPPORT TICKETS =====")

            print("1. Create Ticket")
            print("2. View All Tickets")
            print("3. Search Ticket")
            print("4. Update Status")
            print("5. Close Ticket")
            print("6. Customer Ticket History")
            print("0. Back")

            choice = input("\nSelect Option: ")

            if choice == "1":

                self.create_ticket()

            elif choice == "2":

                self.display_tickets()

            elif choice == "3":

                self.search_ticket()

            elif choice == "4":

                self.update_ticket_status()

            elif choice == "5":

                self.close_ticket()

            elif choice == "6":

                self.customer_ticket_history()

            elif choice == "0":

                break

            else:

                print("\nInvalid option.")

    def create_ticket(self):

        print("\n===== CREATE SUPPORT TICKET =====\n")

        customer_id = int(input("Customer ID: "))

        print("\nIssue Types")
        print("1. Billing")
        print("2. Technical")
        print("3. Network")
        print("4. General")

        issue_options = {
            "1": "Billing",
            "2": "Technical",
            "3": "Network",
            "4": "General"
        }

        choice = input("\nSelect Issue Type: ")

        issue_type = issue_options.get(choice)

        if issue_type is None:

            print("Invalid issue type.")
            return

        description = input("Description: ")

        print("\nPriority")
        print("1. Low")
        print("2. Medium")
        print("3. High")

        priority_options = {
            "1": "Low",
            "2": "Medium",
            "3": "High"
        }

        priority = priority_options.get(
            input("\nSelect Priority: ")
        )

        if priority is None:

            print("Invalid priority.")
            return

        ticket = SupportTicket(
            customer_id=customer_id,
            issue_type=issue_type,
            description=description,
            priority=priority,
            created_date=date.today()
        )

        success, message = self.service.create_ticket(ticket)

        print(f"\n{message}")


    def print_ticket(self, ticket):

        print(f"\nTicket ID     : {ticket['TicketID']}")
        print(f"Customer      : {ticket['FullName']}")
        print(f"Issue Type    : {ticket['IssueType']}")
        print(f"Description   : {ticket['Description']}")
        print(f"Priority      : {ticket['Priority']}")
        print(f"Status        : {ticket['Status']}")
        print(f"Created Date  : {ticket['CreatedDate']}")


    def display_tickets(self):

        tickets = self.service.get_all_tickets()

        print("\n========== SUPPORT TICKETS ==========\n")

        if not tickets:

            print("No tickets found.")
            return

        for ticket in tickets:

            self.print_ticket(ticket)

            print("-" * 50)

    def search_ticket(self):

        print("\n===== SEARCH SUPPORT TICKET =====\n")

        ticket_id = int(input("Enter Ticket ID: "))

        ticket = self.service.get_ticket_by_id(ticket_id)

        if ticket:

            self.print_ticket(ticket)

        else:

            print("\nTicket not found.")


    def update_ticket_status(self):

        print("\n===== UPDATE TICKET STATUS =====\n")

        ticket_id = int(input("Enter Ticket ID: "))

        ticket = self.service.get_ticket_by_id(ticket_id)

        if not ticket:

            print("\nTicket not found.")
            return

        self.print_ticket(ticket)

        transitions = {
            "Open": "In Progress",
            "In Progress": "Resolved",
            "Resolved": "Closed"
        }

        current_status = ticket["Status"]

        if current_status == "Closed":

            print("\nTicket is already closed.")
            return

        new_status = transitions[current_status]

        confirm = input(
            f"\nChange status to '{new_status}'? (Y/N): "
        ).strip().upper()

        if confirm != "Y":

            print("\nOperation cancelled.")
            return

        success = self.service.update_ticket_status(
            ticket_id,
            new_status
        )

        if success:

            print("\nTicket status updated successfully.")

        else:

            print("\nUnable to update ticket.")


    def close_ticket(self):

        print("\n===== CLOSE SUPPORT TICKET =====\n")

        ticket_id = int(input("Enter Ticket ID: "))

        ticket = self.service.get_ticket_by_id(ticket_id)

        if not ticket:

            print("\nTicket not found.")
            return

        self.print_ticket(ticket)

        if ticket["Status"] == "Closed":

            print("\nTicket is already closed.")
            return

        confirm = input("\nClose this ticket? (Y/N): ").strip().upper()

        if confirm != "Y":

            print("\nOperation cancelled.")
            return

        success = self.service.close_ticket(ticket_id)

        if success:

            print("\nTicket closed successfully.")

        else:

            print("\nUnable to close ticket.")


    def customer_ticket_history(self):

        print("\n===== CUSTOMER TICKET HISTORY =====\n")

        customer_id = int(input("Enter Customer ID: "))

        tickets = self.service.get_customer_ticket_history(customer_id)

        if not tickets:

            print("\nNo ticket history found.")
            return

        print(f"\nCustomer ID: {customer_id}\n")

        for ticket in tickets:

            print(f"Ticket ID     : {ticket['TicketID']}")
            print(f"Issue Type    : {ticket['IssueType']}")
            print(f"Description   : {ticket['Description']}")
            print(f"Priority      : {ticket['Priority']}")
            print(f"Status        : {ticket['Status']}")
            print(f"Created Date  : {ticket['CreatedDate']}")
            print("-" * 50)