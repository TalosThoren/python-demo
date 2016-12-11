def find_missing( current_list, target_list ):
    return [ x for x in target_list if x not in current_list ]

def compare( current_list, target_list ):
    additions_list = find_missing( current_list, target_list )
    deletions_list = find_missing( target_list, current_list )
    return { 'additions': additions_list, 'deletions': deletions_list }
