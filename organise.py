import os
import shutil

source="C:/Users/star/Downloads"
destination="C:/Users/star/Downloads/documents"

filesList=os.listdir(source)

for i in filesList:
    name,ext=os.path.splitext(i)
    
    if ext=="":
        continue

    if ext in [".txt", ".doc", ".docx", ".pdf"]:
        path1=source+"/"+i
        path2=destination+"/"+i

        if os.path.exists(destination):
            shutil.move(path1,path2)
        else:
            os.makedirs(destination)
            shutil.move(path1,path2)