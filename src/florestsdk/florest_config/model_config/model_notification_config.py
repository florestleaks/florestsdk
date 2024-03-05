from pydantic import BaseModel


class NotificationSender(BaseModel):
    email_setup_manager: list
    email_monitoring: list
