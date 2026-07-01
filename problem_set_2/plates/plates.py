def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6:
        if s.isalpha():
            return True
        if s.isalnum() and s[0:2].isalpha():
            for str in s:
                if str.isalpha():
                    s = s.replace(str, '')
                if str.isdigit():
                    break
            if s.isdigit() and str[0] != '0':
                    return True

# 两个字母开头
# 字母或者数字，最多6个
# 数字必须放末尾、第一个数字不能是0

main()
