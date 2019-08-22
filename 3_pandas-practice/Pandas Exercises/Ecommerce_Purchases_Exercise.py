#Ecommerce Purchases Exercise

#import pandas and NUmpy

import pandas as pd
import numpy as np

#data read from the csv using pandas

eco = pd.read_csv('Ecommerce Purchases')
print(eco)

print('\n\nHow many rows and columns are there?')
print(eco.info())

print('\n\nWhat is the average Purchase Price?')
print(eco['Purchase Price'].mean())

print('\n\nWhat were the highest and lowest purchase prices?')
print(eco['Purchase Price'].max())
print(eco['Purchase Price'].min())

print('\n\nHow many people have English "en" as their Language of choice on the website?')
print(eco[eco['Language'] == 'en'].count())

print('\n\nHow many people have the job title of "Lawyer"')
print(eco[eco['Job'] == 'Lawyer'].count())

print('\n\n How many people made the purchase during the AM and how many people made the purchase during PM ?')
print(eco['AM or PM'].value_counts())

print('\n\nWhat are the 5 most common Job Titles?')
print(eco['Job'].value_counts().head(5))

print('\n\nSomeone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction?')
print(eco[eco['Lot']  == '90 WT']['Purchase Price'])

print('\n\nWhat is the email of the person with the following Credit Card Number: 4926535242672853')
print(eco[eco['Credit Card'] ==  4926535242672853]['Email'])

print('\n\nHow many people have American Express as their Credit Card Provider *and made a purchase above $95 ?')
print(eco[(eco['CC Provider'] == 'American Express')&(eco['Purchase Price'] > 95)].count())

print('\n\nHard: How many people have a credit card that expires in 2025?')
print(sum(eco['CC Exp Date'].apply(lambda x : x[3:]) == '25'))

print('\n\nHard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)')
print(eco['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5))
