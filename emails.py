import os  # for files
import re  # python Regular Expressions
import json  # json

# get user input about what file to search in:
filename = input(
    "\nEnter the name of the file you want to search for email addresses: \n"
)

# open file, search for mails
with open(filename, "r") as f:  # open file and close after done
    # read text into variable
    data = f.read()
    # find all matching substrings
    match = re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", data)
    # print(type(match)) --> <class 'list'>

# write results into a text file
with open("email_results.txt", "w+") as results:
    match = str(match)  # convert from list to string
    results.write(match)  # done
    print(match)
