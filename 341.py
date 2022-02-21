# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """

#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """

#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
from collections import deque
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.index = 0    
        self.stack = []
        for item in nestedList:
            self.makeFlat(item)

    def makeFlat(self, item: [NestedInteger]):
        if item.isInteger():
            self.stack.append(item.getInteger())
        else:
            for newitem in item.getList():
                self.makeFlat(newitem)

    def next(self) -> int:
        top_element =  self.stack[self.index]
        self.index += 1
        return top_element

    
    def hasNext(self) -> bool:
        if len(self.stack) > self.index:
            return True
        return False

         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())