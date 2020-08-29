
def largestPalindromeAtIndex(s,left,right):
    leftIndex = 0
    rightIndex = 0
    while left >=0 and right < len(s):
        if s[left] == s[right]:
            leftIndex = left
            rightIndex = right
        else:
            break
        leftIndex -= 1
        rightIndex += 1

    return (rightIndex - leftIndex + 1)

def longestPalindrome(s):
    start = 0
    end = 0
    for i in range(len(s)):
        lengthOddPalindrome = largestPalindromeAtIndex(s,i,i)
        lengthEvenPalindrome = largestPalindromeAtIndex(s,i,i+1)
        length = max([lengthOddPalindrome,lengthEvenPalindrome])
        if length > (end-start):
            start = i - ((length-1)/2)
            end = i + (length/2)
    return s[start:end+1]


print(longestPalindrome("BABCDBCCBD"))
