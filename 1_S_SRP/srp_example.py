class TaskHandler:
    def create_task(self, description: str) -> None:
        if self.__verify_input_data(description):
            print("Creating a new task")

    def __verify_input_data(self, description: str) -> bool:
        return isinstance(description, str)

    def update_task(self, description: str) -> Dict:
        if self.__verify_input_data(description):
            print("Updating the task")

    def check_task(self, task_id: str):
        print("Checking the task")

    def remove_task(self, task_id: str):
        print("Removing the task")


class APIHandler:
    def connect_api(self):
        print("Connecting to API")


class Notificator:
    def send_notification(self, message: str):
        print("Sending a notification")


class ReportHandler:
    def generate_report(self):
        print("Generating report")

    def send_report(self):
        print("Sending report")
