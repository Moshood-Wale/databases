import unittest
from models.book import Book

class TestBook(unittest.TestCase):

    def setUp(self):
       self.book=Book()
        
    def test_get_all(self):
        get_all= self.book.get_all_users()
        self.assertTrue(type(get_all), 'pandas.core.frame.DataFrame')
        # self.assertIsInstance(get_all,list)
        # self.assertIsNotNone(get_all)
        
    def test_get_by_id(self):  
        get_by_id=self.book.get_by_id(1)
        self.assertIsNotNone(get_by_id)
        self.assertIsInstance(get_by_id,list)
    
    def test_create(self):
        update= self.book.create_book_record(3,'Love takes all',100)
        self.assertIsNotNone(update)
        self.assertIsInstance(update,str)
        self.assertEqual(update,'Record created')

    def test_update(self):
        update= self.book.update_book_record('fences',50,1)
        self.assertIsNotNone(update)
        self.assertIsInstance(update,str)
        self.assertEqual(update,'Record updated')
        
    def test_delete(self):
        delete=self.book.delete_book_record(7)
        self.assertEqual(delete,'Record deleted')
        self.assertIsNotNone(delete)

if __name__ == '__main__':
    unittest.main()