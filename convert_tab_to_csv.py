"""Converts a tab delimited file to a CSV
BASH FORMAT: $ python convert_tab_to_csv.py input_file.txt output_file.csv
Will OVERWRITE existing output file if one is present.
NOTE: Will wrap fields in quotes to prevent comma-interference if
      commas exist within fields"""

from sys import argv

input_file, output_file = argv[1:]

fin = open(input_file, 'r')
fout = open(output_file, 'w')

line_no = 1
current_line = fin.readline()

while current_line != "":

    print "{:0>4} | TAB $ {!r}".format(line_no, current_line)

    current_line_tabs = '"' + current_line.replace('\t', '","')
    current_line_out = current_line_tabs.replace('\n', '"\n')
    # Encapsulates all fields in quotes and replaced tabs with commas
    # The reason for this, is that commas WITHIN fields will break
    # the CSV import unless the fields are quoted.

    print "{:0>4} | CSV $ {!r}\n".format(line_no, current_line_out)

    fout.write(current_line_out)
    line_no += 1

    current_line = fin.readline()


print "DONE. {} (TAB-delimited) written to {} (CSV)".format(
      input_file, output_file)
fin.close()
fout.close()
