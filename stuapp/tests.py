class MinStack:

    def __init__(self):
        # do intialization if necessary
        self.stack = []

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, number):
        # write your code here
        self.stack.append(number)

    """
    @return: An integer
    """

    def pop(self):
        # write your code here
        n = self.stack[-1]
        self.stack = self.stack[0:len(self.stack)]
        return n

    """
    @return: An integer
    """

    def min(self):
        # write your code here
        n = self.stack[0]
        for v in self.stack:
            if v < n:
                n = v
        return n




