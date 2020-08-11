import unittest
import requests
import json

class TestLogin(unittest.TestCase):
    # def setUp(self):
    #     print("Test cast started")

    # def tearDown(self):
    #     print("Test case closed")

    # @classmethod
    # def setUpClass(cls):
    #     try:
    #         with open('./static/testdata.json','r') as cls.t_data:
    #             print(type(cls.t_data))
    #     except Exception as e:
    #         print(e)

    # @classmethod
    # def tearDownClass(cls):
    #     pass

    def test_get_from_file(self):
        url = "http://127.0.0.1:5000/one"
        res = requests.get(url)
        self.assertIn('00039811C',res.text)
        # print(type(res.text))

    def test_post_with_json(self):
        url = "http://127.0.0.1:5000/three"
        p_body = json.dumps({
            "username": "Python",
            "password": "unittest"
        })
        res = requests.post(url,p_body).json()

        self.assertEqual("Login Success", res['msg'])

    
    
if __name__ == "__main__":
    unittest.main()