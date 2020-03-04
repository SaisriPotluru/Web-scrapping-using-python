# cs5293p19-project0
web scrapping using python


**Norman, Oklahoma police department reports of incidents **

This website consist of arrests, incidents and cases summaries.The data can be found in http://normanpd.normanok.gov/content/daily-activity website.In this project we are going to extract information from the file (PDF) then get the data into a database and display all the count of the nature types of the incidents happening.

Author Saisri M Potluru.You can contact me at saisri.m.potluru-1@ou.edu .


The packages which has been used are urllib.request,PyPDF2,urllib,tempfile,sqlite3,argparse and pandas.


**Setup Info : 

You can create all the files using touch and mkdir commands.
By giving the url of the required pdf ,we can fetch the data in the pdf,extract all the pages in the pdf then after performing the data scrapping the data is pushed to the sqlite3 database and we can get to know the count of the nature types of the incidents happening .The data which is extracted from the pdf has been stored as NORMANPOLICE.db. 

By using the following steps you can run the main.py file which is in the project0 directory.You can code it in command line as python main.py –incidents “the url for which you want to provide” . You can see the output as the different nature types along with the occurences of those types for the given data.


**Description of the functions:**

**fetchincidents():**

This function reads the data from the url using the urllib.request package and returns the collected data to the next function.


**extractincidents():**

In the function we extract the data by using the PyPDF2 package and store it a temp. this function does all the data scrapping part ,converting it in the form of list of lists and at last  a dataframe of  5 rows.


**createdb():**

This function will connect to a database 'NORMANPOLICE.db' and creates a table incidents .
The structure of the database table should be in this format.

CREATE TABLE incidents (
incident_time TEXT,
incident_number TEXT,
incident_location TEXT,
nature TEXT,
incident_ori TEXT
);
If needed so help to access sqlite3 you can check this link https://docs.python.org/3.8/library/sqlite3.html .

**populatedb():**

This function allows us to push all the data in the dataframe to the incidents table which we have created in NORMANPOLICE database.

**status():**

The status() function is used to print all the list of the nature of the incidents along with the number of times they have occurred. This list is sorted alphabetically and the nature and count is separated by a ‘|’ operator.


**Challenges:**

-	In one of the row the data gets into a next line which has to be handled correctly or else it would get as a separate data of next row in a list.
-	There are few extra data which has to be removed before forming it as a data frame and pushing it to the database.

**tests: **

#1.test_download:to check the data in the url is not empty
#2.test_extractincidents:to check if the rows and columns are same after reading the data
#3.test_createdb:to check if the incidents table is created 
#4.test_populatedb:to check if after reading the total number rows are same 
#5.test_status:to check if the database is not null

**External Resources:**

https://www.tutorialspoint.com/sqlite/sqlite_python.htm https://www.geeksforgeeks.org/list-methods-in-python-set-2-del-remove-sort-insert-pop-extend/ http://echrislynch.com/2018/07/13/turning-a-pdf-into-a-pandas-dataframe/
https://www.geeksforgeeks.org/break-list-chunks-size-n-python/ 
https://stackoverflow.com/questions/43314559/extracting-text-from-a-pdf-all-pages-and-output-file-using-python 






