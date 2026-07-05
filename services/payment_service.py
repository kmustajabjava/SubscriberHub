from repositories.payment_repository import PaymentRepository


class PaymentService:

    def __init__(self):

        self.payment_repository = PaymentRepository()

    def get_all_payments(self):

        return self.payment_repository.get_all_payments()
    
    def get_payment_by_id(self, payment_id):

        return self.payment_repository.get_payment_by_id(payment_id)
    
    def complete_payment(self, payment_id):

        return self.payment_repository.complete_payment(payment_id)
    
    def fail_payment(self, payment_id):

        return self.payment_repository.fail_payment(payment_id)
    
    def refund_payment(self, payment_id):

        return self.payment_repository.refund_payment(payment_id)
    
    def get_customer_payment_history(self, customer_id):

        return self.payment_repository.get_customer_payment_history(
            customer_id
        )