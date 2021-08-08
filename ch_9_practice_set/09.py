# using files content. and this_is_copy_of_content to make this question
with open('content.txt') as f:
    c1= f.read()
with open('this_is_copy_of_content.txt') as k:
    c2= k.read()
'''
Method no . 1 by me-
'''
# c=[c1,c2]
# for i in c:
#     for n in c:
#         if c[i] is c[n]:
#             print(f"yes, content of {i} matches with {n}")

'''
method no. 2 by me-
'''
if c1==c2:
    print('yes, content is copied')
else:
    print('not copied')