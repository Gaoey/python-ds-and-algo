# https://leetcode.com/problems/design-browser-history/

class DDLNode(object):
    def __init__(self, val=0, prev=None, my_next=None, is_cursor=False):
        self.val = val
        self.prev = prev
        self.next = my_next
        self.is_cursor = is_cursor

    def __str__(self):
        traverse = self
        temp = []
        while traverse is not None:
            val = traverse.val
            if traverse.is_cursor:
                val = "*" + val

            temp.append(val)
            traverse = traverse.next

        return "{ "+', '.join(str(e) for e in temp)+" }"


class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.head = DDLNode(val=homepage)
        self.cursor = self.head
        self.size = 1

    def __str__(self):
        traverse = self.head
        temp = []
        while traverse is not None:
            val = traverse.val
            if traverse.is_cursor:
                val = "*" + val

            temp.append(str(val))
            traverse = traverse.next

        return "[ "+', '.join(str(e) for e in temp)+" ]"

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        new_node = DDLNode(val=url, prev=self.cursor, is_cursor=True)

        self.cursor.next = new_node
        self.cursor = new_node

        if self.cursor.prev is not None:
            self.cursor.prev.is_cursor = False
        self.size += 1

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        count = 0
        while count <= steps:
            if count == steps or self.cursor.prev is None:
                return self.cursor.val

            self.cursor.is_cursor = False
            self.cursor = self.cursor.prev
            self.cursor.is_cursor = True
            count += 1

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        count = 0
        while count <= steps:
            if count == steps or self.cursor.next is None:
                return self.cursor.val

            self.cursor.is_cursor = False
            self.cursor = self.cursor.next
            self.cursor.is_cursor = True
            count += 1


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory("test.com")
# obj.visit("new_test.com")
# print(obj)
# print("\n")
# param_2 = obj.back(1)
# print(obj)
# print(param_2)
# print("\n")
# param_3 = obj.forward(2)
# print(obj)
# print(param_3)

func_arr = ["BrowserHistory", "visit", "visit", "visit", "back",
            "back", "forward", "visit", "forward", "back", "back"]
input_arr = [["leetcode.com"], ["google.com"], ["facebook.com"], [
    "youtube.com"], [1], [1], [1], ["linkedin.com"], [2], [2], [7]]

for i in range(len(func_arr)):
    curr_func = func_arr[i]
    curr_input = input_arr[i]
    print(f"\n{curr_func}{curr_input}")
    if curr_func == "BrowserHistory":
        obj = BrowserHistory(curr_input[0])
    elif curr_func == "visit":
        obj.visit(curr_input[0])
    elif curr_func == "back":
        params = obj.back(curr_input[0])
        print(params)
    elif curr_func == "forward":
        params = obj.forward(curr_input[0])
        print(params)
    else:
        continue
    print(f"> {obj}")
