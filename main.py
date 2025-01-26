from tkinter import Tk
from gui.display import Display
from gui.keypad import Keypad
from core.parser import Parser


def main() -> None:
    root = Tk()

    root.title('Calculator')

    root.geometry('280x400')
    root.resizable(False, False)

    display = Display(root)
    keypad = Keypad(root)
    parser = Parser()

    def get_result(display: Display, parser: Parser):
        result = parser.parse(display.get_string())
        return str(result).rstrip("0").rstrip(".").replace('-', '−')

    key_map = {
        "<": lambda: display.move_cursor(-1),
        ">": lambda: display.move_cursor(1),
        "DEL": display.delete_char,
        "CLS": display.clear_string,
        "7": lambda: display.insert_char("7"),
        "8": lambda: display.insert_char("8"),
        "9": lambda: display.insert_char("9"),
        "+": lambda: display.insert_char("+"),
        "4": lambda: display.insert_char("4"),
        "5": lambda: display.insert_char("5"),
        "6": lambda: display.insert_char("6"),
        "−": lambda: display.insert_char("−"),
        "1": lambda: display.insert_char("1"),
        "2": lambda: display.insert_char("2"),
        "3": lambda: display.insert_char("3"),
        "×": lambda: display.insert_char("×"),
        "0": lambda: display.insert_char("0"),
        ".": lambda: display.insert_char("."),
        "^": lambda: display.insert_char("^"),
        "÷": lambda: display.insert_char("÷"),
        "(": lambda: display.insert_char("("),
        ")": lambda: display.insert_char(")"),
        "=": lambda: display.set_string(get_result(display, parser)),
        "OFF": quit,
        "sin": lambda: display.insert_char("sin"),
        "cos": lambda: display.insert_char("cos"),
        "tan": lambda: display.insert_char("tan"),
        "asin": lambda: display.insert_char("asin"),
        "acos": lambda: display.insert_char("acos"),
        "atan": lambda: display.insert_char("atan"),
        "π": lambda: display.insert_char("π"),
        "τ": lambda: display.insert_char("τ")
    }

    keypad.set_layout(key_map, 4, "column")
    keypad.draw_keys()

    display.pack(fill = "both", expand = True)
    keypad.pack(fill = "both", expand = True)
    
    root.mainloop()


if __name__ == '__main__':
    main()