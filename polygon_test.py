from polygon import *
from polygon_sequence import *


#Test - Module 1


p = Polygon(4,10)
p1 = Polygon(4,10)
p2 = Polygon(5,12)


p_s = Polygon_seq(4,10)

def test_init():
    assert (p.no_of_edges == 4),"something is wrong. please check the code"
    assert (p.circumradius ==10),"something is wrong. please check the code"

def test_repr():
    assert (len(repr(p))>20),"something is wrong. please check the code"

def test_eq():
    assert (p == p1),"something is wrong. please check the code"

def test_gt():
    assert (p2>p1),"something is wrong. please check the code"

def test_interior_angle():
    assert (type(p.interior_angle()) is float),"something is wrong. please check the code"
    assert (p.interior_angle()>0),"something is wrong. please check the code"

def test_edge_length():
    assert (type(p.edge_length()) is float),"something is wrong. please check the code"
    assert (p.edge_length()>0),"something is wrong. please check the code"

def test_apothem():
    assert (type(p.apothem()) is float),"something is wrong. please check the code"
    assert (p.apothem()>0),"something is wrong. please check the code"

def test_area():
    assert (type(p.area()) is float),"something is wrong. please check the code"
    assert (p.area()>0),"something is wrong. please check the code"

def test_perimeter():
    assert (type(p.perimeter()) is float),"something is wrong. please check the code"
    assert (p.perimeter()>0),"something is wrong. please check the code"

def test_max_efficiency():
    assert (p_s.max_efficieny() >0 ),"something is wrong. please check the code"

def test_len():
    assert (len(p_s)>0),"something is wrong. please check the code"

