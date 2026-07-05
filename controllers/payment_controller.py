from services.payment_service import PaymentService


class PaymentController:

    def __init__(self):

        self.service = PaymentService()

    def payment_menu(self):

        while True:

            print("\n===== PAYMENT MANAGEMENT =====")

            print("1. View All Payments")
            print("2. Search Payment")
            print("3. Complete Payment")
            print("4. Mark Payment Failed")
            print("5. Refund Payment")
            print("6. Customer Payment History")
            print("0. Back")

            choice = input("\nSelect Option: ")

            if choice == "1":

                self.display_payments()

            elif choice == "2":

                self.search_payment()

            elif choice == "3":

                self.complete_payment()

            elif choice == "4":

                self.fail_payment()

            elif choice == "5":

                self.refund_payment()

            elif choice == "6":

                self.customer_payment_history()

            elif choice == "0":

                break

            else:

                print("\nInvalid option.")



    def print_payment(self, payment):

        print(f"\nPayment ID      : {payment['PaymentID']}")
        print(f"Customer        : {payment['FullName']}")
        print(f"Plan            : {payment['PlanName']}")
        print(f"Amount          : Rs. {payment['Amount']}")
        print(f"Payment Method  : {payment['PaymentMethod']}")
        print(f"Payment Date    : {payment['PaymentDate']}")
        print(f"Status          : {payment['Status']}")


    def display_payments(self):

        payments = self.service.get_all_payments()

        print("\n========== PAYMENTS ==========\n")

        if not payments:

            print("No payments found.")
            return

        for payment in payments:

            self.print_payment(payment)
            print("-" * 50)

        
    def search_payment(self):

        print("\n===== SEARCH PAYMENT =====\n")

        payment_id = int(input("Enter Payment ID: "))

        payment = self.service.get_payment_by_id(payment_id)

        if payment:

            self.print_payment(payment)

        else:

            print("\nPayment not found.")


    def complete_payment(self):

        print("\n===== COMPLETE PAYMENT =====\n")

        payment_id = int(input("Enter Payment ID: "))

        payment = self.service.get_payment_by_id(payment_id)

        if not payment:

            print("\nPayment not found.")
            return

        self.print_payment(payment)

        if payment["Status"] != "Pending":

            print("\nOnly Pending payments can be completed.")
            return

        confirm = input("\nComplete this payment? (Y/N): ").strip().upper()

        if confirm != "Y":

            print("\nOperation cancelled.")
            return

        success = self.service.complete_payment(payment_id)

        if success:

            print("\nPayment completed successfully.")

        else:

            print("\nUnable to complete payment.")


    def fail_payment(self):

        print("\n===== MARK PAYMENT FAILED =====\n")

        payment_id = int(input("Enter Payment ID: "))

        payment = self.service.get_payment_by_id(payment_id)

        if not payment:

            print("\nPayment not found.")
            return

        self.print_payment(payment)

        if payment["Status"] != "Pending":

            print("\nOnly Pending payments can be marked as Failed.")
            return

        confirm = input("\nMark this payment as Failed? (Y/N): ").strip().upper()

        if confirm != "Y":

            print("\nOperation cancelled.")
            return

        success = self.service.fail_payment(payment_id)

        if success:

            print("\nPayment marked as Failed successfully.")

        else:

            print("\nUnable to update payment.")

        
    def refund_payment(self):

        print("\n===== REFUND PAYMENT =====\n")

        payment_id = int(input("Enter Payment ID: "))

        payment = self.service.get_payment_by_id(payment_id)

        if not payment:

            print("\nPayment not found.")
            return

        self.print_payment(payment)

        if payment["Status"] != "Completed":

            print("\nOnly Completed payments can be refunded.")
            return

        confirm = input("\nRefund this payment? (Y/N): ").strip().upper()

        if confirm != "Y":

            print("\nOperation cancelled.")
            return

        success = self.service.refund_payment(payment_id)

        if success:

            print("\nPayment refunded successfully.")

        else:

            print("\nUnable to refund payment.")

    def customer_payment_history(self):

        print("\n===== CUSTOMER PAYMENT HISTORY =====\n")

        customer_id = int(input("Enter Customer ID: "))

        payments = self.service.get_customer_payment_history(customer_id)

        if not payments:

            print("\nNo payment history found.")
            return

        print(f"\nCustomer ID: {customer_id}\n")

        for payment in payments:

            print(f"Payment ID      : {payment['PaymentID']}")
            print(f"Plan            : {payment['PlanName']}")
            print(f"Amount          : Rs. {payment['Amount']}")
            print(f"Payment Method  : {payment['PaymentMethod']}")
            print(f"Payment Date    : {payment['PaymentDate']}")
            print(f"Status          : {payment['Status']}")
            print("-" * 50)