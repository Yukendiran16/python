import unittest
from datetime import datetime
from unittest.mock import Mock


class api:

    json = {'name': 'yuki', 'age': 21, 'role': 'dev'}

    @staticmethod
    def post():
        api.json['method'] = 'post'
        api.json['time_stamp'] = datetime.now().date()
        return api.json

    @staticmethod
    def get():
        return api.post()


def mock_post():
    api.post = Mock()
    api.post.return_value = {'name': 'yuki', 'age': 22, 'role': 'dev',
                             'method': 'post', 'time_stamp': datetime.now().date()}
    return api.get()


class Test(unittest.TestCase):

    def setUp(self):
        super(Test, self).setUp()
        self.mock_data = {'name': 'yuki', 'age': 21, 'role': 'dev',
                          'method': 'post', 'time_stamp': datetime.now().date()}
        print("hii")

    @unittest.skipUnless({'name': 'yuki', 'age': 21, 'role': 'dev',
                          'method': 'post', 'time_stamp': datetime.now().date()} is None, reason="nothing")
    def test_1(self):
        self.assertEqual(self.mock_data, {'name': 'yuki', 'age': 21, 'role': 'dev',
                                          'method': 'post', 'time_stamp': datetime.now().date()})

    @unittest.skip
    def test_2(self):
        self.assertEqual(mock_post(),
                         {'name': 'yuki', 'age': 22, 'role': 'dev', 'method': 'post',
                          'time_stamp': datetime.now().date()})

    @unittest.skipIf(api.get() is not None, reason="nothing")
    def test_3(self):
        api.post = Mock()
        api.post.return_value = {'name': 'yuki', 'age': 20, 'role': 'dev',
                                 'method': 'post', 'time_stamp': datetime.now().date()}
        self.assertEqual(api.get(),
                         {'name': 'yuki', 'age': 20, 'role': 'dev', 'method': 'post',
                          'time_stamp': datetime.now().date()})

    def test_4(self):
        pass
    
    def tearDown(self):
        super(Test, self).tearDown()
        print(self.mock_data)
        self.mock_data = {}
        print(self.mock_data)


if __name__ == '__main__':
    unittest.main()
