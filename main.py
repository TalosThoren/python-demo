from example import list_compare

def demo_main():
    current_list = [1,4,7,8,12]
    target_list = [2,4,6,8,24,10,9]
    results = list_compare.compare( current_list, target_list )

    print 'Current List: ' + str( current_list )
    print 'Target List: ' + str( target_list )
    print 'Additions: ' + str( results['additions'] )
    print 'Deletions: ' + str( results['deletions'] )

if __name__ == '__main__':
    demo_main()
