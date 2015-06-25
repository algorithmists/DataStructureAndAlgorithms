#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      alok
#
# Created:     24/06/2015
# Copyright:   (c) alok 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
        print 'No item in stack'
        return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

     def stack_items(self):
        if self.items == []:
            return self.isEmpty()
        else:
            for item in self.items:
                print item

##if __name__ == '__main__':
##    stack = Stack()
##    #stack.push(10)
##    #stack.push(20)
##    stack.stack_items()
