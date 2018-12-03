import unittest
import pytest.save_network
import sqlite3

class Test_RNN(unittest.TestCase):
    # def setUp(self):
    #     loaded_model = save_network.loading_rnn()

    def test_rnn(self):
        loaded_model = pytest.save_network.loading_rnn()
        conn = sqlite3.connect("pytest/base/test_base1.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM test_base1")
        list = cursor.fetchall()
        print(len(list))
        k = 0
        for i in list:
            print(k)
            score = pytest.save_network.work_rnn(i[0], loaded_model)
            score = round(float(score))
            if score == int(i[1]):
                k += 1
        self.assertGreater(round(k / len(list) * 100), 60)

if __name__=="__main__":
    unittest.main()