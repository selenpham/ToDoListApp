# To-Do List APP
# Tạo list rỗng để chứa các todo sẽ nhập sau đó

# todos = []
#Sử vòng lặp True để lặp liên tục

while True:
    user_action = input("Type add, show,edit, complete or exit: ")
    user_action = user_action.strip() # loại bỏ khoảng trắng

# Người dùng chỉ được nhập các action theo gợi ý, nếu khác thì sẽ hiện warning
    match user_action:
        case 'add' :
            todo= input("Enter a todo:")+"\n"
# input nhập vào được ghi vào file todos.txt
            file = open(r"D:\60daysPython\Day1\Day2\todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open(r"D:\60daysPython\Day1\Day2\todos.txt", "w")
            file.writelines(todos)
            file.close()
        case 'show':
            file = open(r"D:\60daysPython\Day1\Day2\todos.txt", "r")
            todos = file.readlines()
            file.close()

            # new_todos = [item.strip("\n") for item in todos]
            
            for index, item in enumerate(todos):  # tạo thứ tự cho list todo đã nhập vô
                item = item.title()
                item =item.strip("\n")
                row = f"{index+1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number -1
            new_todo =input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number-1)
        case 'exit':
            break
        case whatever:
            print("\t Hey, you entered unknown command")
# Chọn exit thì thoát chtr và in Bye
print("Bye")
