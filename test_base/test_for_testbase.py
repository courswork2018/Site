import unittest
import sqlite3

class Test_RNN(unittest.TestCase):

    def test_base11(self):
        conn = sqlite3.connect("../test_base/test_base11.db")
        cursor = conn.cursor()
        cursor.execute("SELECT feedback FROM test_base11")
        list = cursor.fetchall()
        k = 0
        for i in list:
            sovpadeniya = cursor.execute("SELECT feedback FROM test_base11 WHERE feedback = (?)", i).fetchall()
            if len(sovpadeniya) != 1:
                k += 1
        self.assertGreater(k, 0)

    def test_base(self):
        conn = sqlite3.connect("../test_base/test_base.db")
        cursor = conn.cursor()
        cursor.execute("SELECT feedback FROM test_base")
        list = cursor.fetchall()
        k = 0
        for i in list:
            sovpadeniya = cursor.execute("SELECT feedback FROM test_base WHERE feedback = (?)", i).fetchall()
            if len(sovpadeniya) != 1:
                k += 1
        self.assertGreater(k, 0)