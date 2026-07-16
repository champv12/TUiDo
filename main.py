import json
from pathlib import Path
import typer

# initialize the Typer app
app = typer.Typer()

# define the path to the todo.json file
DATA_FILE = Path(__file__).with_name("todo.json")

# loads todo.json as python object
def load_lists():
    if not DATA_FILE.exists():
        return {}

    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)

#in-memory data
lists = load_lists()

#saves in-memory data to todo.json
def save_lists():
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(lists, file, indent=4)

@app.command()
def create_list(name: str):
    for list_name in lists:
        if name == list_name:
            print(f"List '{name}' already exists.")
            return
    else:
        lists[name] = []
        save_lists()
        print(f"List '{name}' created successfully.")

@app.command()
def delete_list(name: str):
    if not lists:
        print("no lists created")
    elif not name:
        print(f"list '{name}' not created")
    else:
        lists.pop(name)
        save_lists()
        print(f"list '{name}' deleted")

@app.command()
def show_lists():
    if not lists:
        print("no lists created")
    else:
        print("Lists:")
        for list_name in lists:
            print(f"- {list_name}")

#implement a show list func here!!!
#@app.command()
#def show_list(name: str):

@app.command()
def create_task(task: str, list_name: str):
    if not lists:
        create_list("inbox")
        lists["inbox"].append(task)
        print(f"Task '{task} created and added to Inbox")
    elif list_name not in lists:
        create_list(list_name)
        lists[list_name].append(task)
        print(f"'{list_name}' list created")
        print(f"'{task}' task added to '{list_name}' list")

@app.command()
def delete_task(task: int, list_name: str):
    
if __name__ == "__main__":
    app()
