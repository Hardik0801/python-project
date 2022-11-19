string_1 = "This is a \n string"

#(i) Spilting a number
print("(i)",string_1)

#(ii) Checking if substring is there or not
substring = "string"
print("(ii)",substring in string_1)

#(iii) Replacing strings
replace = string_1.replace("This", "It")
print("(iii)",replace)

#(iv) Index of first occurence
index = string_1.find("is")
print("(iv) Index of first occurence of substring is",index)