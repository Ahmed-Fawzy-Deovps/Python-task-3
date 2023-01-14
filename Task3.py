def isBalanced (s: str) -> bool:  # created a function with string as input and boolean check.
    stack = []       # stack to contain data
    # dictionary to be checked later in for loop.
    closetopen = {")": "(", "]": "[", "}": "{"}
    for b in s:  # for loop control variable (b) to search in strings .
        # if (b) is in dictionary (closetopen) that contains all the brackets.
        if b in closetopen:
            # if the stack is not empty and to take the last item in it also to check if it is contained inside the dictionary
            if stack and stack[-1] == closetopen[b]:  
                 stack.pop()
            else: #if else it will return false to us
                return False

        else:
            stack.append(b) #to add the brackets in the stack
    return True if not stack else False #true if the brackets is in the stack or false if not


print (isBalanced("{()}")) 
