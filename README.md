# Test task: House with elevator

---

Project have 4 classes: House, Floor, Human and Elevator

When the house is initialized, it is filled with floors.
Each floor has a certain number of people. Everyone wants to move to another floor.

Elevator have functions: 
+ check_way - shows the direction of the elevator ('True' - Up, 'False' - Down).
+ check_output - checks whether there are those wishing to get out of the elevator.
+ check_input - checks whether there are those wishing to enter the elevator.
+ unload_people - if check_output == True, the right people are unloaded.
+ download_people - if check_input == True and the elevator have free places, the right people are downloaded. 

### To start the elevator you need to create a ***house*** and call the function: ***house.work_elevator()*** 
##### P.S. Project haven't requirements. The clear Python.
