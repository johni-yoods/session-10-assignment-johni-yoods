import math

class Polygon:
    """
    Polygon class to generate polygon of
    desired vertex and circumradius.
    """

    def __init__(self,no_of_edges:int,circumradius:int):
        """
            no_of_edges: Number of vertices of the plygon
            circumradius: circumradius of the polygon.
        """
        self.no_of_edges = no_of_edges
        self.circumradius = circumradius
    
    def __repr__(self)->str:
        """
        function to display the output of the class object.
        
        """
        return (f"Polygon with {self.no_of_edges} vertices and {self.circumradius} as Circumradius")
    
    def __eq__(self, obj)->bool:
        """
        check the self.no_of_edges and self.circumradius with the
        the obj passed as an argument

        returns : bool  - True if equal else False
        """
        if not isinstance(obj,Polygon):
            raise TypeError('expected polygon class but given is not a polygon class')
        
        return ((self.no_of_edges == obj.no_of_edges) and (self.circumradius == obj.circumradius))
    
    def __gt__(self, obj)->bool:
        """
        This class is to check greater than. It checks the self.no_of_edges and self.circumradius with the ones
        of the other passed in as argument

        returns: bool  - True if equal else False
        """
        if not isinstance(obj,Polygon):
            raise TypeError('expected polygon class but given is not a polygon class')
        return self.no_of_edges > obj.no_of_edges   
    
    def interior_angle(self)->float:
        """
        This function calculates the interior angle (n-2)*180/n
       
       """
        
        return ((self.no_of_edges-2)*180)/self.no_of_edges
    
    def edge_length(self)->float:
        """
        This function calculates the edge length s=2*R*sin(pi/n)

        """
        return 2*self.circumradius*math.sin(math.pi/self.no_of_edges)
    
    def apothem(self)->float:
        """
        This function calculates the apothem a=R*cos(pi/n)

        """
        return self.circumradius*math.cos(math.pi/self.no_of_edges)
    
    def area(self)->float:
        """
        This function calculates the area, area=1/2*n*s*a

        """
        return 0.5*self.apothem()*self.edge_length() * self.no_of_edges
    
    def perimeter(self)->float:
        """
        This function calculates the perimeter, perimeter = n*s

        """
        return self.no_of_edges * self.edge_length()

