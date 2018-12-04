import unittest
import views
import sqlite3

class Test_RNN(unittest.TestCase):

    # @unittest.skip('skip test')
    def test_rnn_base11(self):
        conn = sqlite3.connect("../test_base/test_base11.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM test_base11")
        list = cursor.fetchall()
        k = 0
        for i in list:
            score = views.text(i[0])
            # score = views.text(i[1]) # fot test_base1
            score = round(float(score))
            if score == int(i[1]):
            # if score == int(i[2]): # fot test_base1
                k += 1
        self.assertGreater(round(k / len(list) * 100), 60)

    def test_rnn_base(self):
        conn = sqlite3.connect("../test_base/test_base.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM test_base")
        list = cursor.fetchall()[0:700:2]
        k = 0
        for i in list:
            # score = views.text(i[0])
            score = views.text(i[1]) # fot test_base1
            score = round(float(score))
            # if score == int(i[1]):
            if score == int(i[2]): # fot test_base1
                k += 1
        self.assertGreater(round(k / len(list) * 100), 60)

    # def test_spase(self):
    #     self.assertRaises(BaseException, views.text, "") #(exs, fun, *args, **kwds) — fun(*args, **kwds) порождает исключение exc

    # def test_enter(self):
    #     self.assertRaises(BaseException, sentifilm.views.work_rnn, "\n", loaded_model)
    #
    # @unittest.skip('skip test')
    # def test_enter(self):
    #     self.assertRaises(BaseException, sentifilm.views.work_rnn, "是的，昨天我不在家", loaded_model)

# if __name__=="__main__":
#     unittest.main()