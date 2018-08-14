from journal import write_header, write_header_with_bullet_points, create_file, complete

if __name__ == "__main__":
    evening_path, markdown_file = create_file("../evening/", "Evening")

    write_header(markdown_file, "Today I felt:")
    write_header(markdown_file, "How I did on my goals:")
    write_header_with_bullet_points(markdown_file, "Today I'm grateful for:")

    complete(markdown_file, evening_path)
