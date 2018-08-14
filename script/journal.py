import datetime, os

import os

def write_header_with_bullet_points(flie, header_text):
    file.write("\n## " + header_text + "\n")
    for i in range(3):
        file.write("* \n")

date = datetime.datetime.today().strftime('%Y-%m-%d')
current_path = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(current_path, "../morning/") + date + ".md"

file = open(path, "w+")

file.write("# " + date + " Morning Journal\n")

write_header_with_bullet_points(file, "Today I'm grateful for:")
write_header_with_bullet_points(file, "Today's focus is:")

file.close()
