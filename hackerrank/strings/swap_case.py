# https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    reverse = ''
    for char in s:
        if char.islower():
            reverse += char.upper()
        else:
            reverse += char.lower()
    return reverse

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
