# from functions import get_todos, write_todos
from modules import functions
import time

print(f"it is {time.strftime('%b/%d/%Y - %H:%M')}")

while True:
    user_action = input("Type add , show ,edit , complete or  exit: ")
    user_action = user_action.lower()

    if user_action.startswith("add"):

        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo+"\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index,item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index+1}.{item}")

    elif user_action.startswith("edit"):

        try:
            number = int(user_action[5:])

            todos = functions.get_todos()

            new_todo = input("enter new to do:  ")
            todos[number-1] = new_todo + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("wrong command")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = functions.get_todos()
            number =(int(user_action[9:]))
            todo_to_remove = todos[number-1].strip("\n")

            todos.pop(number-1)

            functions.write_todos(todos)
            message = f"the {todo_to_remove} has been removed."
            print(message)
        except ValueError:
            print("wrong command")
            continue
        except IndexError:
            print("there is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("command is not valid!")

print("bye")
