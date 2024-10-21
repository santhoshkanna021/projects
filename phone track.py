import phonenumbers
from phonenumbers import geocoder


number = input("Enter the phone number with country code (e.g., +41446681800): ")

ch_number = phonenumbers.parse(number, "CH")  

print(geocoder.description_for_number(ch_number, "en"))

print("succesfully verified")
