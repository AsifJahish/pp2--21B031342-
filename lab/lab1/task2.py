


def execute_commands(n, commands):
    s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    for i in range(n):
        command, value = commands[i].split()
        if command == 'pop':
            s.pop()
        elif command == 'remove':
            s.remove(int(value))
        elif command == 'discard':
            s.discard(int(value))
    return sum(s)


n = int(input())

commands = ['remove 4', 'pop', 'discard 9']
print(execute_commands(n, commands))
