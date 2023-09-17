# 백준 10828번 스택

import sys
class Stack:
    def push(item):
        stacks.append(item)

    def top():
        try:
            print(stacks[-1])
        except IndexError:
            print(-1)

    def size():
        print(len(stacks))

    def empty():
        if len(stacks) == 0:
            print(1)
        else:
            print(0)

    def pop():
        try:
            popItem = stacks.pop()
            print(popItem)
        except IndexError:
            print(-1)

numOfCommand = int(sys.stdin.readline())
stacks = []
for _ in range(numOfCommand):
    commands = sys.stdin.readline().split()

    if commands[0] == 'push':
        Stack.push(commands[1])
    elif commands[0] == 'top':
        Stack.top()
    elif commands[0] == 'size':
        Stack.size()
    elif commands[0] == 'empty':
        Stack.empty()
    elif commands[0] == 'pop':
        Stack.pop()