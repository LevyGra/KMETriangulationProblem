"""
vertex.py
Version: 0.1.0
Author: Levi Graham
Date: 24.10.2022

Description:
    This file contains the definition for the Vertex class that is used
    by the Graph class for the triangulation problem proposed in the
    Kappa Mu Epsilon meeting on 10.10.2022. This file contains the
    definition the Graph class uses to reference a vertex and which
    other vertices

Version History:
    0.1.0 - Seperated from original file that previously was used to
            solve this problem.
"""

class Vertex:
    """
    A class to represent a vertex in a graph.
    
    Attributes
    ----------
    num : int
        the number for this vertex to denote it's position in the graph
    incoming : list
        a list of verticies that have an incoming edge to this vertex
    outgoing : list
        a list of verticies that have an outgoing edge to this vertex
    pos_row : int
        the row of the graph that this vertex is in
    pos_col : int
        the column of the graph that this vertex is in
        
    Methods
    -------
    add_incoming(incoming_num):
        Appends the incoming_number onto the incoming list and sorts 
        the list.
    add_outgoing(outgoing_num):
        Appends the outgoing_number onto the outgoing list and sorts 
        the list.
    """
    def __init__(self, num:int, pos:tuple[int,int]):
        """
        Constructs all the necessary attributes for a Vertex object.
        
        Parameters
        ----------
        num : int
            the number for this vertex to denote it's position on the 
            graph
        pos : tuple(int,int)
            the position of the number in the graph, used for traversing 
            the graph
        """
        self.num = num
        self.row, self.col = pos
        self.incoming = []
        self.outgoing = []
        
    def add_incoming(self, incoming_num:int) -> None:
        """
        Add the incoming_num onto the incoming list.
        
        Parameters
        ----------
        incoming_num : int
            number denoting a vertex that has an incoming edge to 
            this vertex
            
        Returns
        -------
        None
        """
        self.incoming.append(incoming_num)
        self.incoming.sort()
        
    def add_outgoing(self, outgoing_num:int) -> None:
        """
        Add the outgoing_num onto the outgoing list.
        
        Parameters
        ----------
        outgoing_num : int
            number denoting a vertex that has an outgoing edge to 
            this vertex
            
        Returns
        -------
        None
        """
        self.outgoing.append(outgoing_num)
        self.outgoing.sort()