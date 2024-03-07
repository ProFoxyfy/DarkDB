# DarkDB Docs

## Functions

### makeDatabase()
```python
makeDatabase(filename : String)
```
Creates an empty database file. (acts as an file creator at the moment)
### addRow()
```python
addRow(name : String, value : String, filename : String)
```
Adds a row to the database specified within the filename argument.
### removeRow()
```python
removeRow(name : String, value : String, filename : String)
```
Removes a row from the database with specified name. *(note that with the way databases currently work names do not need to be unique)*
### removeRowByVal()
```python
removeRowByVal(value : String, filename : String)
```
Removes a row from the database with specified value.
### dbRowsAsStringTable()
```python
dbRowsAsStringTable(filename : String)
```
Returns the database in [name,value] format as a table.

e.g. 
> [['Hi!','Hello World!'],['Bye!','Good Night!']]
### changeRow()
```python
changeRow(name : String, newValue : String, filename : String, overwrite* : Boolean)
```
Changes a row from the database with specified name and new value.
### dbAsString()
```python
dbAsString(filename : String)
```
Returns the database in plaintext format.
### dbAsTableOfRows()
```python
dbAsTableOfRows(filename : String)
```
Returns the database in Row format as a table.

" * " = Deprecated

## Additional Notes
changeRow() currently has an changeable overwrite parameter. This will be removed in the future.
