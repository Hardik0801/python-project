# import random
# #(i)Revering a word or sentence
# def reverse(str):
#     s =""
#     for character in str:
#         s = character + s
#     return s

# user = str(input("Enter a word or sentence to be reversed: "))


# #(ii) Generating a password
# alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# def password():
#     size = 1
#     password = ""
#     while size <= 10:
#         password = password + random.choice(alph)
#         size+=1
#     return password


# #(iii) Exhchanging first and last string 
# def swap(word):
#     start = word[0]
#     end = word[-1]
#     swapped_number = end + word[1:-1] + start
#     print(swapped_number)

# user_1 = str(input("Enter any word: "))

#(iv) Swapcase
# string_4 = "Hello my name is PETER"
# x = string_4.swapcase()
# print(x)

#(v) Wrap Text
