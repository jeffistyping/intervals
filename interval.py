from typing import Tuple, List
from bisect import bisect_left

'''Interval object
Represents the interval object, with methods to add, delete and retrieve ranges of numbers
The object contains one instance variable, data, which represents the ranges currently added
'''
class Interval(object):
  
  def __init__(self, data:List[Tuple[int,int]] = []) -> None:
    self.data = sorted(data, key = lambda x: (x[0],x[1]))

  def Add(self, interval: Tuple[int,int]) -> None:
    '''
    Adds a range specified by the user
    Partial range overlaps will be merged, duplicates will not be added
    '''
    if len(self.data) == 0:
      self.data.append(interval)
      return
    
    low, high = interval
    right,left = 0,0
    
    while right < len(self.data):
      if low <= self.data[right][1]:
        if high < self.data[right][0]:
          break
        low = min(low, self.data[right][0])
        high = max(high, self.data[right][1])
      else:
        left +=1
      right += 1
    self.data = self.data[:left] + [(low,high)] + self.data[right:]

  
  def Delete(self, interval: Tuple[int,int]) -> None:
    '''
    Deletes a range specified by the user
    If the range does not exist, nothing will be removed
    '''
    low, high = interval
    output = []
    
    lb = 0
    ub = len(self.data)-1
    for i in range(len(self.data)):
      if self.data[i][1] < low:
        lb += 1
    
    for i in range(len(self.data)-1,-1,-1):
      if self.data[i][0] > high:
        ub -=1
    
    for i in range(lb,ub+1):
      if self.data[i][0] < low:
        output.append((self.data[i][0], low))
      if high < self.data[i][1]:
        output.append((high, self.data[i][1]))
    
    self.data[lb:ub+1] = output

  def Get(self, interval: List[Tuple[int,int]]) -> List[Tuple[int,int]]:
    '''
    Get selected intervals (if exists) in the saved ranges
    '''
    output = []
    low, high = interval

    for i in range(len(self.data)):
      if low <= self.data[i][0] and self.data[i][1] <= high:
        output.append(self.data[i])
    return output

  def __str__(self):
    return "Intervals: {" + str(self.data) + "}"
  
  __repr__ = __str__