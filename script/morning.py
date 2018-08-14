from journal import write_header_with_bullet_points, create_file, complete

if __name__ == "__main__":
    morning_path, markdown_file = create_file("../morning/", "Morning")

    write_header_with_bullet_points(markdown_file, "Today's focus is:")

    complete(markdown_file, morning_path)
