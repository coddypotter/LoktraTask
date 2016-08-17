#TASK 1
#Reverse Hash Program

#function to reverse hash
def reverseHash(n):
    letters = 'acdegilmnoprstuw' #refernce string
    result = ''
    strLen = str(n)
    n = int(n)
    i = 0
    while(len(strLen)>7):
        i = i+1
        result = letters[n%37] + result
        n=n/37
        if i == 7: #7 because in problem statement it has been given 7 letter string
            break
    
    return result

reverse = reverseHash('680131659347')
print(reverse)
