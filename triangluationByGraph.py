"""
triangulation.py                             
Author: Levi Graham
Date: 13.10.2022

Description: 
    triangulation.py is an implementation to try and find a solution 
    the triangluation problem that was proposed in the 
    Kappa Mu Epsilon meeting on 10.10.2022. This file creates a graph
    theory approach to finding the tiling any given n and k value.
    
Modifications:
 - 12.10.2022 | LG | Added base Vertex and Graph classes.
 - 12.10.2022 | LG | Started implementation on building the graph.
 - 13.10.2022 | LG | Fixed bug in building the graph. Started writing 
                     documentation for this file.
 - 13.10.2022 | LG | Fixed bug to allow for generalized n and k values.
 - 13.10.2022 | LG | Added print_graph method to Graph class.
 - 13.10.2022 | LG | Stubbed out the generate squence methods in Graph
                     class.
"""
import time

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
        
class Graph:
    """
    A class to represent a graph of Vertex classes. 
    The graph has n verticies split into k rows.
    
    Attributes:
        n : int 
            represents the total number of verticies in the graph
        k : int 
            represents the total number of rows in the graph
        graph : list 
            list representation of the graph, the items in the list are 
            lists of the rows of verticies.
    
    Methods:
        build()
            Builds the graph by assigning verticies their incoming and 
            outgoing edges and placing them in the graph in the correct
            position.
        print_graph()
            Builds a printable version of the graph for output to the
            console for testing.
    """
    def __init__(self, n:int, k:int):
        """
        Constructs all necessary attributes for a Graph object.
        
        Parameters:
            n (int): total number of verticies in the graph
            k (int): number of rows for the graph
        """
        self.n = n
        self.k = k
        self.graph = [[None] * (n // k) for _ in range(self.k)]
        
    def build(self):
        """
        Builds the graph by creating the verticies and putting them into
        their positions in the graph attribute.
        
        Parameters:
            None
        
        Returns:
            None
        """
        number_list = [(x + 1) for x in range(self.n)]
        n, k = self.n, self.k
        for i in range(self.k):
            numbers_on_row = number_list[i * (n//k):i * (n//k) + (n//k)]
            for j in range(len(numbers_on_row)):
                # Find the number for this vertex.
                x = numbers_on_row[j]
                
                # Find verticies in each direction.
                up, down = x - (n // k), x + (n // k)
                left, right = x - 1, x + 1
                up_diag, down_diag = x - (1 + n // k), x + (1 + n // k)
                
                # Create Vertex
                pos = (i, j)
                vertex = Vertex(x, pos)
                
                # When one of the calculated edges is in the number_list
                # add it to the appropriate incoming or outgoing.
                # Add up to incoming if the upward direction is in the
                # graph.
                #if up in number_list and x - (n//k) > 1: 
                if up in number_list:
                    vertex.add_incoming(up)
                # Add down to outgoing if the downward direction is in
                # the graph.
                #if down in number_list and x + (n//k) <= n: 
                if down in number_list:
                    vertex.add_outgoing(down)
                # Add left to incoming if x is not on the left side
                # of the graph.
                #if left in number_list and x <= i * 0: 
                if left in number_list:
                    vertex.add_incoming(left)
                # Add right to outgoing if x is not equal to k.
                # TODO: Change this logic
                #if right in number_list and x != i * 0 + k - 1:
                if right in number_list: 
                    vertex.add_outgoing(right)
                # Add up_diag to outgoing if it is in the graph.
                if up_diag in number_list: 
                    vertex.add_outgoing(up_diag)
                # Add down_diag to incoming if it is in the graph.
                if down_diag in number_list: 
                    vertex.add_incoming(down_diag)
                
                # Add vertex in correct position
                self.graph[i][j] = vertex
                
    def print_graph(self):
        """
        Builds a printable version of the graph for output to the
        console for testing.
        
        Parameters:
            None
        
        Returns:
            None
        """
        
        # Generate output string
        # Example:
        #   -----------
        #   | XX | XX |
        #   -----------
        #   | XX | XX |
        #   -----------
        # TODO: Make printed number length programatic for numbers with length > 2.
        output = "-" * (1 + self.n//self.k) + "----" * (self.n//self.k) + "\n"
        for i in range(len(self.graph)):
            line_output = "|"
            for j in range(len(self.graph[i])):
                line_output += " " + str(self.graph[i][j].num).zfill(2) + " "
                line_output += "|"
            line_output += "\n"
            output += line_output
            output += "-" * (1 + self.n//self.k) + "----" * (self.n//self.k) + "\n"
        print(output)
        
    def generate_sequence_down(self) -> list:
        """
        Generates the sequence of nodes to hit to traverse the graph
        without crossing an edge more than once. 
        
        Parameters:
            None
        
        Returns:
            list : List generated by the traversal algorithm.
        """
        # Define direction markers
        is_down = True
        is_zigzag = False
        last_move = None
        
        # Initialize current vertex with the first vertex.
        curr_vertex:Vertex = self.graph[0][0]
        start_vertex:Vertex = self.graph[0][0]
        
        # Initialize the output string with the current vertex.
        output = [curr_vertex.num]
        
        # Loop while n isn't in the output string twice
        while output.count(self.n) < 2:
            # Check if you can progress down to the next node.
            if curr_vertex.row == len(self.graph) - 1:
                # Switch over to is_zigzag
                is_down = False
                is_zigzag = True
                #last_move = None
            elif curr_vertex.row == 0 and curr_vertex.col == start_vertex.col + 1:
                # Switch over to is_down
                is_down = True
                is_zigzag = False
                start_vertex = curr_vertex
                last_move = None
            elif output.count(self.n) == 2:
                is_down = False
                is_zigzag = False
            
            # Progress the downward direction.
            if is_down:
                # Progress down the graph to the bottom left node.
                new_vertex:Vertex = self.graph[curr_vertex.row+1][curr_vertex.col]
                # Check if the next vertex can be moved to.
                if new_vertex.num in curr_vertex.outgoing:
                    curr_vertex = new_vertex
                    # Append the next vertex to the output.
                    output.append(curr_vertex.num)
            # Progress by doing the zigzag loop.   
            elif is_zigzag:
                if last_move == None or last_move == "back":
                    curr_row, curr_col = curr_vertex.row, curr_vertex.col
                    if curr_col+1 >= 0 and curr_col+1 <= len(self.graph[0])-1:
                        new_vertex = self.graph[curr_row][curr_col+1]
                        if new_vertex.num in curr_vertex.outgoing:
                            curr_vertex = new_vertex
                            last_move = "across"
                            output.append(curr_vertex.num)
                elif last_move == "across":
                    curr_row, curr_col = curr_vertex.row, curr_vertex.col
                    if((curr_row-1 >= 0 and curr_row-1 <= len(self.graph)-1) and 
                       (curr_col-1 >= 0 and curr_col-1 <= len(self.graph[0])-1)):
                        new_vertex = self.graph[curr_row-1][curr_col-1]
                        if new_vertex.num in curr_vertex.outgoing:
                            curr_vertex = new_vertex
                            last_move = "back"
                            output.append(curr_vertex.num)
                    else:
                        is_down = True
                        is_zigzag = False
                        last_move = None
    
        return output
    
    def generate_sequence_across(self):
        return None
        
if __name__ == "__main__":
    graph = Graph(12, 3)
    graph.build()
    start = time.time()
    # graph.print_graph()
    print(graph.generate_sequence_down())
    # print(Graph.__doc__)
    end = time.time()
    # print(end-start)
    # len_of_sequence = []
    # for num in [1, 2, 3, 4, 6, 12]:
    #     graph = Graph(12, num)
    #     graph.build()
    #     len_of_sequence.append(len(graph.generate_sequence_down()))
    # print(len_of_sequence)
    