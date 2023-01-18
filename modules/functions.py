FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read text file and return list of todos"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write to-do items in text files"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


