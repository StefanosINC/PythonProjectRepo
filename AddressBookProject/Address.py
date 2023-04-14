## leveraging OOP Create an Address Book .
## Some of the features we want in an address book are Delete, Search Create Read.
## Also, I want to be able to Sort the AddressBook by City, or State. 
## I want to be able to caculate a percentage value of whos phone numbers start within the 559 area code. 
## I want to be able to have compelte proper error checking of this information. 
## Lets populate some values into the addressBook for starters then move forward from there. 
## Proper Error handling needs to be performed for all of this. 

## AI RESPONSE
### single string argument to be passed as the first parameter, but you're passing multiple arguments to it. 
###To fix this, you can concatenate all the string inputs into a single string,
### then pass that as the first argument to re.match().
## You can also simplify the method by removing the while loop and the try-except block,
## since they're not necessary for your validation.


import re
import pycountry
## Challenge -> Make it so each individual User has there own addressBook Once the above things are completed
GLOBAL_BOOKLET = []

class Contact:
    def __init__(self, address, zip_code, phone, city, state, country, residence_name):
        self.address = address,
        self.zip_code = zip_code, 
        self.phone = phone,
        self.city = city,
        self.state = state,
        self.country = country,
        self.residence_name = residence_name
    
class AddresBook: 
    def __init__(self):
        self.booklet = []

    def RegexValidation(self, address, zip_code, phone, city, state, country, residence_name):
       
        if not re.match(r'^\d{3}-\d{3}-\d{4}$', phone): ## CHeck Phone. Validation
            raise TypeError('Phone does not meet requirements')
        if not re.match(r'^\d{5}$', zip_code):
            raise TypeError('Zip Code does not meet requirements')
        input_string = ' '.join([address, zip_code, phone, city, state, country, residence_name]) ## Just need to make thema list to then concat them
        if not re.match(r'^[\w\s]+$', input_string.replace("-", "")): ## Dive more int this BIG TIME
            raise TypeError('The Input contains a special charachter and that is not allowed')
        
        else:
            print('Successfully passed the match!')
    def add_contact(self):
     while True:

        address = input('enter address')
        zip_code = input('Enter Zip')
        phone = input("Enter Phone")
        city = input('Enter City')
        state = input('Pleaes select a state')
        country = input('Enter a country')
        residence_name = input('Enter a residence')
        self.CountryValidation(country)
        self.RegexValidation(address, zip_code, phone, city, state, country, residence_name)
        newEntry = Contact(address, zip_code, phone, city, state, country, residence_name)
        
        GLOBAL_BOOKLET.append(newEntry)
        print(f"Added a new contact. The residence name is {newEntry.residence_name}")

    def search_Contact(self):
        for index, contact in enumerate(GLOBAL_BOOKLET):
            print(f"Index Position: {index}")

        index_input = int(input("Enter the index of the contact you want to retrieve: "))
        self.RegexValidation(index_input)
        if index_input < len(GLOBAL_BOOKLET):
            foundContact = GLOBAL_BOOKLET[index_input] #This is what trully allows us to correlate a searchable index to an object in our list. 
            print(f"{index} Contact:{foundContact.address} Zip Code: {foundContact.zip_code} Phone: {foundContact.phone} City: {foundContact.city} State: {foundContact.state} Country: {foundContact.country} Residencey {foundContact.residence_name}")
        else:
            print("Invalid index")

    def print_contact(self): ## Eventually address the commas
        print('Printing Contact List')
        for index, contact in enumerate(GLOBAL_BOOKLET):
            print(f" {index} Contact:{contact.address} Zip Code: {contact.zip_code} Phone: {contact.phone} City: {contact.city} State: {contact.state} Country: {contact.country} Residencey {contact.residence_name}")

    def exit_program(self):
        print('Exiting the Switch Case Options')
        exit()
    
    def delete_Contact(self):
        index_input = int(input("Enter the index of the contact you want to retrieve: "))
        if index_input < len(GLOBAL_BOOKLET):
            foundContact = GLOBAL_BOOKLET[index_input] #This is what trully allows us to correlate a searchable index to an object in our list. 
            GLOBAL_BOOKLET.remove(foundContact)
            print(GLOBAL_BOOKLET)
        else:
            IndexError("Invalid index chosen")

    def getContactByResidence_Name(self, residence_name):
        for contact in GLOBAL_BOOKLET:
            if contact.residence_name == residence_name:
                return contact
            return None
    
    def update_Contact(self):
        AddresBook.print_contact(self) ## Print the contacts
        Residence_Name_Input = input('Enter the place you wish to update according to there residence name:  ')
        contact = self.getContactByResidence_Name(Residence_Name_Input)
        print(f" Below is the retrieved Contact\n ----------------\n 1Please enter the name of the part you want to change (E.G 'Phone')\n Address {contact.address}\n Zip Code: {contact.zip_code}\n Phone: {contact.phone}\n City: {contact.city}\n State: {contact.state}\n Country: {contact.country}\n ResidenceName {contact.residence_name} \n------------")
        UpdateChoice = input('Great Contact to Update. What would you like to update next address, zip_code, phone, city, state, country? ')
        if UpdateChoice == "address":
             new_address = input('Enter the new address: ')
             contact.address = new_address
             
        elif UpdateChoice == "zip_code":
            new_zip_code = input('Enter the new zip code: ')
            contact.zip_code = new_zip_code

        elif UpdateChoice == "phone":
            new_phone = input('Enter the new phone number: ')
            contact.phone = new_phone

        elif UpdateChoice == "city":
            new_city = input('Enter the new city: ')
            contact.city = new_city

        elif UpdateChoice == "state":
            new_state = input('Enter the new state: ')
            contact.state = new_state

        elif UpdateChoice == "country":
            new_country = input('Enter the new country: ')
            contact.country = new_country
        else:
            print('Invalid choice.')
        print('Contact updated successfully.\n')
## I want to be able to caculate a percentage value of whos phone numbers start within the 559 area code. 
    def caculateAreaCodePercentage(self, phone):
        for contact in GLOBAL_BOOKLET:
            if contact.phone == residence_name:
                return contact
            return None
        ## I want to be able to look through the Global List
        ## If the Phone Number starts with 559
    def CountryValidation(self, country): ## Research on how to improve this.
        countries = list(pycountry.countries)
        for c in countries:
            if c.name == country:
                print('validation is true')
            else: 
                raise TypeError('Countries dont match the library')
            
my_book = AddresBook()
    
print('Welcome to the console version of this AddressBook Application')
## While the condition is true...
while True:
    choice = input("Please enter your choice {1 - 4 }")
    Options = {
    "1": my_book.add_contact,
    "2": my_book.print_contact,
    "3": my_book.search_Contact,
    "4": my_book.delete_Contact,
    "5": my_book.update_Contact,
    "6": my_book.exit_program
    }
    Options.get(choice, lambda: print("Invalid choice"))()
