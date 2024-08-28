# Define three variables for the LaunchCode shuttle - one for the starting fuel level, another for the number of astronauts aboard, and the third for the altitude the shuttle r




# Exercise #1: Construct while loops to do the following:
  # a. Query the user for the starting fuel level. Validate that the user enters a positive, integer value greater than 5000 but less than 30000. 

fue_level = 0
while fue_level < 5000 or fue_level > 30000:
      fue_level = int(input("what is the fuel level"))



# b. Use a second loop to query the user for the number of astronauts (up to a maximum of 7). Validate the entry.
number_of_astronots = 0
while number_of_astronots < 1 or number_of_astronots > 7:
      number_of_astronots = int(input("what is the number of astronot"))
 
  
  
  
# c. Use a final loop to monitor the fuel status and the altitude of the shuttle. Each iteration, decrease the fuel level by 100 units for each astronaut aboard. Also, increase the altitude by 50 kilometers.



# Exercise #2: Print the result with the phrase, The shuttle gained an altitude of ___ km and has ___ kg of fuel left. Fill in the blanks with the altitude and fuel level values.

# If the altitude is 2000 km or higher, add “Orbit achieved!” Otherwise add, “Failed to reach orbit.”
