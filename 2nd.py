# Replace 'filename.txt' with your actual file path
file_path = 'filename.txt'

with open(file_path, 'r') as file:
    content = file.read()
    print(content)