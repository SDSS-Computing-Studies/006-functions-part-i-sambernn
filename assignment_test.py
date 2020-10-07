#! python3

import task1
import task2
import task3
import task4
import problem1
import problem2
import problem3

def test1():
  assert task1.sum(11,2.5) == 13.5
  assert task1.sum(8,-2) == 6

def test2():
  assert task2.largest([3,1,4,7,13,9]) == 13
  assert task2.largest([5,1,12.3]) == 12.3

def test3():
  assert task3.perimeter( [5,2,6]) == 13
  assert task3.perimeter( [9,8,6,5.5] ) == 28.5

def test4():
  assert task4.isInteger( 9.5 ) == False
  assert task4.isInteger( -2 ) == True

def test5():
  # Problem 1 Assertions
  assert problem1.hypotenuse(3,4,False) == 5
  assert problem1.hypotenuse(13,5,True) == 12

def test6():
  # Problem 2 Assertions
  assert round(problem2.distance( (2,4) , (6,3)) , 3) == 4.123
  assert round(problem2.distance( (-3,2.2) , (1,2)) , 3) == 4.005

def test7():
  # Problem 3 Assertions
  assert problem3.factors(12) == [1,2,3,4,6,12]
  assert problem3.factors(37) == [1,37]


  
