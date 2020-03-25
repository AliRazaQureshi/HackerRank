from Implementing_Dequeue import Dequeue
d = Dequeue()
def is_Palindrome(word):
    for char in word:
        d.add_rear(char)

    still_equal = True
    while d.size() > 1 and still_equal:
        first_char = d.remove_front()
        last_char = d.remove_rear()
        if first_char != last_char:
            still_equal = False
    return still_equal

if __name__ == '__main__':
    word = input()
    print(is_Palindrome(word))