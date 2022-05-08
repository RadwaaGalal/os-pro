class Fat:
    
#فانكشن لتعريف الفات تابول
    
 def initil(self):
  fat=[0]*1024
  fat[0]= -1
  fat[1]= -1
  fat[2]= -1
  fat[3]= -1
  fat[4]= -1
  return fat

    #فانكشن عشان احول الاراي لبايت واكتبه في الفايل
 def write_cluster(self):
  fi=open("OS_pro.txt","ab+")
     # converting to string
  str_val = str(Fat.initil(self))
     # converting string to bytes
  byte_val = str_val.encode()
  fi.seek(1024)
  fi.write(byte_val)
  fi.close()
  #return byte_val

#اقرأالفايل واحول الاراي لانتجر وارجعه عشان بعدين هحتاج اعرف ايه الاماكن الفاضية  
 def read_cluster(self):
  fil = open("OS_pro.txt", "r")
  fil.seek(1024)
  fil.read()
  st_val =Fat.write_cluster(self).decode()
  #int_val=int(st_val , base=10)
  fil.close()
 # return int_val

  #فانكشن بترجعلي اندكس اول مكان فاضي في الاراي
 
 def get_avaliable_cluster(self):
     fil = open("OS_pro.txt", "r+")
    
     index=0
     for i in range(1024):
         if(Fat.initil(self)[i]==0):
             index=i
             break
     fil.close()       
     return index
    
   #بيديني اندكس وانا اجيب القيمة اللي في الاندكس ده
 def get_next(self,index):
    
    return Fat.initil(self)[index]

#بيغير يدوياقيمة عنصر معين هو هيديني الاندكس
 def set_next(self,x,val):
   
     Fat.initil(self)[x]=val


 def file(self):
   File=open('OS_pro.txt',"a")
   File.seek(1024*5)
   for i in range(1019*1024):
      File.write("0")
   File.close()