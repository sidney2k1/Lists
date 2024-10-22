def squaredvalues(beg,end):
    lst=[]
    for i in range(beg,end):
        lst.append(i**2)
    lsteven=[]
    lstodd=[]
    for i in lst:
        if i%2==0:
            lsteven.append(i)
        else:
            lstodd.append(i)
    print("Heres a list of even squared numbers within the specified range:",lsteven)
    print("Heres a list of odd squared numbers within the specified range:",lstodd)
beg=int(input("Enter the starting range:"))
end=int(input("enter the ending range:"))
squaredvalues(beg,end)