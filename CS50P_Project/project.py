import requests

response = requests.get("https://code.org/schools.json").json()
schools = response["schools"]

def main():
    choice = int(menu())
    while choice != 8:
        if choice == 1:
            print(f"{count_schools(schools)} Schools on record")
            print("*" * 20)
        elif choice == 2:
            print_results(FreeSchools(schools))
        elif choice == 3:
            name = input("Enter school name: ")
            print_results(school_by_name(schools, name))
        elif choice == 4:
            level = input("Enter school level: ")
            print_results(school_by_level(schools, level))
        elif choice == 5:
            language = input("Enter programming language: ")
            print_results(school_by_language(schools, language))
        elif choice == 6:
            country = input("Enter country: ")
            print_results(school_by_country(schools, country))
        elif choice == 7:
            city = input("Enter city: ")
            print_results(school_by_city(schools, city))
        else:
            print("Invalid choice")
        choice = int(menu())

#create menu for user to selet choice
def menu():
    print("""
    1 - How many Schools are there of note
    2 - List of free schools
    3 - Search school by name
    4 - Search school by level 
    5 - Search by programming language 
    6 - Search by country
    7 - Search by city
    8 - Exit
    """)
    return input("Enter your choice: ")

#count number of schools returned by API
def count_schools(schools):
    return len(schools)

#helper function to check if school is free
def isFree(school):
    return school["money_needed"]

#find free schools
def FreeSchools(schools):
        return list(filter(isFree, schools))

#find school by name
def school_by_name(schools, name):
    return list(filter(lambda school: school["name"] == name, schools))

#find school by level
def school_by_level(schools, level):
    return list(filter(lambda school: level in school["levels"], schools))

#find school by language
def school_by_language(schools, language):
    return list(filter(lambda school: language in school["languages"], schools))

#find school by city
def school_by_city(schools, city):
    return list(filter(lambda school: school["city"] == city, schools))

 #find school by country       
def school_by_country(schools, country):
    return list(filter(lambda school: school["country"] == country, schools))

#print search resluts to screen
def print_results(results):
    if results:
        for school in results:
            print(f"Name: {school['name']}")
            print(f"Website: {school['website']}")
            print(f"Contact Number: {school['contact_number']}")
            print(f"Contact Email: {school['contact_email']}")           
            print("*" * 20)
    else:
        print("No results found") 

if __name__ == "__main__":
    main()
