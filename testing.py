import unittest
from main import main, is_valid_email
from sql import save_to_fav, view_favs, create_new_user, authentication
from gptapi import recomendation
from weatherAPI import fetch_weather

class TestMain(unittest.TestCase):

    #def setUp(self):
        #self.main = main()
        #print("Test passed")

    def test_email(self):
        self.assertTrue(is_valid_email('test@gmail.com'))
        self.assertFalse(is_valid_email('test'))
        print("Test passed")

    def test_gpt(self):
        rec_test = recomendation({"sunny with a chance of light rain"})
        self.assertIsNotNone(rec_test)
        print("Test passed")

    def test_weather(self):
        fetch = fetch_weather('newyork')
        self.assertIsNotNone(fetch)
        print("Test passed")

    def test_create(self):
        #new user has to be created each time!
        self.assertTrue(create_new_user(" @gmail.com", " ", "hello"))

    def test_auth(self):
        self.assertFalse(authentication("ann@gmail.com", "hello"))
        self.assertTrue(authentication("anna@gmail.com", "hello"))
        print("Test passed")

    def test_save(self):
        self.assertIsNone(save_to_fav("anna@gmail.com", "anna", "shirt"))
        print("Test passed")
    
    def test_view(self):
        self.assertIsNone(view_favs("anna@gmail.com"))
        print("Test passed")

if __name__ == '__main__':
    unittest.main()