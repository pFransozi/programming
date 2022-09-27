def largest_rectangle(h):
    stack=[]
    area=0
    i=0
    while i<len(h):
        
        if not stack or h[stack[-1]]<=h[i]:
            stack.append(i)
            i+=1
           
        else:
            top=stack.pop()
            area=max(area,h[top]*(i-stack[-1]-1 if stack else i))
    
    while stack:
        top=stack.pop()
        area=max(area,h[top]*(i-stack[-1]-1 if stack else i))
        
    return area

#largest_rectangle = largest_rectangle([11, 11, 10, 10, 10])
largest_rectangle = [8979,4570,6436,5083,7780,3269,5400,7579,2324,2116]
print(largest_rectangle)