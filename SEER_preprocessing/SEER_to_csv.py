'''
Parses the pure ASCII SEER files into CSV format, using the
vars.txt file created by get_vars.py.
'''

import sys

if len(sys.argv) != 4:
    print('Usage: python SEER_to_csv.py \
    [begin flag ("t" or "f")] [input file] [output file]')
    exit(1)

f_input = open('../SEER_raw/' + sys.argv[2], 'r')
f_output = open('../SEER_parsed_csv/' + sys.argv[3], 'a')


with open('vars.txt', 'r') as f_vars:
    # read variable names, begin index, and length
    # print header row
    vars_and_indices = []
    for row in f_vars:
        info = row.split()
        info[1] = int(info[1])
        info[2] = int(info[2])
        vars_and_indices.append(info)
        if sys.argv[1] == "t":
            f_output.write(info[0]+",")
    if sys.argv[1] == "t":
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
