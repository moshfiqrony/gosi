import os

# get all icon name
my_file_list = sorted(os.listdir('.'))

# open readme file to write
my_txt = open('README.md', 'w')

# Write the title
my_txt.write("# google-official-svg-icons\n")

for file in my_file_list:
    if '.svg' not in file:
        continue
    str = '!['+file+']('+file+')\n'
    my_txt.write(str)

my_txt.close()