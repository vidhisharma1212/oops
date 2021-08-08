content= True
i= 0
with open('content.txt') as f:
    
    while content:
        content= f.readline().lower()
        i +=1
        if 'python' in content:
            print('yes python is present')
            print('line=', i)