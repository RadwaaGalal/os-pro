
import os
import sys
import shutil
from Virtual_Disk import virtual_disk
from Fat_Table import Fat
from Directory_Entry import Directory_Entery
from Directory import directory
from File_entry import file_entry

commands={
"cd": "      - Change the current default directory to.\n           If the argument is not present, report the current directory.\n           If the directory does not exist an appropriate error should be reported.",
"cls" : "     - Clear the screen.",
"dir":"     - List the contents of directory",
"exit":"    - Quit the shell.",
"copy": "    - Copies one or more files to another location.",
"del":"     - Deletes one or more files.",
"help":"    - Provides Help information for commands.",
"md":"      - Creates a directory.",
"rd":"      - Removes a directory.",
"rename":"  - Renames a file.",
"type":"    - Displays the contents of a text file.",
"import":"  - import text file(s) from your computer.",
"export":"  - export text file(s) to your computer."
}
command = ' '
while(command != "exit"):
 print("\n")
 current_path = os.getcwd()
 print(os.getcwd() , end=" ")
 command = input()
 lst = command.split()
 lst[0] = lst[0].lower()
 if not (lst[0] in commands.keys()): #if command not exist
    print(f"{command} this command is not supported ")
 else:
    if ((lst[0]=="help") and (len(lst)==1)):#1-help command
       for i in commands.keys(): 
           print(f"{i} {commands[i]}")
    elif((lst[0]=="help") and (len(lst)==2)): 
           if (lst[1] in commands.keys()):  
              print(f"{lst[1]} {commands[lst[1]]}")
       
           else: 
              print(f"{lst[1]} this command is not supported by the help utility") 
 
    elif(lst[0]=="cls" and len(lst)==1):#2-Clear Screen
           os.system('CLS')   

    elif(lst[0]=="cd" and len(lst)==1):#3-Change Directory
           print(os.getcwd())
    elif(lst[0]=="cd" and len(lst)>1):  
           if os.path.exists(lst[1]): 
              os.chdir(lst[1])

   # elif(lst[0]=="exit" and len(lst)==1):#4-Exit
        #exit(0)
    #elif(lst[0]=="exit" and len(lst)>1):
        #print("eroor")

    elif(lst[0]=="dir" and len(lst)==1):#5-List of content
           print(os.listdir(current_path)) 

    elif(lst[0]=="copy" and len(lst)==1):#6-copy file
           print("ERROR:\nCopies one or more files to another location.\ncopy command syntax is\n     copy [source]\nor\n     copy [source] [destination]\n[source] can be file Name (or fullpath of file) or directory Name (or fullpath of directory)\n[destination] can be file Name (or fullpath of file) or directory name or fullpath of a directory")

    elif(lst[0]=="copy" and len(lst)==2):
           if not os.path.exists(lst[1]): 
              print(f"this file: {lst[1]} isn't exist in your disk")
           elif(lst[1]== current_path):
               print("The file can't be copied onto itself")
           elif(lst[1] !=  current_path):
              shutil.copy(lst[1],current_path)
              print(f"file {lst[1]} copied successfully")

    elif(lst[0]=="rename" and len(lst)==1):#7-Rename File
            print("ERROR:\nRename a file.\nrename command syntax is\n rd [fileName] [new fileName]\n[fileName] can be a file name or fullpath of a filename\n[new fileName] can be a new file name not fullpath")
    elif(lst[0]=="rename" and len(lst)==3):
           if not os.path.exists(lst[1]): 
               print("ERROR path not found")
           else:
               if  os.path.exists(lst[2]): 
                   print("A duplicate file name exists!")
               else:
                   os.rename(lst[1], lst[2])
                   print("Done Sucessfully")

    elif(lst[0]=="del" and len(lst)==1):#8-Delet one or more file
           print("ERROR:\nDelet one or more files.\nNOTE: it confirms the user choice to delete the file before deleting\ndel command syntax is\ndel [dirFile]+\n+ after [dirfile] represent that you can pass more than file Name (or fullpath of file) or directory name (or fullpath of directory)\n[dirfile] can be file Name (or fullpath of file) or directory name (or fullpath of directory).")
    elif(lst[0]=="del" and len(lst)>1):
         lst.remove('del')
         for i in lst:
           if os.path.exists(i):
               confirm = input(f"Are You Sure That You Want to delet {i} , if yes enter y or enter n for no: ")
               if(confirm=='y'):
                   if os.path.isdir(i):
                        shutil.rmtree(i) 
                   elif os.path.isfile(i):
                      os.remove(i)
                   print(f"{i} deleted successfully")
           else: print("ERROR: path not found!")

    elif(lst[0]=='md' and len(lst)==1):#9-make Directory
         print("ERROR:\nCreate Directory\nmd command syntax is\nmd [directory]\n[directory] can be a new directory name or fullpath of a new directory")
    elif(lst[0]=='md' and len(lst)==2):
           if not os.path.exists(lst[1]): 
                 os.mkdir(lst[1]) 
           else: print(f"ERROR: This directory {list[1]} is already exists!")


    elif(lst[0]=='rd' and len(lst)==1):#Remove Directory
           print("ERROR:\nRemove Directory\nNOTE: it confirms the user choice to delete the directory before deleting\nrd command syntax is\nrd [directory]+\n[directory] can be a directory name or fullpath of a directory\n+ after [directory] represent that you can pass more than directory name (or fullpath of directory")
    elif(lst[0]=='rd' and len(lst)>1):
         lst.remove('rd')
         for i in lst:
           if not os.path.exists(i): 
                print(f"ERROR: This directory {i} isn't exist!")  
           else: 
               if not (os.listdir(i) ):
                    os.rmdir(i) 
               else:
                   print("ERROR: This folder isn't empty!")

    elif(lst[0]=='type' and len(lst)==1):#Type
             print('ERROR:\nType:\nDisplays the contents of a text file.\ntype command syntax is\ntype [file]+\nNOTE: it displays the filename before its content for every file\n[file] can be file Name (or fullpath of file) of text file\n+ after [file] represent that you can pass more than file Name (or fullpath of file).')
    elif(lst[0]=='type' and len(lst)>1):
         lst.remove('type')
         for i in lst:
           if not os.path.exists(i):
                print(f"ERROR: This file {i} isn't exist!")  
           else: 
               if os.path.isdir(i):
                   print("Error this is not a file name or access is denied")
               elif os.path.isfile(i):
                      file_content=open(i)
                      print(file_content.read())

o=virtual_disk()
o.write()
ob=Fat() 
ob.initil()
ob.write_cluster()
ob.file()
#print(ob.read_cluster())
ob.get_avaliable_cluster()
ob.get_next(2)
obje=Directory_Entery('Os.txt','0x0')
