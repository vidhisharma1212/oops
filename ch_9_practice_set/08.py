with open('content.txt') as f:
    content= f.read()
    with open('this_is_copy_of_content.txt','w') as j:
        j.write(content)