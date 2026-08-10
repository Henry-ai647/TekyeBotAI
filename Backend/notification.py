notifications = []


def create_notification(
    message: str,
    notification_type: str = "order"
):
    notification = {
        "id": len(notifications) + 1,
        "type": notification_type,
        "message": message,
        "read": False
    }

    notifications.append(notification)

    return notification


def get_notifications():
    return notifications


def mark_notification_read(notification_id: int):

    for notification in notifications:

        if notification["id"] == notification_id:

            notification["read"] = True

            return {
                "success": True,
                "notification": notification
            }

    return {
        "success": False,
        "message": "Notification not found."
    }
