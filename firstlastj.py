import json
import sys
people_string = '''
{
"Information" : [{
      "First_Name": "Jack",
      "Second_Name": "Leiper",
      "Age": "21",
      "Height": "5'11",
      "ID": "123"
   },
   {
      "First_Name": "Ian",
      "Second_Name": "Brooke",
      "Age": "29",
      "Height": "5'8",
      "ID": "100"
   },
   {
      "First_Name": "Chelsea",
      "Second_Name": "Brown",
      "Age": "19",
      "Height": "5'4",
      "ID": "999"
   },
   {
      "First_Name": "Peter",
      "Second_Name": "James",
      "Age": "42",
      "Height": "6'2",
      "ID": "667"
   },
   {
      "First_Name": "Keith",
      "Second_Name": "Jones",
      "Age": "42",
      "Height": "17'2",
      "ID": "668"
   }
      ]
}
'''
data2 = json.loads(people_string)

#print(type(data2["Information"]))
#prints

def ret_last_name(firstname):
   for i in data2 ["Information"]:
      found = False
      first = i["First_Name"]
      last = i["Second_Name"]
      if firstname == (first):
         print("Hello, " + first + " " + last + ".") 
         return last
         found = True
         
      else:
         found = False   
   if found == False:
      return "Error! No name found."

def yesno(response):
   if response == "Y":
         response = ""
         return func()
   if response == "n":
      return ("Thank you for using the program.")
   else:
      raise NameError("Invalid input, program expected \"Y\" or \"n\" only")

def func():
   firstname = raw_input("Enter Name: ")
   ret_last_name(firstname)
   
   
   response = raw_input("Do you want to search for another name?(Y/n): ")
   yesno(response) 
   print yesno(response)  
      
func()

   
   
