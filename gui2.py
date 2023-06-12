import functions2
import PySimpleGUI as gui
import time

gui.theme("DarkGrey4")

# clock=gui.Text("", key="clock",color="red")
clock=gui.Text("", key="clock", font=("Helvetica", 12, "bold"), text_color="pink")


label  = gui.Text("Type in a to-do", font=("Helvetica", 12, "bold"), text_color="dark blue")
input_box = gui.InputText(tooltip="Enter todo", key= "todo")
add_button = gui.Button(size= 2 ,image_source="add.png",mouseover_colors="Yellow",
                        tooltip="Add Todo", key="Add")

list_box = gui.Listbox(values=functions2.get_todos(), key = "todos", 
                       enable_events=True, size=[45,10])
edit_button = gui.Button("Edit")
complete_button = gui.Button(size= 2 ,image_source="complete.png",mouseover_colors="Purple",
                        tooltip="Complete Todo", key="Complete")
exit_button = gui.Button("Exit")

window = gui.Window("My To-Do App", 
                    layout=[[clock],
                        [label],
                        [input_box, add_button],
                        [list_box, edit_button, complete_button],
                        [exit_button]],
                    font=('Helvetica',12))
while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos =functions2.get_todos()
            new_todo =values['todo'] +"\n"
            todos.append(new_todo)
            functions2.write_todos(todos)
            window["todos"].update(values = todos)

        case "Edit":
            try:
                todo_edit= values["todos"][0]
                new_todo = values["todo"]

                todos = functions2.get_todos()
                index = todos.index(todo_edit)
                todos[index] = new_todo
                functions2.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                gui.popup("Please select an item first!",font=("Helvetica",10))
        case "Complete":
            try:
                todo_complete = values['todos'][0]
                todos = functions2.get_todos()
                todos.remove(todo_complete)
                functions2.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(values='')
            except IndexError:
                gui.popup("Please select an item first!",font=("Helvetica",10))
        case "todos":
            window["todo"].update(value = values["todos"][0])
        case "Exit" :
            break
        case gui.WIN_CLOSED:
            break

window.close()