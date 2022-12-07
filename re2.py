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
# print the list of containing all the
import re
s="The rain in spain"
t=re.findall("ai",s)
print(t)
# search function returns the match object if ther e is a match. if there is more match then
s="The rain in spain"
t=re.search("\s",s)
print("The first occurnce=",t.start())
# we want to spaces the white spaces
m=re.sub("\s","-",s,1)
print(m)
''' the split function returns the '''