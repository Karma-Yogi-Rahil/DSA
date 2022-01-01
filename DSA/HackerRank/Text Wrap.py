"""
Sample Input 0
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output 0
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""
import textwrap
string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'

max_width = 4 


print(textwrap.fill(string,max_width))
        