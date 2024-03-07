# DarkDB Docs

## Functions

### makeDatabase()

    makeDatabase(filename : String)
Creates an empty database file. (acts as an file creator at the moment)
### addRow()

    addRow(name : String, value : String, filename : String)
Adds a row to the database specified within the filename argument.
### removeRow()

    removeRow(name : String, value : String, filename : String)
Removes a row from the database with specified name. *(note that with the way databases currently work names do not need to be unique)*
### removeRowByVal()

    removeRowByVal(value : String, filename : String)
Removes a row from the database with specified value.
### dbRowsAsStringTable()

    dbRowsAsStringTable(filename : String)
Returns the database in [name,value] format as a table.

e.g. 
> [['Hi!','Hello World!'],['Bye!','Good Night!']]
### changeRow()

    changeRow(name : String, newValue : String, filename : String, overwrite* : Boolean)
Changes a row from the database with specified name and new value.
### dbAsString()

    dbAsString(filename : String)
Returns the database in plaintext format.
### dbAsTableOfRows()

    dbAsTableOfRows(filename : String)
Returns the database in Row format as a table.

" * " = Deprecated

## Additional Notes
changeRow() currently has an changeable overwrite parameter. This will be removed in the future.
