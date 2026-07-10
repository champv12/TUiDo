import json
from pathlib import Path
import typer

# initialize the Typer app
app = typer.Typer()

# add json implementation here
# lists = []

@app.command()
def create_list(name: str):
    if name in lists:
        print(f"List {name} already exists.")
    else:
        lists.append(name)
        print(f"List {name} created.")

@app.command()
def show_lists(name: str | None = None):
    if not lists:
        print("no lists created")
    else:
        print("Lists:")
        for list_name in lists:
            print(f"- {list_name}")


if __name__ == "__main__":
    app()
