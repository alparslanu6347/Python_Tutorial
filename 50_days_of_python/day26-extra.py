# s = 'Hi my name is Richard'
# Write a function called string_length that takes a string of
# words (words and spaces) as argument. This function should
# return the length of all the words in the string. Return the results
# in a form of a dictionary. The string above should return:
# {'Hi': 2, 'my': 2, 'name': 4, 'is': 2, 'Richard': 7}

def string_length(s):
    s=s.split()
    s_dict={}
    count=0
    for i in s:
        #print(i)
        s_dict[i]=len(i)
        #print(f"{i}: {len(i)}", end=",")
    print(s_dict)


s = 'Hi my name is Richard'
string_length(s)