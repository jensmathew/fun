import typer

app = typer.Typer()
a=[]

@app.command()
def list():
    print("1.add - Add a new item with priority no. and text  to the list")
    print("2.sorted - Show incomplete priority list items sorted by priority in ascending order")
    print("3.dele - Delete the incomplete item with the given priority number")
    print("4.done - Mark the incomplete item with the given PRIORITY NUMBER as complete")
    print("5.help - Show usage")
    print("6.report - Statistics")

@app.command()
def add():
    # a =[(a, input("Enter the task with priority (eg.55 To Drink Water) : "))]
    insertvalue = int(input("Enter the priority no. : "))
    inserttext = input("Enter the task : ")
    a.insert(insertvalue, inserttext)
    print(a)

@app.command()
def help():
    print("1.add - Add a new item with priority no. and text  to the list")
    print("2.sorted - Show incomplete priority list items sorted by priority in ascending order")
    print("3.dele - Delete the incomplete item with the given priority number")
    print("4.done - Mark the incomplete item with the given PRIORITY NUMBER as complete")
    print("5.help - Show usage")
    print("6.report - Statistics")

@app.command()
def sorted():
    print(a)

@app.command()
def dele():
    b = int(input("enter the position to delete: "))
    global c
    c = a[b]
    del a[b]
    print(a)

@app.command()
def report():
    print("Pending : ")
    print(c)
    print("Completed : ")
    print(e)

@app.command()
def done():
    d = int(input("enter the position to be marked as done: "))
    global e
    e = a[d]
    del a[d]
    print(a)

@app.command()
def start():
    list()
    n = int(input("Enter the choice : "))
    if n == 1:
        add()

        start()
    elif n == 2:
        sorted()

        start()
    elif n == 3:
        dele()

        start()
    elif n == 4:
        done()

        start()
    elif n == 5:
        list()

        start()
    elif n == 6:
        report()

        start()
    else:
        print("Invalid Entry")

if __name__ == '__main__':
    app()