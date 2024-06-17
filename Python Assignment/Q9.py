main = input("enter string: ")
substring = input("enter substring: ")
ans = main.find(substring)
if(ans!=-1):
    print("present")
else:
    print("not present")