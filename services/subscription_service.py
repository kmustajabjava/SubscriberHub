from datetime import date, timedelta

from models.subscription import Subscription
from models.payment import Payment

from repositories.customer_repository import CustomerRepository
from repositories.plan_repository import PlanRepository
from repositories.subscription_repository import SubscriptionRepository
from repositories.payment_repository import PaymentRepository


class SubscriptionService:

    def __init__(self):

        self.customer_repository = CustomerRepository()

        self.plan_repository = PlanRepository()

        self.subscription_repository = SubscriptionRepository()

        self.payment_repository = PaymentRepository()

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

        # Create payment object
        payment = Payment(
            subscription_id=subscription_id,
            amount=plan.price,
            payment_method=payment_method,
            payment_date=start_date
        )

        # Save payment
        self.payment_repository.insert_payment(payment)

        return True, "Subscription created successfully."