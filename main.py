import typer

app = typer.Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}")

def create_list(name: str):
   name = []
   return name

@app.command()
def add_item(item: str, list_name:str)
    if list


if __name__ == "__main__":
    app()
