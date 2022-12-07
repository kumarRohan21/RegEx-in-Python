#-------------------------------------------------------------------------------
# Name:        module1
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
import re
s="The rain in India falls in autumn"
t=re.findall("falls|stays",s)
print(t)
 # round bracket it is capture as an round group
'''match funtion
it returns a match object if there
we want to find one or more digit strng'''
import re
s="abc123xyz"
t=re.fullmatch("abc\d+",s)
if t:
    print("match found")
else:
    print("not found")