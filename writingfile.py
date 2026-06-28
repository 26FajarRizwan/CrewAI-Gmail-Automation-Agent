#writing to a file
f=open("demo.txt","a")
f.write("\n I want to learn javascript also")
f.close()

f=open("sample.txt","w")
f.close()

f=open("demo.txt", "r+")
f.write("abc")
f.close()

#r+        data can be read      overwrite    pointer at start       no truncate
#w+          same                 same          does not value        truncate
#a+        read                   append       ptr end               no truncate


