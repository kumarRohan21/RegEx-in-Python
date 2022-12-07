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
s='The country is spain'
t=re.search("^The .*spain$",s)
print(t)
if t:
    print('Yes found')
else:
    print('not found')
