
import unittest
from database import Database

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.database = Database()

    def test_show(self):
        conn = Database.db_connect()
        result = Database.db_show()
        expected = [('Bitcoin', '29877.5410233920924520')]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
    
