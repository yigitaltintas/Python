# create stack
def createStack():
    stack = []
    return stack


# size stack
def size(stack):
    pass


# is empty stack
def isEmpty(stack):
    pass


# push item in stack
def push(stack, item):
    return stack.append(item)


# pop item in stack
def pop(stack):
    return stack.pop()


# reverse string
def reverse(string):
    stack = createStack()

    n = len(string)

    for i in range(n):
        push(stack, string[i])

    new_string = ""

    for i in range(n):
        new_string += pop(stack)

    return new_string


print(reverse('datai'))
