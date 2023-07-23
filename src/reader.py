# format:
# name:value;
# anotherName:anotherValue;
#
# this means that for the name or value, ":" and ";" are invalid characters.

class Row:
    Name = ""
    Value = None


def readDbAsTable(filename):
    result = []
    file = open(filename, "r")
    lines = file.read().split(";")

    for stri in lines:
        _newrow = Row()
        _splitstr = stri.split(":")

        if _splitstr.__len__() > 1:  # if the length is lower than 2 we think it's a newline
            _newrow.Name = _splitstr[0]
            _newrow.Value = _splitstr[1]

        result.append(_newrow)

    return result


def saveTable(table, filename, overwrite):
    content = ""

    for row in table:
        if row == None or row.Value == None or row.Name == None:
            continue

        content += row.Name + ":" + row.Value + ";"
        content += "\n"

    currentWriteMode = "a"
    if overwrite:
        currentWriteMode = "w"

    newFile = open(filename, currentWriteMode)
    newFile.write(content)
