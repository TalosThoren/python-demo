from .context import list_compare
import unittest

class TestArrayCompare( unittest.TestCase ):

    current_list = [1,2,3,6]
    target_list = [3,4,5,6,7]
    expected_result = { 'additions': [4,5,7], 'deletions': [1,2] }

    def test_find_missing( self ):
        self.assertIsInstance( list_compare.find_missing( self.current_list, self.target_list ), type( [] ) )

    def test_compare( self ):
        self.assertIsInstance( list_compare.compare( self.current_list, self.target_list ), type( {} ) )
        self.assertEqual( list_compare.compare( self.current_list, self.target_list ), self.expected_result )

if __name__ == '__main__':
    unittest.main()
