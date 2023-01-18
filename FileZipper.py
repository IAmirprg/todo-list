import PySimpleGUI as Sg

text1 = Sg.Text("Select files to compress:")
text2 = Sg.Text("Select destination folder:")
input_box1 = Sg.InputText()
input_box2 = Sg.InputText()
choose_button1 = Sg.FileBrowse("Choose")
choose_button2 = Sg.FolderBrowse("Choose")
compress_button = Sg.Button("compress")

window = Sg.Window("File Zipper", layout=[[text1, input_box1, choose_button1], [text2, input_box2, choose_button2],
                                          [compress_button]])
window.read()
window.close()


