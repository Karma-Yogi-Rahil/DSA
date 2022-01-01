
""" Www.HackerRank.com → wWW.hACKERrANK.COM  """
def swap_case(s):
    word = ''
    for i in s:
        if(i.isupper())== True:
            word += i.lower()
        else:
            word += i.upper()
    return word

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)