import unittest
from views import text
import sqlite3
import time

class Test_RNN(unittest.TestCase):

    def test_rnn_base11(self):
        conn = sqlite3.connect("../test_base/test_base11.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM test_base11")
        list = cursor.fetchall()
        k = 0
        global time11
        time11 = 0
        for i in list:
            # print(i[0])
            start_time = time.time()
            score = text(i[0])
            time11 = time11 + (time.time() - start_time)
            score = round(float(score))
            if score == int(i[1]):
                k += 1
        time11 = time11 / len(list)
        self.assertGreaterEqual(round(k / len(list) * 100), 60)

    def test_rnn_base(self):
        conn = sqlite3.connect("../test_base/test_base.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM test_base")
        list = cursor.fetchall()[0:700:2]
        k = 0
        global time_
        time_ = 0
        for i in list:
            start_time = time.time()
            score = text(i[1])
            time_ = time_ + (time.time() - start_time)
            score = round(float(score))
            if score == int(i[2]):
                k += 1
        time_ = time_ / len(list)
        self.assertGreaterEqual(round(k / len(list) * 100), 60)

    def test_time(self):
        # print(time.time())
        res_time = (time11 + time_) / 2
        self.assertLess(res_time, 0.6)


    # def test_spase(self):
    #     self.assertRaises(BaseException, views.text, "") #(exs, fun, *args, **kwds) — fun(*args, **kwds) порождает исключение exc

    # def test_enter(self):
    #     self.assertRaises(BaseException, sentifilm.views.work_rnn, "\n", loaded_model)
    #
    # @unittest.skip('skip test')
    # def test_enter(self):
    #     self.assertRaises(BaseException, sentifilm.views.work_rnn, "是的，昨天我不在家", loaded_model)
