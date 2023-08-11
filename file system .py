import datetime

class File:
    def __init__(self, name, size, permissions):
        self.name = name
        self.size = size
        self.created = datetime.datetime.now()
        self.modified = datetime.datetime.now()
        self.permissions = permissions
        self.content = ""

    def read(self):
        return self.content

    def write(self, content):
        self.content = content
        self.size = len(content)
        self.modified = datetime.datetime.now()

class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.directories = []

    def create_file(self, name, size, permissions):
        file = File(name, size, permissions)
        self.files.append(file)
        return file

    def delete_file(self, name):
        for file in self.files:
            if file.name == name:
                self.files.remove(file)
                return True
        return False

    def list_files(self):
        if not self.files:
            print("No files in the directory.")
        else:
            for file in self.files:
                print(file.name)

    def create_directory(self, name):
        directory = Directory(name)
        self.directories.append(directory)
        return directory

    def delete_directory(self, name):
        for directory in self.directories:
            if directory.name == name:
                self.directories.remove(directory)
                return True
        return False

    def list_directories(self):
        if not self.directories:
            print("No subdirectories in the directory.")
        else:
            for directory in self.directories:
                print(directory.name)

class FileSystem:
    def __init__(self):
        self.root = Directory("root")

    def create_file(self, path, name, size, permissions):
        directory = self._get_directory(path)
        if directory:
            return directory.create_file(name, size, permissions)
        else:
            print("Directory not found.")
        return None

    def delete_file(self, path, name):
        directory = self._get_directory(path)
        if directory:
            return directory.delete_file(name)
        else:
            print("Directory not found.")
        return False

    def list_files(self, path):
        directory = self._get_directory(path)
        if directory:
            directory.list_files()
        else:
            print("Directory not found.")

    def create_directory(self, path, name):
        directory = self._get_directory(path)
        if directory:
            return directory.create_directory(name)
        else:
            print("Directory not found.")
        return None

    def delete_directory(self, path, name):
        directory = self._get_directory(path)
        if directory:
            return directory.delete_directory(name)
        else:
            print("Directory not found.")
        return False

    def list_directories(self, path):
        directory = self._get_directory(path)
        if directory:
            directory.list_directories()
        else:
            print("Directory not found.")

    def _get_directory(self, path):
        if path == "/":
            return self.root

        components = path.split("/")
        directory = self.root
        for component in components[1:]:
            found = False
            for sub_directory in directory.directories:
                if sub_directory.name == component:
                    directory = sub_directory
                    found = True
                    break
            if not found:
                return None
        return directory

def prompt_continue():
    response = input("Do you want to continue? (Y/N): ").lower()
    return response == "y"

# Example usage
fs = FileSystem()

while True:
    print("\n1. Create file")
    print("2. Write to file")
    print("3. Read file")
    print("4. Delete file")
    print("5. Create directory")
    print("6. Delete directory")
    print("7. List files")
    print("8. List directories")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == "1":
        name = input("Enter the file name: ")
        size = int(input("Enter the file size: "))
        permissions = input("Enter the file permissions: ")
        file1 = fs.create_file("/", name, size, permissions)
        if file1:
            print("Created file:", file1.name)
    elif choice == "2":
        name = input("Enter the file name: ")
        content = input("Enter the content to write: ")
        directory = fs._get_directory("/")
        if directory:
            file = None
            for f in directory.files:
                if f.name == name:
                    file = f
                    break
            if file:
                file.write(content)
                print("Content written to file.")
            else:
                print("File not found.")
        else:
            print("Directory not found.")
    elif choice == "3":
        name = input("Enter the file name: ")
        directory = fs._get_directory("/")
        if directory:
            file = None
            for f in directory.files:
                if f.name == name:
                    file = f
                    break
            if file:
                content = file.read()
                print("File Content:", content)
            else:
                print("File not found.")
        else:
            print("Directory not found.")
    elif choice == "4":
        name = input("Enter the file name: ")
        result = fs.delete_file("/", name)
        if result:
            print("File deleted successfully")
        else:
            print("File not found or unable to delete")
    elif choice == "5":
        name = input("Enter the directory name: ")
        directory = fs.create_directory("/", name)
        if directory:
            print("Created directory:", directory.name)
    elif choice == "6":
        name = input("Enter the directory name: ")
        result = fs.delete_directory("/", name)
        if result:
            print("Directory deleted successfully")
        else:
            print("Directory not found or unable to delete")
    elif choice == "7":
        fs.list_files("/")
    elif choice == "8":
        fs.list_directories("/")
    elif choice == "9":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")

    if not prompt_continue():
        print("Exiting...")
        break
