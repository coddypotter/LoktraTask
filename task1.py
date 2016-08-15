#TASK 1
#Hash Program

#function to 
def hashString(str):
    h = 7
    letters = 'acdegilmnoprstuw' #refernce string
    for alphabet in str:
        h = (h * 37 + letters.index(alphabet)) #compute hash

    return h #Return the hash value

#call to the hashString Function
hString = hashString('leepadg')
print(hString) #Print the result.
