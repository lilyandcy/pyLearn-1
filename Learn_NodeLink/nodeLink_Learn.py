class Node():
    __slots__=['_item','_next']
    def __init__(self,item):
        self._item=item
        self._next=None
    def getItem(self):
        return self._item
    def getNext(self):
        return self._next
    def setItem(self,newitem):
        self._item=newitem
    def setNext(self,newnext):
        self._next=newnext

class SingleLinkedList():
    def __init__(self):
        self._head=None
        self._size=0
    def isEmpty(self):
        return self._head==None
    def add(self,item):
        temp=Node(item)
        temp.setNext(self._head)
        self._head=temp
    def append(self,item):
        temp=Node(item)
        if self.isEmpty():
            self._head=temp
        else:
            current=self._head
            while current.getNext()!=None:
                current=current.getNext()
            current.setNext(temp)
    def search(self,item):
        current=self._head
        foundItem=False
        while current!=None and not foundItem:
            if current.getItem() == item:
                foundItem=True
            else:
                current=current.getNext()
        return foundItem
    def index(self,item):
        current=self._head
        count=0
        found=None
        while current!=None and not found:
            count+=1
            if current.getItem()==item:
                found=True
            else:
                current=current.getNext()
        if found:
            return count
        else:
            raise ValueError, '%s is not in linkedlist' %item
    def remove(self,item):
        current=self._head
        pre=None
        while current!=None:
            if current.getItem()==item:
                if not pre:
                    self._head=current.getNext()
                else:
                    pre.setNext(current.getNext())
                break
            else:
                pre=current
                current=current.getNext()
    def insert(self,pos,item):
        if pos == self._size:
            self.append(item)
        else:
            temp=Node(item)
            count=1
            pre=None
            current=self._head
            while count<=pos and current!=None:
                if count==pos:
                    pre=current.getNext()
                    current.setNext(temp)
                    temp.setNext(pre)
                else:
                    current=current.getNext()
                count+=1
                self._size+=1

