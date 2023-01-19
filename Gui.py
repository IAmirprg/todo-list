from modules import functions
import PySimpleGUI as Sg

text = Sg.Text("Type in a To-do:")
input_box = Sg.InputText(tooltip="Enter To-do", key="todo")
add_button = Sg.Button("Add")
edit_button = Sg.Button("Edit")
list_box = Sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])


window = Sg.Window("To-do App",
                   layout=[[text], [input_box, add_button], [list_box, edit_button]],
                   font=("Helvetica", 12))
while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "todos":
            window['todo'].update(value=values['todos'][0])






        case Sg.WIN_CLOSED:
            break



window.close()
