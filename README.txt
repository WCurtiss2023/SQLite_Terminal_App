Assignment 1 - Sqlite
William Curtiss
ID: 2348299

Hi Rene,
When you run my script on your machine, you should uncomment the
'generateAdvisorsForWholeDB()' function, 'isDeletedToZero()', and 'readCSV_toDB()'.
'generateAdvisorsForWholeDB()' will make it so there is an advisor for every student, and 
'isDeletedToZero()' will make it so isDeleted is zero for every record. 
Also, you should change your path to StudentDB and student.csv in my function readCSV_toDB
before uncommenting the method by the same name. Comment them again afterword, leaving only 'menu()'.
App should run seemlessly after that. Thanks. 
