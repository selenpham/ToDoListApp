def get_todos(filepath=r"D:\60daysPython\Day1\TodosApp\todos.txt"):
    with open(filepath, "r") as file_local:
            todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_args,filepath=r"D:\60daysPython\Day1\TodosApp\todos.txt"):
     with open(filepath, "w") as file: 
            file.writelines(todos_args) 


if __name__ == "__main__":
    print(__name__)
    print(type("__name__"))
    print(get_todos())