import unittest
import requests
import json

class TestLogin(unittest.TestCase):
    # def setUp(self):
    #     print("Test cast started")

    # def tearDown(self):
    #     print("Test case closed")

    def test_post_with_json(self):
        url = "http://127.0.0.1:5000/three"
        p_body = json.dumps({
            "username": "Python",
            "password": "unittest"
        })
        res = requests.post(url,p_body).json()

        self.assertEqual("Login Succss", res['msg'])

    def test_get_from_file(self):
        url = "http://127.0.0.1:5000/four"
        res = requests.get(url)
        self.assertIn('39811C',res.text,)
        # print(type(res.text))
    
if __name__ == "__main__":
    unittest.main()