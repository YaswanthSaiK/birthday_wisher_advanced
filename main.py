##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random

# 1. Update the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day

list = {
    0 : "letter_templates/letter_1.txt",
    1 : "letter_templates/letter_2.txt",
    2 : "letter_templates/letter_3.txt"
}
# 2. Check if today matches a birthday in the birthdays.csv
df = pandas.read_csv("birthdays.csv")
df.to_dict()

gh = {row.month: row.day for (index, row) in df.iterrows()}
count = 0
for i in gh:
    if i == month and gh[i] == day:
        n = random.randint(0,2)
        f = open(list[n])
        letter = f.read()
        h = letter.replace("[NAME]", df["name"][count])
        print(h)
        count +=1
    count+=1

print(gh)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
# from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




