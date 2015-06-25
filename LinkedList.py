
import Stack as stack

from Stack import *


class Node(object):
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class LinkedList(object):

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found


    def print_list(self):
        current = self.head
        if self.head == None:
            self.isEmpty()
        else:
            while current != None:
                print current.getData()
                current = current.getNext()




    def remove(self,item):
        current = self.head
        previous = None
        found = False


        while current != None:
            if current.getData() == item:
                current = current.getNext()
                print 'I am here'
                previous.setNext(current)
                print 'Item removed'

            else:
                previous = current
                current = current.getNext()



##'''
##This is an iterative approach of printing the list in reverse order where we iterate over the list and push item in to the
##stack. Then pop the item from the stack which print the list in reverse order.
##Time complexicity is O(n) for traversing the whole list and O(1) ---> contsant time for push and pop operation
##
##'''

    def print_reverse(self):

            stack = Stack()
            current = self.head
            if self.head == None:
                self.isEmpty()
            else:
                while current != None:
                    item = current.getData()
                    stack.push(item)
                    current = current.getNext()
            #stack.stack_items()
            print 'In reverse order'
            while stack.items != None:
                    if stack.items == []:
                        return stack.isEmpty()
                    else:

                        print stack.pop()



##'''
##This is an iterative approach of reversing the whole list
##Time complexicity is O(n) for traversing the whole list and Space Complexicity O(1)
##
##'''


    def reverse_linked_list(self):


        if self.head == None:
                self.isEmpty()

        current = self.head
        current = current.getNext()

        previous = self.head

        self.head.setNext(None)

        while current is not None:
            print 'I am here'
            next_node = current.getNext()
            current.setNext(previous)
            previous = current
            current = next_node

        self.head = previous
        self.print_list()







if __name__ == '__main__':

	mylist = LinkedList()

	mylist.add(31)
	mylist.add(77)
	mylist.add(17)
	mylist.add(93)
	mylist.add(26)
	mylist.add(54)

mylist.print_list()

mylist.print_reverse()

mylist.reverse_linked_list()

#mylist.print_list()
##	print(mylist.size())
##	print(mylist.search(93))
##	print(mylist.search(100))
##
##	mylist.remove(93)
##	print(mylist.size())















