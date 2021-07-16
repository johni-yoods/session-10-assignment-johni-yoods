from polygon import *

class Polygon_seq:
    """
    This is a polygon sequence class used to develop a custom sequence
    """
    def __init__(self,no_of_edges:int, circumradius:int):
        """
            no_of_edges: Number of vertices of the plygon
            circumradius: circumradius of the polygon. 
        """
        self.no_of_edges = no_of_edges
        self.circumradius = circumradius
        self.ratios = {}
    
    def __repr__(self)->str:
        """
        This function is used to display the output of the class object.
        
        """
            
        return (f"Polygon with {self.no_of_edges} vertices and {self.circumradius} as Circumradius")

    def __len__(self)->int:
        """
        This function is returns the length i.e. no of veritices/edges
        
        """
        return self.no_of_edges
    
    def __getitem__(self):
        """
        This function returns the generated sequence

        returns: Sequence - sequence containing the ratio
        """
        return self.ratios 
    
    def max_efficieny(self)->float:
        """
        Function to  calculate the maximum_efficieny

        """
        for i in range(self.no_of_edges):
            p=Polygon(i+1,self.circumradius)
            self.ratios[i] = p.area()/p.perimeter()
        key = max(self.ratios,key = self.ratios.get)
        return self.ratios[key]
