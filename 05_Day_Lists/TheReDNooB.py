# Exercises: Level 1

#  1. Declare an empty list
mylist = []
print(mylist,type(mylist))

#  2.Declare a list with more than 5 items
other_list = ["monday", 31, True, {"two":2, "three":3}, "80"]
print(other_list)

#   3.Find the length of your list
print(len(other_list))

#   4.Get the first item, the middle item and the last item of the list
my_list = list()
my_list = other_list[::2]
print(my_list)

#   5.Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["TheReDNooB", 22, 1.80, "Single", "Colombia"]
print(mixed_data_types)

#   6.Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#   7.Print the list using print()
print(it_companies)

#   8.rint the number of companies in the list
print("it companies: ",len(it_companies))

#   9.Print the first, middle and last company
other_it_list = it_companies[::3]
print(other_it_list)

#   10.Print the list after modifying one of the companies
it_companies[0] = "Meta"
print(it_companies)

#   11.Add an IT company to it_companies
it_companies.append("Tesla")
print(it_companies)

#   12.Insert an IT company in the middle of the companies list
it_companies.insert(4,"Open IA")
print(it_companies)

#   13.Change one of the it_companies names to uppercase (IBM excluded!)
it_name = it_companies[0]
it_companies[0] = it_name.upper()
print(it_companies)

#   14-Join the it_companies with a string '#;  '
joined_companies = '#'.join(it_companies)
print(joined_companies)

#   15.Check if a certain company exists in the it_companies list.
does_exist = "Google" in it_companies
print(does_exist)

#   16.Sort the list using sort() method
it_companies.sort()
print(it_companies)

#   17.Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)

#   18.Slice out the first 3 companies from the list
first_it_companies = it_companies[:3]
print(first_it_companies)

#   19.Slice out the last 3 companies from the list
last_it_companies = it_companies[-3:]
print(last_it_companies)

#   20.Slice out the middle IT company or companies from the list
middle_it_companies = it_companies[3:7]
print(middle_it_companies)

#   21.Remove the first IT company from the list
it_companies.remove("Tesla")
print(it_companies)

#   22.Remove the middle IT company or companies from the list
it_companies.remove("META")
print(it_companies)

#   23.Remove the last IT company from the list
it_companies.pop(-2)
print(it_companies)

#   24.Remove all IT companies from the list
it_companies.clear()
print(it_companies)

#   25.Destroy the IT companies list
del it_companies

#   26.Join the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
list_joined = front_end + back_end
print(list_joined)

#   27.After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = []
full_stack = list_joined.copy()
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print("copy ",full_stack)

# Exercises: Level 2
#   1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

"""
1. Sort the list and find the min and max age
2. Add the min age and the max age again to the list
3. Find the median age (one middle item or two middle items divided by two)
4. Find the average age (sum of all items divided by their number)
5. Find the range of the ages (max minus min)
6. Compare the value of (min - average) and (max - average), use abs() method
"""
#

#1
ages.sort()
min_age = min(ages)
max_age = max(ages)
print(f"the min age is: {min_age} and the max age is: {max_age}")

#2
ages.append(min_age)
ages.append(max_age)
print(ages)

#3
ages.sort()
print("the median age is: ",ages[5])

#4
observations = sum(ages)
average = observations/len(ages)
print("the average age is: ",average)

#5
range_age = ages[-1]-ages[0]
print("the range of the ages is: ",range_age)

#6
min_avg = abs(min_age - average)
max_avg = abs(max_age - average)
print(f"the value of (min - average) is: {min_avg} and the value of (max - average) is: {max_avg}")
