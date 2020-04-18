
def is_palindrome(s):
    if str(s).lower() == str(s)[::-1].lower():
        return True
    else: return False

if __name__ == '__main__':
    s = input()
    result = is_palindrome(s)
    print(result)
