
#1.Maria is entering customer data for her web design business. You’re going to help her organize her data.Start by turning this list of customer first names into a list called first_names. Make sure to enter the names in this order:Ainsley,Ben,Chani,Depak
#2.Create an empty list called age.
#3.Depak’s age is 42. Use .append() to add 42 to age.
#4.Maria needs a list of the ages for all customers. Create a new list called all_ages that adds age with the following list, containing the ages for Ainsley, Ben, and Chani:[32, 41, 29]Make sure all_ages begins with the ages for Ainsley, Ben, and Chani and ends with Depak’s age (stored in age)!
#5.Create a new variable called name_and_age that combines first_names and all_ages using zip.
#6.Create a range object called ids with an id number for each customer. Since there are 4 customers, so id values should go from 0 to 3.











first_names=['Ainsley','Ben','Chani','Depak']
age =[32,41,29]
age.append(42)
all_ages =age

name_and_age =zip(first_names ,all_ages)
ids=range(0,4)
print(list(name_and_age))