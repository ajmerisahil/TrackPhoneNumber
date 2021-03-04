#importing package
import phonenumbers
#number imported form test.py file
from test import number

#geocoder imported for fetching the country name
from phonenumbers import geocoder

ch_number = phonenumbers.parse(number , "CH")
print(geocoder.description_for_number(ch_number , "en"))

#carrier imported for fetching the service provider name
from phonenumbers import carrier

service_number = phonenumbers.parse(number , "RO")
print(carrier.name_for_number(service_number , "en"))