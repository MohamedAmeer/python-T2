# merge two python dictionaries

std_detail ={
    "name": "brock",
    "id": "12",
    "age": "27",
     "country":"india",
    "email": "abc@gmail.com",
    "phone_no": "12345"
}
clg ={
 "clg_name":"xyzinstitute",
 "clg_contact_no": "9876543"
}
std_detail.update(clg)
print(std_detail)

# remove a key from dictionary

countrys = {
    "india": "1",
    "america": "2",
    "china": "3",
    "indonesisa": "4",
    "dubai": "5","switcherland": "6"
}
print(countrys)

countrys.pop("china")
print(countrys)

# map two lists into a dictionary
# first create two list

book = ["english", "math", "physics"]
value = ["$2", "$4","$7"]
# then mapping the two lists into a dictioanry
zip(book, value)
next(zip(book, value))
dictionary = dict(zip(book, value))
print(dictionary)

#find a length of a set

set = {"123", "captain", ".2","animals", "birds" }
print(len(set))

# remove intersection of 2nd set from 1st set

a = {"red", "orange", "22", "100","yellow"}
b = {"green", "red", "44", "22", "100"}

c = a | b
print(c)
