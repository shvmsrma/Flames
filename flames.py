print('Welcome to Flames')
name1 = raw_input("Enter Your name: ")
name2 = raw_input("Enter name of your counterpart: ")


def flames(fname,sname):
    fname = name1
    sname = name2
    joined_name = fname+sname
    name11 = []
    name21 = []
    name11 = fname.split()
    name21 = sname.split()
    for i in range(0,len(name11)):
        for j in range (0,len(name21)):
            final_strings = []
            if(name11[i] != name21[j]):
                final_strings.append(name11[i])
                final_strings.append(name21[j])
            else:
                final_strings.append(name11[i])
        return final_strings
    print(final_strings)
    length_finalstring = len(final_strings)
    my_list = ['F','L','A','M','E','S']
    count = 1
    while(count<len(final_strings)):
        delete = length_finalstring % len(my_list)
        del my_list[delete]
        count = count+1
        return my_list

result = flames(name1,name2)
print(name1 + ' your FLAMES result with ' + name2 + ' is ' + str(my_list))
