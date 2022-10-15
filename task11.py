dek = []

while True:
    command = input().strip()
    if command.startswith('push_front'):
        number = int(command.split()[1])
        dek.insert(0, number)
        print('ok')
    elif command.startswith('push_back'):
        number = int(command.split()[1])
        dek.append(number)
        print('ok')
    elif command == 'pop_front':
        if len(dek) == 0:
            print('error')
        else:
            print(dek[0])
            del dek[0]
    elif command == 'pop_back':
        if len(dek) == 0:
            print('error')
        else:
            print(dek[-1])
            del dek[-1]
    elif command == 'front':
        if len(dek) == 0:
            print('error')
        else:
            print(dek[0])
    elif command == 'back':
        if len(dek) == 0:
            print('error')
        else:
            print(dek[-1])
    elif command == 'size':
        print(len(dek))
    elif command == 'clear':
        dek.clear()
        print('ok')
    elif command == 'exit':
        print('bye')
        break
    else:
        print('error')
