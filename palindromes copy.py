x = "radar"


def palindrome(i):
    if len(i) == 0 or len(i) == 1:
        return True

    if i[0] == i[-1]:
        return palindrome(i[1:-1])
    else:
        return False


print(palindrome(x))



