def read_from_file(file_path):
    try:
        # Open the file
        with open(file_path, "r") as file:
            transcript = file.read()

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except IOError as e:
        print(f"Error occurred reading the file: {e}")
        return None

    return transcript


def save_content_to_file(file_path, content):
    try:
        with open(file_path, "w") as file:
            file.write(content)
    except IOError as e:
        print(f"Error occured while writing to the file {e}")
        return None
    except Exception as e:
        print("Unexpected error occured {e}")
        return None

    return content
