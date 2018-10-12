import datetime
import tkinter as tk

"""
Motivation:
Planning apps are nice (like Todoist, etc.), but I find that they often do a bad job of laying out my
tasks and prioritizing them. I want to make a planning app that not only lets me keep track of my homework/to-dos,
but also provides the following:
- a clear "forecast" of what's coming up on your next week
    - this will allow you to determine how much time to spend studying vs. having fun on any given day/weekend
    e.g. If I have 2 tests next week, I want my planning app to warn me that I should start studying this week/weekend
- categorization that prioritizes based on the following criteria
    - what is the event/to-do item? (test, quiz, homework, social gathering, etc.)
    - how difficult is the class for you? (if the item is related to a class)
- allotment of time:
    - given your schedule, can tell you how much of your free time should be spent working vs. having fun
        - N.B. I think it's important that you don't spend every waking moment studying. There should be some
               percentage of your time that is allowed to be allotted for relaxation/social time that is dynamically
               determined based on your upcoming tasks
"""

# TODO: We'll probably want to modify values here later
priorities = {
    'test': 5,
    'quiz': 4,
    'homework': 3,
    'social': 2,
}

# TODO: Will be input/modified by user
classes = {
    'CPSC320': 5,
    'CPSC313': 4,
    'CPSC322': 3,
    'MATH200': 4,
    'CHEM100': 2
}

# List containing task objects
tasks = list()

# List containing times we're always busy
always_busy = list()


def get_priority(task_type, course=None):
    """
    :param task_type: String
    :param course: String
    :return: Score representing priority of task
    """
    if course is None:
        return priorities[task_type]
    else:
        return priorities[task_type] + classes[course]


def within_seven(task):
    date = datetime.datetime.now()
    date = datetime.date(day=date.day, month=date.month, year=date.year)
    margin = datetime.timedelta(days=7)

    if task.due_date <= date + margin:
        return True

    return False


def get_next_seven_days(priority_threshold=None):
    next_seven_days = list()

    if priority_threshold is None:
        for task in tasks:
            if within_seven(task.due_date):
                next_seven_days.append(task)
    else:
        for task in tasks:
            if task.priority >= priority_threshold:
                if within_seven(task):
                    next_seven_days.append(task)
    return next_seven_days


def determine_free_time():
    """
    Determines the times user has available to do tasks outside of
    regularly scheduled events (i.e. weekly classes, meetings)
    """
    pass


def add_always_busy_time():
    """
    Adds a time when we're always busy (due to a class/meeting)
    to our always_busy list
    """
    pass


def remove_always_busy_time():
    """
    Removes a time when we're always busy (due to a class/meeting)
    to our always_busy list
    """
    pass





