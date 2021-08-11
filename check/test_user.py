import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
       self.user=User()
        
    def test_get_all(self):
        get_all= self.user.all()
        self.assertTrue(type(get_all), 'pandas.core.frame.DataFrame')

    
        
    
if __name__ == '__main__':
    unittest.main()