import unittest
import sentifilm.views
import sqlite3

class Test_RNN(unittest.TestCase):

    # @unittest.skip('skip test')
    def test_rnn(self):
        conn = sqlite3.connect("test_base/test_base1.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM test_base1")
        list = cursor.fetchall()
        # print(len(list))
        k = 0
        for i in list:
            # print(k)
            score = sentifilm.views.analysis()
            score = round(float(score))
            if score == int(i[1]):
                k += 1
        self.assertGreater(round(k / len(list) * 100), 60)

    def test_spase(self):
        self.assertRaises(BaseException, sentifilm.views.work_rnn, " ", loaded_model) #(exs, fun, *args, **kwds) — fun(*args, **kwds) порождает исключение exc

    def test_enter(self):
        self.assertRaises(BaseException, sentifilm.views.work_rnn, "\n", loaded_model)

    @unittest.skip('skip test')
    def test_enter(self):
        self.assertRaises(BaseException, sentifilm.views.work_rnn, "是的，昨天我不在家", loaded_model)

if __name__=="__main__":
    unittest.main()