import unittest
import canplan as cp
import task
import datetime


class Tests(unittest.TestCase):

    def setUp(self):
        self.now = datetime.datetime.now()
        self.T = task.Task("320 Midterm 2", "test", "CPSC320", due_date=datetime.date(day=self.now.day+3, month=self.now.month, year=self.now.year))

    def test_priority(self):
        self.assertEqual(cp.get_priority("test", "CPSC320"), 10)

    def test_task_constructor(self):
        self.assertEqual(self.T.name, "320 Midterm 2")
        self.assertEqual(self.T.task_type, "test")
        self.assertEqual(self.T.priority, 10)

    def test_within_seven(self):
        self.assertTrue(cp.within_seven(self.T))

    def test_edit_name(self):
        self.T.edit_name("New task name")
        self.assertEqual(self.T.name, "New task name")

    def test_edit_task_type(self):
        self.T.edit_task_type("homework")
        self.assertEqual(self.T.task_type, "homework")

    def test_edit_course(self):
        self.T.edit_course("CPSC322")
        self.assertEqual(self.T.course, "CPSC322")
        self.assertEqual(self.T.priority, 8)

    def test_edit_due_date(self):
        self.T.edit_due_date(datetime.date(year=self.now.year, month=self.now.month, day=self.now.day+3))
        self.assertEqual(self.T.due_date, datetime.date(year=self.now.year, month=self.now.month, day=self.now.day+3))