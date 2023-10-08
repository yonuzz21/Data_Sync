import os
import shutil
import logging

def message():
    return """
Welcome to my project!

The script does the folowing:
* Creates two folders that are always in sync(Production and Test)

* The modification commited in Test folder will be saved automatically after 1 minute,
  or by pushing to Production.

* You can find a log file inside Production, with all the changes made
"""

def menu():
    return   """
Use the menu below to navigate:

[1]Add Test Data
[2]Edit Test Data
[3]Show Path
[0]Exit
"""

def exit_script():
    return """

Thank you for using the interface!
Have a great day! :D

"""

def push_production():

  """ Function to transfer the Test data to Production """

  try:
    source = os.path.join(_test_path, "text.txt")
    destination = os.path.join(_prod_path, "text.txt")
    shutil.copy(source,destination)
    print("\n[!] Files were transfered!")
    
  except FileNotFoundError:
    try:
     os.remove(destination) 

    except FileNotFoundError:
     print("\n[!] No files exist.")
    

def folder_creation():
    """ This function creates the Test with text.txt file and Production folder. """
    
    try:
     global _prod_path, _test_path, _text_path
     _prod = "Production"
     _test = "Test"
     
     _prod_path = os.path.join(desktop_path, _prod)
     _test_path = os.path.join(desktop_path, _test)
     _text_path = os.path.join(_test_path,"text.txt")
     
   
     os.mkdir(_prod_path)
     os.mkdir(_test_path)
     open(_text_path,"+a")
     

     print(f"""
[*] Production folder initialized at: {_prod_path}
[*] Test folder initialized at: {_test_path}

""")
     

    except FileExistsError:
     print(f"""
[*] Production folder initialized at: {_prod_path}
[*] Test folder initialized at: {_test_path}

""")



def show_folder():
   try:
    print(desktop_path)
   except NameError:
    print("\n[!] Please create a folder before!")





desktop_path = os.getcwd()
print(desktop_path)
folder_creation()
logging.basicConfig(filename="logs.txt", 
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s %(levelname)-8s %(message)s')
logging.info("[!] Folders and Test file created!")
print(message())

while True: 

    print("==================================================")
    print(menu())
    
    menu_select = input("Select: ")
 
    while True:
      
      if menu_select == "1": #Add Test
        _list =[]
       
       
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        age = input("Age: ")
        
        _list.append(f"Name:{first_name}|Last Name:{last_name}|Age:{age}\n")
        
        handle = open(_text_path,"+a")
        for item in _list:
         handle.write(item)
         handle.close()
         logging.basicConfig(filename="logs.txt", 
                             level=logging.INFO,
                             datefmt='%Y-%m-%d %H:%M:%S',
                             format='%(asctime)s %(levelname)-8s %(message)s')
         logging.info(f"[NEW] {_list} !")
        push_production()
        break
        
       
      elif menu_select == "2":
        items = open(_text_path, "r+")
        item_list = list(items)  

        for nr, item in enumerate(item_list):
         print([nr], item)

        select = input("Select item to delete or <enter> to exit: ")
        if select.isdigit() and int(select) < len(item_list):
          item_list.pop(int(select)) 
          items.seek(0) 
          items.truncate()  

        
          items.write("".join(item_list))
          items.close()  
          push_production()
          logging.basicConfig(filename="logs.txt", 
                              level=logging.INFO,
                              datefmt='%Y-%m-%d %H:%M:%S',
                              format='%(asctime)s %(levelname)-8s %(message)s')
          logging.info(f"[Deleted] [{nr} | {item}]")
          break

        elif select == "":
          break

        else:
         print("\n=====================")
         print("Invalid selection!")
         print("=====================\n")
       
      elif menu_select == "3":
          print("==================================================")
          print("Folder can be found at:")
          show_folder()
          break
       
      elif menu_select == "0":
          print(exit_script())
          input("Press <enter> to exit.")
          exit()
      
      else:
         print("==================================================")
         print("Invalid Choice!")
         break
