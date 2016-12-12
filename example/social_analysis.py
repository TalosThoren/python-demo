import csv
import UserDict
from itertools import chain
from pprint import pprint

class Node( object ):

    def __init__( self, postId, repostId, followers ):
        self.postId = postId
        self.repostId = repostId
        self.children = []
        self.followers = followers

    def get_all_children( self ):
        all_children = self.children

        for child in self.children:
            all_children += child.children

        return all_children

class NodeDict( UserDict.UserDict ):

    def addNodes( self, nodes ):
        for i in (1, 2):
            for node in nodes:
                self.data[node.postId] = node
                if( node.repostId in self.data.keys() ):
                    if( node.repostId != '-1' and
                        node not in self.data[node.repostId].children ):
                        self.data[node.repostId].children.append( node )

def csv_to_tree( filename ):

    nodes = []
    data = read_csv( filename )

    for row in data:
        nodes.append( Node( row[0], row[1], row[2] ) )

    nodeDict = NodeDict()
    nodeDict.addNodes( nodes )

    return nodeDict

def read_csv( filename ):

    with open( filename, 'rb' ) as file:
        reader = csv.reader( file )
        reader.next() # Skip the headers
        return [[value.strip(' ') for value in row] for row in reader]

def count_followers( rootNode ):

    followers = int( rootNode.followers )

    for each in rootNode.get_all_children():
        followers += int( each.followers )

    return followers
