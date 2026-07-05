from repositories.audit_log_repository import AuditRepository


class AuditService:

    def __init__(self):

        self.repository = AuditRepository()

    def log_action(self, customer_id, action):

        return self.repository.log_action(
            customer_id,
            action
        )