FILEPATH = r"D:\60daysPython\Day1\TodosApp\todos.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file_local:
            todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath=FILEPATH):
     with open(filepath, "w") as file: 
            file.writelines(todos_arg) 


if __name__ == "__main__":
    # print(__name__)
    # print(type("__name__"))
    print("Hello")
    print(get_todos())