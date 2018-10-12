import unittest
import canplan as cp
import task
import datetime


class Tests(unittest.TestCase):

    def test_priority(self):
        self.assertEqual(cp.get_priority("test", "CPSC320"), 10)

    def test_task_constructor(self):
        T = task.Task("320 Midterm 2", "test", "CPSC320")
        self.assertEqual(T.name, "320 Midterm 2")
        self.assertEqual(T.task_type, "test")
        self.assertEqual(T.priority, 10)

    def test_within_seven(self):
        now = datetime.datetime.now()
        T = task.Task("320 Midterm 2", "test", "CPSC320", due_date=datetime.date(day=now.day+3, month=now.month, year=now.year))
        self.assertTrue(cp.within_seven(T))
