import requests

response = requests.get("https://code.org/schools.json").json()
schools = response["schools"]

def main():
    choice = int(menu())

#create menu for user to selet choice
"""
 Create a Menu that gives options to answer questions about data:
    a) How many Schools are there of note
    b) List of free schools - Money Needed false
    c) Search school by name - name, website, level, country, contact_name, contact_number, contact_email, description - List of dictionaries
    d) Search school by level - "Preschool", "Elementary", "Middle School", "High School", "College" 
    e) Search by programming language - name, country, website
    f) Search by country - List
    g) Search by city - name, website, level, country, contact_name, contact_number, contact_email- List
"""
def menu():
    print("""
    1 - How many Schools are there of note
    2 - List of free schools - Money Needed false
    3 - Search school by name - name, website, level, country, contact_name, contact_number, contact_email, description - List of dictionaries
    4 - Search school by level - "Preschool", "Elementary", "Middle School", "High School", "College" 
    5 - Search by programming language - name, country, website
    6 - Search by country - List
    7 - Search by city - name, website, level, country, contact_name, contact_number, contact_email- List
    8 - Exit
    """)
    return input("Enter your choice: ")



#helper function to check if school is free
def isFree(school):
    return school["money_needed"]

#find free schools
def FreeSchools(schools):
        return list(filter(isFree, schools))

 #find school by country       
def school_by_country(schools, country):
    return list(filter(lambda school: school["country"] == country, schools))