from config.database import get_connection
from models.plan import Plan


class PlanRepository:

    def get_all_plans(self):

        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT
                PlanID,
                PlanName,
                SpeedMbps,
                Price
            FROM Plans
            ORDER BY Price
        """)

        rows = cursor.fetchall()

        plans = []

        for row in rows:

            plans.append(
                Plan(
                    plan_id=row["PlanID"],
                    plan_name=row["PlanName"],
                    speed=row["SpeedMbps"],
                    price=row["Price"]
                )
            )

        cursor.close()
        connection.close()

        return plans
    
    def get_plan_by_id(self, plan_id):

        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT *
            FROM Plans
            WHERE PlanID=%s
            """,
            (plan_id,)
        )

        row = cursor.fetchone()

        cursor.close()
        connection.close()

        if row:

            return Plan(
                plan_id=row["PlanID"],
                plan_name=row["PlanName"],
                speed=row["SpeedMbps"],
                price=row["Price"]
            )

        return None