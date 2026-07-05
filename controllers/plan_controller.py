from services.plan_service import PlanService


class PlanController:

    def __init__(self):

        self.service = PlanService()

    def display_plans(self):

        plans = self.service.get_all_plans()

        print("\n===== AVAILABLE PLANS =====\n")

        for plan in plans:

            print(plan)