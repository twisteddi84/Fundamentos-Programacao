def longestPrefixRepeated(s):
    count = 1
    n = s[0:count]
    m = s
    for i in s:
        m = m[1:]
        n = s[0:count]
        if n in m:
            count += 1
        else:
            count -= 1
            n = s[0:count]
            break
    return n


def main():
    s = input("String:")
    s = s.lower()
    print(longestPrefixRepeated(s))

main()
