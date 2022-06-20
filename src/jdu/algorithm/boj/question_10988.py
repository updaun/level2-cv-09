import sys
is_palindrome = sys.stdin.readline().strip()
print(int(is_palindrome == is_palindrome[::-1]))