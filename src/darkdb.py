import reader


# makes a usable data base file
def makeDatabase(filename):
    open(filename, "w").write("")


# appends a row to the database
def addRow(name, value, filename):
    _newRow = reader.Row()
    _newRow.Name = name
    _newRow.Value = value

    reader.saveTable([_newRow], filename, False)


# removes a row from the database by name
# if you want to do it by value youll have to look into 'removeRowByVal'
def removeRow(name, filename):
    _contents = reader.readDbAsTable(filename)
    for row in _contents:
        if row.Name == name:
            row.Name = "TOBEDELETED"
            row.Value = "TOBEDELETED"

    reader.saveTable(_contents, filename, True)


# removes a row from the database by value
# if you want to do it by name youll have to look into 'removeRow'
def removeRowByVal(value, filename):
    _contents = reader.readDbAsTable(filename)
    for row in _contents:
        if row.Value == value:
            row.Name = "TOBEDELETED"
            row.Value = "TOBEDELETED"

    reader.saveTable(_contents, filename, True)


# converts a table of rows into a table of strings
# before:
# [[Row at XXXXXXXX, Row at XXXXXXXX]]
# after:
# [['Hi!','Hello World!'],['Bye!','Good Night!']]
def dbRowsAsStringTable(table):
    _contents = table
    _newTable = []
    for row in _contents:
        _newTable.append([row.Name, row.Value])

    return _newTable


# changes a row by name
def changeRow(name, newValue, filename, overwrite):
    _contents = reader.readDbAsTable(filename)
    for row in _contents:
        if row.Name == name:
            row.Value = newValue

    reader.saveTable(_contents, filename, overwrite)


# returns the db in its original format
def dbAsString(filename):
    return open(filename, "r").read()


# returns db as a table of Row objects
# see reader.py
def dbAsTableOfRows(filename):
    return reader.readDbAsTable(filename)
