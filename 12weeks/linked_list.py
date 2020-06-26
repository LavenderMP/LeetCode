import sys
class LinkedNode:
  def __init__(self, val):
    self.val = val
    self.next = None
    self.prev = None

  def connectNodes(self, other):
    self.next = other
    other.prev = self

  def remove_node(self):
    self.prev.next = self.next
    self.next.prev = self.prev


class MyLinkedList:

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.size = 2

    self.head = LinkedNode(None)
    self.tail = LinkedNode(None)
    self.head.connectNodes(self.tail)

  def get(self, index: int) -> int:
    """
    Get the value of the index-th node in the linked list. If the index is invalid, return -1.
    """
    Node = self.getNode(index)
    if Node == -1 or Node is None:
      return -1
    else:
      return Node.val

  def getNode(self, index):
    curNode = self.head
    if index < 0 or index > self.size - 1:
      return -1
    while index > 0:
      curNode = curNode.next
      index -= 1
    return curNode

  def addAtHead(self, val: int) -> None:
    """
    Add a node of value val before the first element of the linked list.
    After the insertion, the new node will be the first node of the linked list.
    """
    if self.head.val is None:
      self.head.val = val
    else:
      curNode = LinkedNode(val)
      curNode.connectNodes(self.head)

      self.head = curNode
      self.size += 1

  def addAtTail(self, val: int) -> None:
    """
    Append a node of value val to the last element of the linked list.
    """
    if self.tail.val is None:
      self.tail.val = val
    else:
      curNode = LinkedNode(val)
      self.tail.connectNodes(curNode)

      self.tail = curNode
      self.size += 1

  def addAtIndex(self, index: int, val: int) -> None:
    """
    Add a node of value val before the index-th node in the linked list.
    If index equals to the length of linked list, the node will be appended to the end of linked list.
    If index is greater than the length, the node will not be inserted.
    """
    if index == 0:
      self.addAtHead(val)
    elif index == self.size:
      self.addAtTail(val)
    elif index > self.size:
      return
    else:
      newNode = LinkedNode(val)
      curNode = self.getNode(index)
      prevNode = curNode.prev

      newNode.connectNodes(curNode)
      prevNode.connectNodes(newNode)
      self.size += 1

  def deleteAtIndex(self, index: int) -> None:
    """
    Delete the index-th node in the linked list, if the index is valid.
    """
    if index < 0 or index > self.size - 1:
      return
    elif index == 0:
      curNode = self.head
      self.head = curNode.next
      self.head.prev = None
    elif index == self.size - 1:
      curNode = self.tail
      self.tail = curNode.prev
      self.tail.next = None
    else:
      curNode = self.getNode(index)
      curNode.remove_node()
    self.size -= 1

  def display(self):
    curNode = self.head
    while curNode:
      print(curNode.val, end=' ')
      curNode = curNode.next
    print()
    print("#" * 20)

# Your MyLinkedList object will be instantiated and called as such:
# ["MyLinkedList","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"]
# [[],[2],[1],[2],[7],[3],[2],[5],[5],[5],[6],[4]]

llinked = MyLinkedList()
llinked.addAtHead(1)
llinked.addAtTail(4)
llinked.addAtTail(4)
llinked.addAtTail(3)
llinked.addAtTail(4)
llinked.addAtIndex(1,2)
llinked.addAtIndex(0,9)
llinked.addAtIndex(7,9)
llinked.addAtIndex(7,8)
llinked.display()
llinked.deleteAtIndex(2)
llinked.display()

# a = LinkedNode(1)
# b = LinkedNode(2)
# c = LinkedNode(3)
#
# a.connectNodes(b)
# b.connectNodes(c)
#
# print(b.prev.val)