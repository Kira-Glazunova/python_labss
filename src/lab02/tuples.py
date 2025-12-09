def format_record(rec: tuple[str, str, float]) -> str:
    name_data = rec[0].strip().split()
    if len(name_data) > 2:
        surname, name, patronymic = rec[0].strip().split()
        name_string = f"{surname[0].upper()}{surname[1:]} {name[0].upper()}.{patronymic[0].upper()}."
    elif len(name_data) == 2:
        surname, name = rec[0].strip().split()
        name_string = f"{surname[0].upper()}{surname[1:]} {name[0].upper()}."
    elif len(name_data) == 1:
        surname = rec[0].strip().split()
        name_string = f"{surname[0].upper()}{surname[1:]}"
    else:
        return ValueError

    group = rec[1].strip()
    if group == "":
        return ValueError

    if type(rec[2]) != float and type(rec[2]) != int:
        return "TypeError"
    else:
        gpa = float(rec[2])

    return f"{name_string}, гр. {group}, GPA {gpa:.2f}"
