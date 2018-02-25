import unittest
import json
from urllib2 import Request, urlopen

class TestHelloServer(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://localhost:5000/hello"
        self.first_name = "amir"
        self.last_name = "mukeri"
        self.msg = "Hello World"
    def test_hello(self):
        test_url = self.base_url + '/amir/mukeri'
        req = Request(test_url)
        res = urlopen(req)
        self.assertEqual(res.code, 200)
        json_data = json.load(res)
        assert json_data['first_name'] == self.first_name
        assert json_data['last_name'] == self.last_name
        assert json_data['msg'] == self.msg
        
if __name__ == "__main__":
    unittest.main()
        
    