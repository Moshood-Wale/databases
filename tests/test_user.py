import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
       self.user=User()
        
    def test_get_all(self):
        get_all= self.user.all()
        self.assertTrue(type(get_all), 'pandas.core.frame.DataFrame')

    def test_get_by_id(self):  
        get_by_id=self.user.get_by_id(1)
        self.assertIsNotNone(get_by_id)
        self.assertIsInstance(get_by_id,list)
    
    def test_create_user(self):
        create= self.user.create_user_record()
        self.assertIsNone(create)

    def test_update(self):
        update= self.user.update_user_record('froz','Ade','Peter',1)
        self.assertIsNotNone(update)
        self.assertIsInstance(update,str)
        self.assertEqual(update,'Record updated')
        
    def test_delete(self):
        delete=self.user.delete_user_record(1)
        self.assertEqual(delete,'Record deleted')
        self.assertIsNotNone(delete)  
        
    
if __name__ == '__main__':
    unittest.main()