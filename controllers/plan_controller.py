from services.plan_service import PlanService


class PlanController:

    def __init__(self):

        self.service = PlanService()

    def plan_menu(self):

        while True:

            print("\n===== PLAN MANAGEMENT =====")
            print("1. Display Plans")
            print("0. Back")

            choice = input("\nSelect Option: ")

            if choice == "1":

                self.display_plans()

            elif choice == "0":

                break

            else:

                print("Invalid option.")

    def display_plans(self):

        plans = self.service.get_all_plans()

        print("\n===== AVAILABLE PLANS =====\n")

        for plan in plans:

            print(plan)