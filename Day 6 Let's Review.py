# Enter your code here. Read input from STDIN. Print output to STDOUT
def even_odd_chars(string):
    even_chars = ""
    odd_chars = ""
    for index in range(0, len(string)):
        if index % 2 == 0:
            even_chars += string[index]
        
        else:
            odd_chars += string[index]

    print("{} {}".format(even_chars, odd_chars))
    
num_string = int(input())
while num_string > 0:
    string = input()
    even_odd_chars(string)
    num_string -= 1
