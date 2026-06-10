Task 1

Files

Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it. Then write another script that opens myfile.txt, and reads and prints its contents. Run your two scripts from the system command line. 

Does the new file show up in the directory where you ran your scripts? 

What if you add a different directory path to the filename passed to open?

Note: file write methods do not add newline characters to your strings; add an explicit "\n" at the end of the string if you want to fully terminate the line in the file.

 

Task 2

Extend Phonebook application

Functionality of Phonebook application:

Add new entries 
Search by first name 
Search by last name 
Search by full name
Search by telephone number
Search by city or state
Delete a record for a given telephone number
Update a record for a given telephone number
An option to exit the program
 

The first argument to the application should be the name of the phonebook. Application should load JSON data, if it is present in the folder with application, else raise an error. After the user exits, all data should be saved to loaded JSON.