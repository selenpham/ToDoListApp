# To-Do List APP
#Sử vòng lặp True để lặp liên tục

import functions
import time

now = time.strftime("b %d, %Y %H:%M:%S")

while True:
    user_action = input("Type add, show,edit, complete or exit: ")
    user_action = user_action.strip() # loại bỏ khoảng trắng

# Người dùng chỉ được nhập các action theo gợi ý, nếu khác thì sẽ hiện warning
    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()
        todos.append(todo+ "\n")

# cách khác ghi file không cần close file

        functions.write_todos(todos)


    elif user_action.startswith("show"):

        # with open(r"D:\60daysPython\Day1\Day2\todos.txt", "r") as file:
        #     todos = file.readlines()
        todos = functions.get_todos()
        
        # new_todos = [item.strip("\n") for item in todos]
        
        for index, item in enumerate(todos):  # tạo thứ tự cho list todo đã nhập vô
            item = item.title()
            item =item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number -1

            # with open(r"D:\60daysPython\Day1\Day2\todos.txt", "r") as file:
            #     todos =file.readlines()
            todos = functions.get_todos()

            new_todo =input("Enter new todo: ")
            todos[number] = new_todo + "\n"
            
            functions.write_todos(todos)
        
        except ValueError:
            print("Your command is not valid")
            continue

    
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            # with open(r"D:\60daysPython\Day1\Day2\todos.txt", "r") as file:
            #     todos =file.readlines()
            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo - {todo_to_remove} - was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print(" Command is not valid. Enter action again")
# Chọn exit thì thoát chtr và in Bye
print("Bye")
