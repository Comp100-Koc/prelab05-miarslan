def is_repeating(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False
 



def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    """
    for i in range(len(s)):
        for j in range(i,len(s)):
            substring = [i:j]
            if is_repeating(substring):
                s=s.remove(substring)
    """
    while is_repeating(s):
        result = ""
        for i in range(len(s)):
            
            # if the current character is equal to the next character
            if i < len(s)-1 and s[i] == s[i+1]:
                
                # add the rest of the string to the result
                result += s[i+2:]
                
                # break the loop
                break
            else:
                # add the current character to the result
                result += s[i]
        
        # update the string
        s = result
        
    return s

          
          
            
            
        
    
    