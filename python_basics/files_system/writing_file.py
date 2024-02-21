# new_file=open('/media/khalid/Coding/Practices/python/python_basics/files/newFile.txt','w') 
# new_file.write('This is the new file') #it will write from the scratch file, if already have this file then it will override , if there have not any file then it will create and write

new_file=open('/media/khalid/Coding/Practices/python/python_basics/files/newFile.txt','a') 
new_file.write('\nThis is the new line') #it will write in the last line of this file, if already have this file then it will override , if there have not any file then it will create and write in the last 

new_file.close()