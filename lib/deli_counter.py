katz_deli = ["Ann", "Stella", "Sammy"]
def line(deli_line):
    if len(deli_line) == 0:
        print("The line is currently empty.")
    else:
        line_status = "The line is currently:"
        i = 0
        while i < len(deli_line):
            line_status += f" {i + 1}. {deli_line[i]}"
            i += 1
        print(line_status)
def take_a_number(deli_line, name):
    deli_line.append(name)
    print(f"Welcome, {name}. You are number {len(deli_line)} in line.")
def now_serving(deli_line):
    if not deli_line:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {deli_line.pop(0)}.")