import datetime, os
from subprocess import call

def write_header_with_bullet_points(markdown_file, header_text):
    markdown_file.write("\n## " + header_text + "\n")
    for i in range(3):
        markdown_file.write("* \n")

def write_header(markdown_file, header_text):
    markdown_file.write("\n## " + header_text + "\n\n")

def create_file(folder, title):
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    current_path = os.path.dirname(os.path.realpath(__file__))
    full_path = os.path.join(current_path, folder)
    path = full_path + date + ".md"
    markdown_file = open(path, "w+")
    markdown_file.write(f"# {date} {title} Journal \n")
    return full_path, markdown_file

def complete(markdown_file, path):
    markdown_file.close()
    call(["code", path])

