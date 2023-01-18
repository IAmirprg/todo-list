from modules import functions
import PySimpleGUI as Sg

text = Sg.Text("Type in a To-do:")
input_box = Sg.InputText(tooltip="Enter To-do")
add_button = Sg.Button("Add")


window = Sg.Window("Todo", layout=[[text], [input_box, add_button]])
window.read()
window.close()
