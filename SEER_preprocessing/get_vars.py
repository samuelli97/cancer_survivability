'''
Parses the SEER documentation file to get variable names
and respective indices in the ASCII data
'''


f_input = open('read.seer.research.nov17.sas', 'r')
f_vars = open('vars.txt', 'w')

prev_end_index = None

# iterate through lines in documentation file
for l in f_input:
    # line contains variable
    if l[4] == '@':
        elements = l.split()
        var_begin_index = int(elements[1])
        var_name = elements[2]

        if prev_end_index != None:
            prev_index_length = var_begin_index - prev_end_index
            f_vars.write(str(prev_index_length) + "\n")


        f_vars.write(var_name + "\t")
        f_vars.write(str(var_begin_index) + "\t")
        prev_end_index = var_begin_index

f_vars.write("2\n")

#f_indices.close()
f_vars.close()
f_input.close()
