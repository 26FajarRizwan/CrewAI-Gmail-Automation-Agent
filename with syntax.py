with open("demo.txt", "r") as f:
    data=f.read()
    print(data)

#close is not necessary with "with syntax"

with open("demo.txt","w") as f:
    f.write("new data")
    