from tkinter import (
    Tk
)


def main() -> None:
    root = Tk()

    root.title('Calculator')
    
    root.geometry('300x400')
    root.resizable(False, False)

    root.mainloop()

    return


if __name__ == '__main__':
    main()