# https://leetcode.com/problems/design-linked-list/

class DDLNode(object):
    def __init__(self, val=0, prev=None, my_next=None):
        self.val = val
        self.prev = prev
        self.next = my_next

    def __str__(self):
        traverse = self
        temp = []
        while traverse is not None:
            temp.append(traverse.val)
            traverse = traverse.next

        return "{ "+', '.join(str(e) for e in temp)+" }"


class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        traverse = self.head
        temp = []
        while traverse is not None:
            temp.append(str(traverse.val))
            traverse = traverse.next

        return "[ "+', '.join(str(e) for e in temp)+" ]"

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        traverse = self.head
        count = 0
        while traverse is not None:
            if count == index:
                return traverse.val

            traverse = traverse.next
            count += 1

        return -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = DDLNode(val=val)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

        self.size += 1
        if self.size == 1:
            self.tail = self.head

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.size == 1:
            self.tail = self.head

        new_node = DDLNode(val=val)
        new_node.prev = self.tail

        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node

        self.size += 1
        if self.size == 1:
            self.head = self.tail

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == 0:
            self.addAtHead(val)
            return

        new_node = DDLNode(val)
        traverse = self.head
        count = 0
        if index == self.size:
            self.addAtTail(val)
            return

        while traverse is not None:
            if count == index:
                new_node.next = traverse
                new_node.prev = traverse.prev
                traverse.prev.next = new_node
                traverse.prev = new_node
                self.size += 1
                return

            traverse = traverse.next
            count += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index == 0:
            if self.size == 1 or self.size == 0:
                self.head = None
                self.tail = None
                self.size = 0
                return

            if self.head is not None:
                self.head = self.head.next
                self.size -= 1
                return

        if index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return

        traverse = self.head
        count = 0
        while traverse is not None:
            if count == index:
                traverse.prev.next = traverse.next
                if traverse.next is not None:
                    traverse.next.prev = traverse.prev
                self.size -= 1
                break

            traverse = traverse.next
            count += 1


# myLinkedList = MyLinkedList()
# myLinkedList.addAtHead(24)
# print(f"> {myLinkedList.head}, {myLinkedList.tail}, {myLinkedList.size}")
# res = myLinkedList.get(1)
# print(f"> {res}")
# myLinkedList.addAtTail(18)
# print(f"> {myLinkedList.head}, {myLinkedList.tail}, {myLinkedList.size}")
# myLinkedList.deleteAtIndex(1)
# myLinkedList.addAtTail(30)
# print(f"> {myLinkedList.head}, {myLinkedList.tail}, {myLinkedList.size}")

func_arr = ["MyLinkedList", "addAtHead", "addAtTail",
            "addAtIndex", "get", "deleteAtIndex", "get"]
input_arr = [[], [1], [3], [1, 2], [1], [1], [1]]

myLinkedList = MyLinkedList()
for i in range(len(func_arr)):
    curr_func = func_arr[i]
    curr_input = input_arr[i]
    print(f"\n{curr_func}{curr_input}")
    if curr_func == "addAtHead":
        myLinkedList.addAtHead(curr_input[0])
    elif curr_func == "addAtTail":
        myLinkedList.addAtTail(curr_input[0])
    elif curr_func == "get":
        print(myLinkedList.get(curr_input[0]))
    elif curr_func == "addAtIndex":
        print(myLinkedList.addAtIndex(curr_input[0], curr_input[1]))
    elif curr_func == "deleteAtIndex":
        print(myLinkedList.deleteAtIndex(curr_input[0]))
    else:
        continue
    print(f"> {myLinkedList} \n{myLinkedList.tail}, {myLinkedList.size}")
