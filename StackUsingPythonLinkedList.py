class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value


class StackLL:

    def __init__(self):
        self.head = None

    def __str__(self):
        node = self.head
        lst = []
        while node:
            lst.append(str(node.value))
            node = node.next

        return '\n'.join(lst)

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, value):

        node = Node(value)
        node.next = self.head
        self.head = node

    def pop(self):

        if self.isEmpty():
            return 'stack does not exist'
        first = self.head
        self.head = first.next
        first.next = None

    def peek(self):
        return self.head.value

    def delete(self):
        self.head = None


if __name__ == '__main__':
    stll = StackLL()
    stll.push(10)
    stll.push(20)
    stll.push(30)
    stll.push(40)
    stll.push(50)
    print(stll)
    print('***************')
    stll.pop()
    print(stll)
