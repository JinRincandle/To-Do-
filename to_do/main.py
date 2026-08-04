import json
import os


def save(a):
    new_data=[a]
    try:
        with open("to_do/todo.json","r") as j_file:
            j_data = json.load(j_file)
    except (FileNotFoundError, json.JSONDecodeError):
        j_data = []

    j_data.append(new_data)

    with open("to_do/todo.json", "w") as j_file:
            json.dump(j_data, j_file, indent=2)
            print("The task has been Added")

def show():
    q=1
    try:
        with open("to_do/todo.json","r") as j_file:
            j_data = json.load(j_file)
            for i in j_data:
                c="".join(i)
                print(q,c)
                q+=1
    except:
        print("To Do List Is Empty")

def remove(b):
    try:
        with open("to_do/todo.json","r") as j_file:
            j_data = json.load(j_file)
            for i in j_data:
                if [b] == i:
                    j_data.remove(i)

                    with open ("to_do/todo.json","w") as j_file:
                        json.dump(j_data,j_file,indent=2)
                        print("The task has been Removed")
                        return
            print("No Such Task Found")
                    
    except (FileNotFoundError, json.JSONDecodeError):
        print("To Do List Is Empty")



while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("="*40)
    print("TO DO LIST")
    show()
    print("="*40)
    
    x= int(input("1. Add to list: \n2. Remove from list\n3. To Exit\n"))

    if x == 3:
        exit()

    elif x == 1:
        add= input("Add the Task:\n")
        save(add)
        
    elif x == 2:
        re = input("which task to remove:\n")
        remove(re)
        

