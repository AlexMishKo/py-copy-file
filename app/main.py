def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    origin_filename = command.split()[1]
    copy_filename = command.split()[2]
    if origin_filename == copy_filename:
        return

    try:
        with (open(origin_filename, "r") as file_in,
              open(copy_filename, "w") as file_out):
            content = file_in.read()
            file_out.write(content)
    except FileNotFoundError:
        pass
