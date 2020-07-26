import os
if os.path.exists("goku.txt"):
	os.remove("goku.txt")
else:
	print("the file does not exist")

