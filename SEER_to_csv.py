'''
Parses the pure ASCII SEER files into CSV format, using the
vars.txt file created by get_vars.py.
'''

f_input = open('COLRECT.TXT', 'r')
f_vars = open('vars.txt', 'r')
f_output = open('CSV_Data/COLRECT_csv.txt', 'w')

# read variable names, begin index, and length
# print header row
vars_and_indices = []
for row in f_vars:
    info = row.split()
    info[1] = int(info[1])
    info[2] = int(info[2])
    vars_and_indices.append(info)
    f_output.write(info[0]+",")
f_output.write("\n")

count=0
for instance in f_input:
    if count%50000 == 0:
        print(str(count) + " instances parsed")

    for _, var_index, var_length in vars_and_indices:
        # SEER data is 1-indexed, but python is 0-indexed
        val = instance[var_index-1:var_index-1+var_length]
        val = val.replace(" ", "")
        if not val.isspace():
            f_output.write(val)
        f_output.write(",")
    f_output.write("\n")
    count+=1

f_output.close()
f_input.close()
f_vars.close()
