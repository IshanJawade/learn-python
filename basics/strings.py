s = "Hello World"

# looping through the string
for i in s:
    print(i) 

print("length of the s string is", len(s))

# ------------ Searching -----------------
txt = "The best things in life are free!"

# check if the pattern is present
print("free" in txt)    # boolean 

# check if the pattern is not present 
print("ishan" not in txt)   # boolean

# if statements with pattern search
if "freei" in txt:
    print("Yes, it's there")
else:
    print("not found")

# if with not in
if "ishan" not in txt:
    print("Not there")

# ----------- Slicing Strings ------------
text = "0123456789"

# this works well of count index from 1 not from 0
# exclude the numbers in the slicing function
print(text[2:9])     

# from start to the index
print(text[:6])

# from index to end
print(text[4:])

# negative indexing
print(text[-5:-2])

# Strings with placeholders
age = 43
ans = f"That person is {age} years old"
print(ans) 
# default way
print("That person is", age, "years old")

# ------ String OPs -----------

text = "This String is for Testing Purpose ONLY"

print(text.upper())
print(text)