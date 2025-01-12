from dataclasses import dataclass
from collections.abc import Callable
from tkinter import (
    Tk,
    StringVar,
    Entry,
    Frame,
    Button
)
from operator import (
    add,
    sub,
    mul,
    truediv
)


@dataclass
class Function:
    body: Callable[[float, float], float]
    prec: int


func_tbl = {
    '+': Function(add, 1),
    '−': Function(sub, 1),
    '×': Function(mul, 2),
    '÷': Function(truediv, 2),
}


def parse(string: str) -> float:
    output = []
    stack = []

    ptr = 0
    end = len(string)

    while ptr < end:
        if string[ptr].isdigit() or string[ptr] == '.':
            base = ptr

            while ptr < end and (string[ptr].isdigit() or string[ptr] == '.'):
                ptr += 1

            if string[base:ptr].count('.') > 1:
                raise(ValueError)

            output.append(float(string[base:ptr]))
        elif string[ptr] in func_tbl:
            while stack and func_tbl[string[ptr]].prec <= stack[-1].prec:
                if len(output) < 2:
                    raise ValueError

                output.append(stack.pop().body(output.pop(-2), output.pop()))

            stack.append(func_tbl[string[ptr]])

            ptr += 1

    while stack:
        if len(output) < 2:
            raise ValueError

        output.append(stack.pop().body(output.pop(-2), output.pop()))

    if not output or len(output) > 1:
        raise ValueError

    return output[0]


def main() -> None:
    root = Tk()

    root.title('Calculator')

    root.geometry('300x400')
    root.resizable(False, False)

    disp_str = StringVar()

    disp = Entry(root, textvariable=disp_str, font=('Courier New', 18))
    disp.pack(pady=10)

    disp.focus()
    disp.bind('<KeyPress>', 'break')

    kpad = Frame(root)
    kpad.pack(fill='both', expand=True)

    for i in range(4):
        kpad.columnconfigure(i, weight=1)
    for i in range(5):
        kpad.rowconfigure(i, weight=1)

    for i, v in enumerate((
        '<', '>', 'DEL', 'CLS',
        '7', '8', '9', '+',
        '4', '5', '6', '−',
        '1', '2', '3', '×',
        '0', '.', '=', '÷'
    )):
        Button(kpad, text=v).grid(column=i % 4, row=i // 4, sticky='nsew')
 
    keys = kpad.winfo_children()
    
    keys[0].config(command=lambda : disp.icursor(disp.index('insert') - 1))
    keys[1].config(command=lambda : disp.icursor(disp.index('insert') + 1))
    keys[2].config(command=lambda : disp.delete(
        disp.index('insert') - 1,
        disp.index('insert')
    ))
    keys[3].config(command=lambda : disp_str.set(''))
    keys[18].config(command=lambda : (
            disp_str.set(str(parse(disp_str.get())).rstrip('0').rstrip('.')),
            disp.icursor('end')
    ))

    for key in keys:
        if key['command']:
            continue

        key.config(command=lambda x=key['text'] : disp.insert(
            disp.index('insert'),
            x
        ))
    
    root.mainloop()

    return


if __name__ == '__main__':
    main()