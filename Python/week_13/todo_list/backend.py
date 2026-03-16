class Task:

    def __init__(self, message):
        self._message = message

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, new_message):
        if len(new_message) > 0:
            self._message = new_message


class TaskList:

    def __init__(self):
        self.tasks = []

    def create_new_task(self, message):
        new_task = Task(message)
        self.tasks.append(new_task)

    def get_task_message_by_index(self, index):
        task = self.tasks[index]
        return task.message

    def remove_task_at_index(self, index):
        del self.tasks[index]

    def get_num_tasks(self):
        return len(self.tasks)

    def set_task_message_at_index(self, index, message):
        task = self.tasks[index]
        task.message = message