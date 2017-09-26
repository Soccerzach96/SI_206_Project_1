import os
import csv
import datetime
import filecmp

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
	list_of_dict = list()
	with open(file) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			new_dict = dict()
			new_dict['First'] = row['First']
			new_dict['Last'] = row['Last']
			new_dict['Email'] = row['Email']
			new_dict['Class'] = row['Class']
			new_dict['DOB'] = row['DOB']
			list_of_dict.append(new_dict)
	return list_of_dict



#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	sorted_list = list()
	sorted_list = sorted(data, key=lambda k: k[col])

	top_name = dict()
	top_name = sorted_list[0]

	firstName = top_name['First']
	lastName = top_name['Last']

	fullName = firstName + ' ' + lastName
	return fullName



#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:

	counts = dict()
	for d in data:
		counts[d['Class']] = counts.get(d['Class'], 0) + 1

	lst = list()
	for key, val in counts.items():
		reverse_lst = (val, key)
		lst.append(reverse_lst)

	lst = sorted(lst, reverse=True)

	sorted_lst = list()
	for val, key in lst:
		reverse_back = (key, val)
		sorted_lst.append(reverse_back)

	return sorted_lst



# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	count_day = dict()
	for day in a:
		birthday = day['DOB']
		bday = birthday.split('/')
		day = bday[1]
		if day not in count_day:
			count_day[day] = 1
		else:
			count_day[day] += 1

	lst = list()
	for key in count_day.keys():
		day_of_month = (key, count_day[key])
		lst.append(day_of_month)

	sorted_birthdays = sorted(lst, reverse=True, key = lambda k: k[1])
	return int(sorted_birthdays[0][0])



# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	age = list()

	from datetime import date

	today = date.today()
	sum_of_ages = 0
	count_of_people = 0

	for person in a:
		birthday = person['DOB']
		bday = birthday.split('/')
		month = int(bday[0])
		day = int(bday[1])
		year = int(bday[2])
		age = today.year - year - ((today.month, today.day) < (month, day))
		sum_of_ages += age
		count_of_people += 1

	average_age = round(float(sum_of_ages / count_of_people))

	return average_age





#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	list_of_dict = list()
	for row in a:
		new_dict = dict()
		new_dict['First'] = row['First']
		new_dict['Last'] = row['Last']
		new_dict['Email'] = row['Email']
		list_of_dict.append(new_dict)

	a = list_of_dict

	a = sorted(a, key=lambda k: k[col])

	keys = a[0].keys()
	with open(fileName, "w", newline='\n') as output_file:
		writer = csv.DictWriter(output_file, keys, delimiter = ',', lineterminator = '\n')
		writer.writerows(a)

	# list_of_dict = list()
	# with open(file) as csvfile:
	# 	reader = csv.DictReader(csvfile)
	# 	for row in reader:
	# 		new_dict = dict()
	# 		new_dict['First'] = row['First']
	# 		new_dict['Last'] = row['Last']
	# 		new_dict['Email'] = row['Email']
	# 		new_dict['Class'] = row['Class']
	# 		new_dict['DOB'] = row['DOB']
	# 		list_of_dict.append(new_dict)
	# return list_of_dict



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),35)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

