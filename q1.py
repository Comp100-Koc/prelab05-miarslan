def is_palindrome(s):
    if len(s) == 0:
        return False
    
    elif len(s) == 1:
        return True
    
    else:
        if s[::-1]== s:
            return True
    
        
def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    
    
    longest = ""
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            substring = s[i:j]
            if is_palindrome (substring):
                if (len(substring) > len(longest)) and (len(substring)>1):
                    longest = substring
                    
    return longest
                
            
            