def reverse_string(s):
    revStr = ""
    for ch in s:
        revStr = ch + revStr

    return revStr


if __name__ == '__main__':
    print(reverse_string("GeEks"))
