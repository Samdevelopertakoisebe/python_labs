def check_validity(rec):
    if not isinstance(rec, tuple):
        raise TypeError('Not a tuple')
    if not isinstance(rec[0], str) or not isinstance(rec[1], str):
        raise TypeError('Not a string')
    if not isinstance(rec[2], float):
        raise TypeError('Not a float')
    if len(rec[0]) == 0 or len(rec[1]) == 0:
        raise ValueError('Empty name/group')

def initials(name):
    name = name.strip().split()
    if not 2 <= len(name) <= 3:
        raise ValueError('Not a valid name')
    extra = ''
    if len(name) == 3:
        extra = name[2][0].upper() + '.'
    return f'{name[0].capitalize()} {name[1][0].upper()}.' + extra

def format_record(rec):
    check_validity(rec)
    return f'{initials(rec[0])}, гр. {rec[1]}, GPA: {round(rec[2], 2)}'

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))