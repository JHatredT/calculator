from calc import Calculator
from tkinter import Tk


def main() -> None:
    root = Tk()

    root.title('Calculator')

    root.geometry('300x400')
    root.resizable(False, False)

    calculator = Calculator(root)

    calculator.set_display()
    calculator.set_keypad(4, 5)
    calculator.set_key_command(0, calculator.decrement_cursor)
    calculator.set_key_command(1, calculator.increment_cursor)
    calculator.set_key_command(2, calculator.del_char)
    calculator.set_key_command(3, calculator.clear)
    calculator.set_key_command(18, calculator.get_result)
    calculator.set_default_keys()
    
    root.mainloop()

    return


if __name__ == '__main__':
    main()