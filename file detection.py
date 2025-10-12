import os

file_path = "test.txt"

if os.path.exists(file_path):
    print(f"That location '{file_path}' exists !")
    

else:
    print("That location doesn't exists !")
