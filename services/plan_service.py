from repositories.plan_repository import PlanRepository


class PlanService:

    def __init__(self):

        self.repository = PlanRepository()

    def get_all_plans(self):

        return self.repository.get_all_plans()

    def get_plan(self, plan_id):

        return self.repository.get_plan_by_id(plan_id)