# File Creation
def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("2nd line with numbers: 42\n")
            file.write("Third line ends here.\n")
        print("File created successfully.")
    except PermissionError:
        print("Permission denied to create file.")
    except Exception as e:
        print("An error occurred:", e)

# File Reading and Display
def read_file():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied to read file.")
    except Exception as e:
        print("An error occurred:", e)

# File Appending
def append_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1\n")
            file.write("Appending line 2\n")
            file.write("Appending line 3\n")
        print("File appended successfully.")
    except PermissionError:
        print("Permission denied to append file.")
    except Exception as e:
        print("An error occurred:", e)

# Main function
def main():
    create_file()
    read_file()
    append_file()

if __name__ == "__main__":
    main()
