def help_me():
    print("""Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
    Special commands: !help !done""")


def done(previous_text):
    with open("output.md", "w") as file:
        file.write(previous_text)
    exit()


def plain():
    return f'{input("Text: ")}'


def bold():
    return f'**{input("Text:")}**'


def italic():
    return f'*{input("Text:")}*'


def header():
    while True:
        try:
            level = int(input("Level:"))
            if level not in range(1, 7):
                raise Exception
            else:
                break
        except Exception:
            print("The level should be within the range of 1 to 6")
    header_text = f'{level * "#"} {input("Text:")}\n'
    return header_text
#this is me


def link():
    return f'[{input("Label:")}]({input("URL:")})'


def inline_code():
    return f'`{input("Text: ")}`'


def new_line():
    return "\n"


def list_me(kind_of_list):
    text = ""
    while True:
        try:
            number_of_rows = int(input("Number of rows:"))
            if number_of_rows < 1:
                raise Exception
            else:
                for n in range(number_of_rows):
                    if kind_of_list == "unordered":
                        text += "* " + str(input(f"Row #{n + 1}:")) + "\n"
                    elif kind_of_list == "ordered":
                        text += f"{n + 1}. " + str(input(f"Row #{n + 1}:")) + "\n"
                return text
        except Exception:
            print("The number of rows should be greater than zero")


command_dict = {"plain": "plain()", "bold": "bold()", "italic": "italic()", "header": "header()", "link": "link()",
                "inline-code": "inline_code()", "new-line": "new_line()", "unordered-list": "list_me('unordered')",
                "ordered-list": "list_me('ordered')", "!help": "help_me()", "!done": "done(current_text)"}
current_text = ""

while True:
    # x = command_dict[input("Choose a formatter:")]
    try:
        current_text += eval(command_dict[input("Choose a formatter:")])
        print(current_text)
    except Exception:
        print("Unknown formatting type or command")
