from Fat_Table import Fat
class Directory_Entery():
 obj=Fat()
 file_name=''
 file_attr=0
 file_empty=['0']*12
 file_size=0
 first_cluster= obj.get_avaliable_cluster()
 
    
 def __init__(self,file_name,file_attr):
    self.file_attr=file_attr
    self.file_name=file_name
    lest_name=self.file_name.split('.')
    #['tre', 'txt']

        #0x0=file
    if file_attr==0x0:
        Directory_Entery.FILE_NAME_extention(self,lest_name[0],lest_name[1])
            #0x10=folder
    elif file_attr==0x10:
        Directory_Entery.FILE_NAME_no_extention(self,lest_name[0])
    #print( lest_name[0])
    #print(lest_name[1])

 def FILE_NAME_extention(self,NAME,EXTINTION):
    name=NAME
    len_name=len(name)
    extension=EXTINTION
    len_extension=len(extension)
    if(len_name>7):
        name=name[:7]
    elif(len_name<7):
        name=name
            
    if(len_extension>3):
           extension=extension[:3]
    elif len_extension<3:
           extension=extension

    name=name+'.'+extension
      
    self.file_name=name
    #return name
    
##    def get_name(self):
##        return self.file_name
##
 def FILE_NAME_no_extention(self,NAME):
        name=NAME
        len_name=len(name)
        if(len_name>11):
            name=name[:11]
        elif(len_name<11):
            name=name
        self.file_name=name
        return name
# def get_byte():
# def get_derictory_entry():
