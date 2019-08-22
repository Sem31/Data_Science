#SF Salaries Exersice

#import the pandas library

import pandas as pd

#read Salaries.csv as a dataframe called sal

sal = pd.read_csv('Salaries.csv')

print('check the head of the DataFrame :')

print(sal)

print('\n\ncheck the info how many entries there are : ')

print(sal.info())

print('\n\nWhat is the average BasePay :')
print(sal['BasePay'].mean())

print('\n\nwhat is the highest amount of OvertimePay in the dataset : ')
print(sal['OvertimePay'].max())

print('\n\nWhat is the job title of JOSEPH DRISCOLL ?')
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])

print('\n\nHow much does JOSEPH DRISCOLL make (including benefits)?')
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPay'])

print('\n\nWhat is the name of highest paid person (including benefits)?')
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()])

print('\n\nWhat is the name of lowest paid person (including benefits)?')
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()])

print('\n\nWhat was the average (mean) BasePay of all employees per year?')
print(sal.groupby('Year')['BasePay'].mean())

print('\n\nHow many unique job titles are there?')
print(sal['JobTitle'].nunique())

print('\n\nHow many people have the word Chief in their job title? (This is pretty tricky')
def string_chief(title):
	if 'chief' in title.lower().split():
		return True
	else :
		return False
print(sum(sal['JobTitle'].apply(lambda x : string_chief(x))))

print('\n\nWhat are the top 5 most common jobs?')
print(sal['JobTitle'].value_counts().head(5))

print('\n\nHow many Job Titles were represented by only one person in 2013?')
print(sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1))


print('\n\nIs there a correlation between length of the Job Title string and Salary?')
sal['length_job'] = sal['JobTitle'].apply(len)
print(sal[['length_job','TotalPayBenefits']].corr())


