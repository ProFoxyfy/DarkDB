If you've installed through the DarkDB Installer, the import line is the same.
# Recent Changes in 1.1
- Added 3 new functions
- Fixed bug where reading as a table could cause a row with None to appear
- Added cachebust to updater (fixes certain issues)

=======

# Why?

Because why not! I originally created this project for future things.

# How?

Well, Python of course. Even though its slow, its enough for a custom client-side database engine.

# How do i use it?

Its simple.
You also need to put the DarkDB source files in your source directory, 

```python
import darkdb
darkdb.makeDatabase("mydatabase.db")
# add some example
darkdb.addRow("MyRowName","MyRowValue","mydatabase.db")
# remove that example
darkdb.removeRow("MyRowName","mydatabase.db")
# read all lines as string
print(darkdb.dbAsString("mydatabase.db"))
```

If you want to delete a database simply just rm -rf the whole thing!
Its not hard.

# Pros and Cons

## Pros
 - Easy to use
 - Automatically saves beetween actions
 - Can save to a file
 
## Cons
 - Does'nt support server-side without modifications.
 - No snapshot beetween saves
 - Only supports Python
