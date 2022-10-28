breakify = ["Haiku frogs","in snow","A limerick","came from","Nantucket Tetrametric","drum-beats thrumming","Hiawathianic rhythm."]
"<by>".join(breakify)

#modify strings
string = "Hello world!"
output = []
index = 0
while index < len(string):
    output.append(string[index])
    index += 1

print(output)

#find and remove
string1 = "SPAM!HelloSPAM! worldSPAM!!"
output = []
index = 0
while index < len(string):
    if string[index:index+5] == "SPAM!":
        index += 5
    else:
        output.append(string[index])
        index += 1
print("".join(output))
