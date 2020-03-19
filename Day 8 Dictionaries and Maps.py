# Enter your code here. Read input from STDIN. Print output to STDOUT
def create_phonebook(n):
    phoneBook = dict()
    while n > 0:
        user_input = list(map(str, input().split(" ")))
        phoneBook[user_input[0]] = user_input[1]
        n -= 1
    return phoneBook

n = int(input())
phoneBook = create_phonebook(n)
while True:
    try:
        name = input()
    except EOFError:
        break
    if name in phoneBook:
        print("{}={}".format(name, phoneBook[name]))
    else:
        print("Not found")