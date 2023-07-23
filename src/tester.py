import darkdb

try:
  darkdb.makeDatabase("unittest")
  print("Test 1: Success")
except:
  print("Test 1: Fail")
  assert False

try:
  darkdb.addRow("newrow","test","unittest")
  print("Test 2: Success")
except:
  print("Test 2: Fail")
  assert false

try:
  darkdb.changeRow("newrow","NiceOne","unittest", True)
  print("Test 2: Success")
except:
  print("Test 2: Fail")
  assert false

try:
  assert darkdb.dbAsString("unittest")
  print("Test 3: Success")
except:
  print("Test 3: Fail")

try:
  assert darkdb.dbAsTableOfRows("unittest")
  print("Test 4: Success")
except:
  print("Test 4: Fail")
