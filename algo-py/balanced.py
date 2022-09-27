def isBalanced(s):
    restart=True
    while restart:
        if '{}' in s:
            s=s.replace('{}','')
        elif '()' in s:
            s=s.replace('()','')
        elif '[]' in s:
            s=s.replace('[]','')
        else:
            restart=False
    return 'YES' if len(s)==0 else 'NO'

def isBalanced1(s):
    queue = deque(s)
    result_return = 'YES'
    
    while (queue):
    
        left_char = queue.popleft()
        right_char = queue.pop()
        
        if left_char + right_char not in ['{}', '[]', '()']:
            result_return = 'NO'
            break
    
    return result_return