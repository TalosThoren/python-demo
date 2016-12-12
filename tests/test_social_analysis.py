from .context import social_analysis
import unittest

class TestSocialAnalysis( unittest.TestCase ):

    csv_file = './tests/social_media_input.csv'

    def test_read_csv( self ):
        self.assertIsInstance( social_analysis.read_csv( self.csv_file ), type( [] ) )

    def test_count_followers( self ):
        node = social_analysis.Node( '1', '1', '1' )
        self.assertIsInstance( social_analysis.count_followers( node ), int )

if __name__ == '__main__':
    unittest.main()
