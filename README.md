Name : Johni Yoods Durai
email : durai.mj@mistralsolutions.com

# Session 10
# Sequence Types


### Polygon 
1. A regular strictly convex polygon is a polygon that has the following characteristics:
   1. all interior angles are less than 180
   2. all sides have equal length
2. For a regular strictly convex polygon with:
   1. n edges (=n vertices)
   2. R circumradius
   3. interiorAngle = (n-2)*180/n
   4. edgeLength, s = 2*R*sin(pi/n)
   5. apothem, a= R*cos(pi/n)
   6. area = 1/2*n*s*a
   7. perimeter = n*s

### def interior_angle(self)->float:
        """
        This function calculates the interior angle (n-2)*180/n
       
       """

        return ((self.no_of_edges-2)*180)/self.no_of_edges

### def edge_length(self)->float:
        """
        This function calculates the edge length s=2*R*sin(pi/n)

        """
        return 2*self.circumradius*math.sin(math.pi/self.no_of_edges)

####    def apothem(self)->float:
        """
        This function calculates the apothem a=R*cos(pi/n)

        """
        return self.circumradius*math.cos(math.pi/self.no_of_edges)

####    def area(self)->float:
        """
        This function calculates the area, area=1/2*n*s*a

        """
        return 0.5*self.apothem()*self.edge_length() * self.no_of_edges

###    def perimeter(self)->float:
        """
        This function calculates the perimeter, perimeter = n*s

        """
        return self.no_of_edges * self.edge_length()
### def __repr__(self)->str:
        """
        function to display the output of the class object.
        
        """
        return (f"Polygon with {self.no_of_edges} vertices and {self.circumradius} as Circumradius")

### def __eq__(self, obj)->bool:
        """
        check the self.no_of_edges and self.circumradius with the
        the obj passed as an argument

        returns : bool  - True if equal else False
        """
        if not isinstance(obj,Polygon):
            raise TypeError('expected polygon class but given is not a polygon class')

        return ((self.no_of_edges == obj.no_of_edges) and (self.circumradius == obj.circumradius))

### def __gt__(self, obj)->bool:
        """
        This class is to check greater than. It checks the self.no_of_edges and self.circumradius with the ones
        of the other passed in as argument

        returns: bool  - True if equal else False
        """
        if not isinstance(obj,Polygon):
            raise TypeError('expected polygon class but given is not a polygon class')
