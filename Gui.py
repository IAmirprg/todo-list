from modules import functions
import PySimpleGUI as Sg

text = Sg.Text("Type in a To-do:")
input_box = Sg.InputText(tooltip="Enter To-do", key="todo")
add_button = Sg.Button("Add")


window = Sg.Window("To-do App",
                   layout=[[text], [input_box, add_button]],
                   font=("Helvetica", 12))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case Sg.WIN_CLOSED:
            break


window.close()
