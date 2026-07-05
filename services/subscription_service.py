from datetime import date, timedelta

from models.subscription import Subscription
from models.payment import Payment

from repositories.customer_repository import CustomerRepository
from repositories.plan_repository import PlanRepository
from repositories.subscription_repository import SubscriptionRepository
from repositories.payment_repository import PaymentRepository
from services.audit_service import AuditService


class SubscriptionService:

    def __init__(self):

        self.customer_repository = CustomerRepository()

        self.plan_repository = PlanRepository()

        self.subscription_repository = SubscriptionRepository()

        self.payment_repository = PaymentRepository()

        self.audit_service = AuditService()

    def create_subscription(
        self,
        customer_id,
        plan_id,
        payment_method,
        auto_renew=False
    ):

        # Check if customer exists
        if not self.customer_repository.customer_exists(customer_id):

            return False, "Customer not found."

        # Check if plan exists
        plan = self.plan_repository.get_plan_by_id(plan_id)

        if plan is None:

            return False, "Plan not found."

        # Expire any previous active subscriptions
        self.subscription_repository.expire_active_subscriptions(customer_id)

        # Subscription dates
        start_date = date.today()
        end_date = start_date + timedelta(days=30)

        # Create subscription object
        subscription = Subscription(
            customer_id=customer_id,
            plan_id=plan_id,
            start_date=start_date,
            end_date=end_date,
            auto_renew=auto_renew
        )

        # Save subscription
        subscription_id = self.subscription_repository.insert_subscription(
            subscription
        )

        subscription.subscription_id = subscription_id
        # Create payment object
        payment = Payment(
            subscription_id=subscription_id,
            amount=plan.price,
            payment_method=payment_method,
            payment_date=start_date
        )

        # Save payment
        payment_id = self.payment_repository.insert_payment(payment)

        if payment_id:

            self.audit_service.log_action(
                customer_id,
                "Subscription created."
            )

            return True, "Subscription created successfully."

        return False, "Subscription creation failed."
    
    def get_all_subscriptions(self):

        return self.subscription_repository.get_all_subscriptions()
    
    def get_subscription_by_id(self, subscription_id):

        return self.subscription_repository.get_subscription_by_id(
            subscription_id
        )
    
    def pause_subscription(self, subscription_id):

        sub = self.subscription_repository.get_subscription_by_id(
            subscription_id
        )

        if not sub:

            return False

        success = self.subscription_repository.pause_subscription(
            subscription_id
        )

        if success:

            self.audit_service.log_action(
                sub["CustomerID"],
                "Subscription paused."
            )

        return success
    
    def resume_subscription(self, subscription_id):

        sub = self.subscription_repository.get_subscription_by_id(subscription_id)

        success = self.subscription_repository.resume_subscription(subscription_id)

        if success:

            self.audit_service.log_action(
                sub["CustomerID"],
                "Subscription resumed."
            )

        return success
    
    def cancel_subscription(self, subscription_id):

        sub = self.subscription_repository.get_subscription_by_id(subscription_id)

        success = self.subscription_repository.cancel_subscription(subscription_id)

        if success:

            self.audit_service.log_action(
                sub["CustomerID"],
                "Subscription cancelled."
            )

        return success