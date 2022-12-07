#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Dell
#
# Created:     07-12-2022
# Copyright:   (c) Dell 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
# meta charchter
'''rectangular bracket(mt)
'''
import re
s="India is an asian country"
t=re.findall("[a-m]",s)
print(t)
s="hello world"
t=re.search("world$",s)
if t:
    print("Match  found")
else:
    ("not found")
    #dot character
s="hello world"
t=re.findall("he.+o",s)
print(t)
# curly basices meta character adjcetly spcified
# search for a sequence adjcetly two character
s="hello world"
t=re.findall("he.{2}o",s)
print(t)
