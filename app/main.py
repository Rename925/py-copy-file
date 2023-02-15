def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        _, current_file, future_file = command.split()
        if current_file != future_file:
            with (
                open(f"{current_file}", "r") as file,
                open(f"{future_file}", "w") as file_copy
            ):
                file_copy.write(file.read())

