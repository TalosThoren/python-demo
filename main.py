from example import list_compare
from example import social_analysis

def demo_social( filename ):

    tree = social_analysis.csv_to_tree( filename )

    rootNodes = [node for postId, node in tree.items() if node.repostId == '-1']

    for node in rootNodes:
        print str( node.postId ) + ": " + str( social_analysis.count_followers( node ) )

def demo_main():
    print 'BEGIN LIST COMPARE DEMO:'
    print '------------------------'
    current_list = [1,4,7,8,12]
    target_list = [2,4,6,8,24,10,9]
    results = list_compare.compare( current_list, target_list )

    print 'Current List: ' + str( current_list )
    print 'Target List: ' + str( target_list )
    print 'Additions: ' + str( results['additions'] )
    print 'Deletions: ' + str( results['deletions'] )

    print ''
    print 'BEGIN SOCIAL ANALYSIS DEMO:'
    print '---------------------------'
    print ''
    print 'First we use an altered sample csv, to ensure this code does not just handle the sample.'
    csv_file = './tests/social_media_input.csv'
    demo_social( csv_file )

    print ''
    print 'Now we use an unaltered sample, just for demonstration'
    csv_file = './tests/unaltered_sample_input.csv'
    demo_social( csv_file )


if __name__ == '__main__':
    demo_main()
