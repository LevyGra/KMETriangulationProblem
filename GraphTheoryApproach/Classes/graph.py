"""
graph.py
Version: 0.1.0
Author: Levi Graham
Date: 24.10.2022

Description:
    This file is the class definition for the graph class to implement
    the triangulation problem proposed in the Kappa Mu Epsilon meeting
    on 10.10.2022. This file contains the definitions to perform the 
    graph operations needed.
    
Version History:
    0.0.1 - Seperated from original file that previously was used to
            solve this problem.
"""
from .vertex import Vertex

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

    
    def generate_sequence_across(self) -> list:
        is_across = True
        is_zigzag = False
        last_move = None

        curr_vertex:Vertex = self.graph[0][0]
        start_vertex:Vertex = self.graph[0][0]

        output = [curr_vertex.num]

        while output.count(self.n) < 2:

            if curr_vertex.col == len(self.graph) - 1:
                is_across = False
                is_zigzag = True
            elif curr_vertex.col == 0 and curr_vertex.row == start_vertex.row + 1:
                # Switch over to is_down
                is_across = True
                is_zigzag = False
                start_vertex = curr_vertex
                last_move = None
            elif output.count(self.n) == 2:
                is_across = False
                is_zigzag = False

            if is_across:
                new_vertex:Vertex = self.graph[curr_vertex.row][curr_vertex.col+1]
                if new_vertex.num in curr_vertex.outgoing:
                    curr_vertex = new_vertex
                    output.append(curr_vertex.num)
            
            elif is_zigzag: 
                if last_move == None or last_move == 'back':
                    curr_row, curr_vol = curr_vertex.row, curr_vertex.col
                    

# # Progress by doing the zigzag loop.   
#             elif is_zigzag:
#                 if last_move == None or last_move == "back":
#                     curr_row, curr_col = curr_vertex.row, curr_vertex.col
#                     if curr_col+1 >= 0 and curr_col+1 <= len(self.graph[0])-1:
#                         new_vertex = self.graph[curr_row][curr_col+1]
#                         if new_vertex.num in curr_vertex.outgoing:
#                             curr_vertex = new_vertex
#                             last_move = "across"
#                             output.append(curr_vertex.num)
#                 elif last_move == "across":
#                     curr_row, curr_col = curr_vertex.row, curr_vertex.col
#                     if((curr_row-1 >= 0 and curr_row-1 <= len(self.graph)-1) and 
#                        (curr_col-1 >= 0 and curr_col-1 <= len(self.graph[0])-1)):
#                         new_vertex = self.graph[curr_row-1][curr_col-1]
#                         if new_vertex.num in curr_vertex.outgoing:
#                             curr_vertex = new_vertex
#                             last_move = "back"
#                             output.append(curr_vertex.num)
#                     else:
#                         is_down = True
#                         is_zigzag = False
#                         last_move = None


    def generate_sequence_across(self):
        return None