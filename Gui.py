from modules import functions
import PySimpleGUI as Sg
import time

Sg.theme("DarkBlue14")
clock = Sg.Text('', key="clock")
text = Sg.Text("Type in a To-do:")
input_box = Sg.InputText(tooltip="Enter To-do", key="todo")
add_button = Sg.Button("Add")
edit_button = Sg.Button("Edit")
complete_button = Sg.Button("Complete")
exit_button = Sg.Button("Exit")
list_box = Sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])


window = Sg.Window("To-do App",
                   layout=[[clock],
                           [text],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 12))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b/%d/%Y - %H:%M"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                Sg.popup("Please select an item first.", font=("Helvetica", 12))

        case "todos":
            window['todo'].update(value=values['todos'][0])
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                Sg.popup("Please select an item first.", font=("Helvetica", 12))
        case "Exit":
            break

        case Sg.WIN_CLOSED:
            break

window.close()
