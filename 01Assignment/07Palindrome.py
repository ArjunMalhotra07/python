givenString = (input("Enter a String "))
l = len(givenString)

def checkPalindrome(givenString, l):
    newString = ""
    for i in range(l-1, -1, -1):
        newString += givenString[i]

    print(newString)
    if newString != givenString:
        print("Not Palindrome")
    else:
        print("Palindrome")

checkPalindrome(givenString, l)