#file I/O
#perform operations on a file like read and write data
#text files .txt, .docx, .log etc
#binary files .mp4, .mov, .png, .jpeg etc

#basic operations
#open read & close file
f= open("demo.txt","r")
# data =f.read()
# print(data)
# print(type(data))
line1=f.readline()
print(line1)

line2=f.readline()
print(line2)

f.close()



