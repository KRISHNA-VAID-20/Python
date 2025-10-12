txt_data= "I am varun vaid "

file_path = "C:/Users/krishna vaid/Desktop/varun.txt"
with open(file_path,"w") as file:
    file.write(txt_data)
    print(f"Text file {file_path} was created")