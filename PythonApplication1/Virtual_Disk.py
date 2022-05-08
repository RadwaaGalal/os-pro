class virtual_disk:
 def write(self):
    f = open("OS_pro.txt", "w")
 #كده عملنا ال super block
    for i in range(1024):
     f.write("0")
    f.close()
    
  #هتأخد مني داتا واندكس وتحول الدااتا لبايت وتكتبها في الفايل مكان الاندكس
 def write_block(self,data,index):
     if(type(data)==int):
       fi=open("OS_pro.txt","ab")
       string_val = str(data)
       byte_value = str_val.encode()
       fi.seek(index)
       fi.write( byte_value)
       fi.close()
     else:
         fi=open("OS_pro.txt","wb")
         fi.seek(index)
         fi.write( data)
         fi.close()
           
      
  #هتحول الداتا لانتجر وتقراها
 def read_block(self,data,index):
     if(type(data)==int):
        fil = open("OS_pro.txt", "r")
        fil.seek(index)
        fil.read()
        f.close()
     else:
        fil = open("OS_pro.txt", "r")
        fil.seek(index)
        fil.read()
        st_val =data.decode()
        #int_val=int(st_val , base=10)
        fil.close()   


