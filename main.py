import typer

app = typer.Typer()

lists = []


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def create_list(name: str):
    lists.append(name)
    print(f"list {name} created")


# @app.command()
# def add_item(item: str, list_name:str)
#     if list


if __name__ == "__main__":
    app()
