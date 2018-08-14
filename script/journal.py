import datetime, os
from subprocess import call

def write_header_with_bullet_points(markdown_file, header_text):
    markdown_file.write("\n## " + header_text + "\n")
    for i in range(3):
        markdown_file.write("* \n")

if __name__ == "__main__":
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    current_path = os.path.dirname(os.path.realpath(__file__))
    morning_path = os.path.join(current_path, "../morning/")
    path = morning_path + date + ".md"

    markdown_file = open(path, "w+")

    markdown_file.write("# " + date + " Morning Journal\n")

    write_header_with_bullet_points(markdown_file, "Today I'm grateful for:")
    write_header_with_bullet_points(markdown_file, "Today's focus is:")

    markdown_file.close()

    call(["code", morning_path])
