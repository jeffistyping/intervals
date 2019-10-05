# How to use 

You will need Python 3.7. No external libraries. 
There is a file `runner.py` that aims to demo the features in the `Interval` library. 
To run, execute `./run_intervals.sh` in terminal. (Unit tests will run, then demo program will follow)

The interval object can also be used in other programs by importing the file 
`import Interval from interval`

# Implementation

As per the design document, the three methods `Get`, `Add` and `Delete` are implemented to manipulate saved ranges of integers. 

The methods have been implemented as instance methods inside the `Interval` class. The class's main purpose is to keep track of the ranges that have been added, and allow for operations to performed on it intuitively. The library was optimized for balanced use of all three functions, as the specifications did not specify % usage. The asymtopic performance of the methods are listed below. 

## Get(interval: Tuple[int,int])
Time: O(N)
Space: O(N) 

## Add(interval: Tuple[int,int])
Time: O(N)
Space: O(1)

## Delete(interval: Tuple[int,int])
Time: O(N)
Space: O(1)

# Additional Design Considerations
The library was optimized for balanced use of all three functions, as the specifications did not specify % usage of each one. 

An alternate design that was considered was storing the ranges as a sorted flat array. This allows for the use of a binary search to find upper and lower bound during all three operations. This would reduce the complexity from O(N) to O(logN) time. The trade off of this design is that it a list of tuples must be generated from flat array during any output (ie string casting) and that will take O(n) time, and additional space. Additionally, the insertion method for lists costs O(N) time to seek for the location so, as a result, this method would also yield an overall runtime of O(N). 

Therefore, since linear operations peg the runtime to O(N), I can conclude that theoretically, my implmentations can be considered an optimal solution. 

# Assumptions 

1. User initializes the object with valid initial intervals (sorted and no overlap)
2. Ranges are to be stored in RAM not persistent memory



