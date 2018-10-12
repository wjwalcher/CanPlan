import canplan


class Task:

    name = None
    task_type = None
    priority = None
    due_date = None
    course = None

    def __init__(self, name, task_type, course=None, due_date=None):
        """

        :param name: String
        :param task_type: String
        :param course: String
        :param due_date: TODO
        """
        self.name = name
        self.task_type = task_type
        self.course = course
        self.priority = canplan.get_priority(task_type, course)
        self.due_date = due_date

    def edit_name(self, name):
        self.name = name

    def edit_task_type(self, task_type):
        self.task_type = task_type

    def edit_course(self, course):
        self.priority = canplan.get_priority(self.task_type, course)
        self.course = course

    def edit_due_date(self, due_date):
        self.due_date = due_date

