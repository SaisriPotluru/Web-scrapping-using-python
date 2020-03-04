import urllib.request
import PyPDF2
import urllib
import tempfile
import re
import sqlite3
import argparse
import pandas as pd
#to divide the list as list of lists
def divide_chunks(l, n): 
      
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 
  

#fetch incidents
def fetchincidents(url):

    data = urllib.request.urlopen(url).read() #the content is stored in the data 
    return data



#extract incidents
def extractincidents(data):
    temp=tempfile.TemporaryFile() #the data is stored in temp 
    temp.write(data)
    temp.seek(0)
    pdfReader = PyPDF2.pdf.PdfFileReader(temp) #to read the data
    number_of_pages =pdfReader.getNumPages() #to get the count of total number of pages in pdf
    h1 = []
    for pn in range(number_of_pages): #loop for getting all the data in the pdf
        p=pdfReader.getPage(pn)
        pagecontent=p.extractText() 
    #     print(repr(pagecontent))
        if pn == 0:   #for the first page
            pagecontent = pagecontent.replace(' \n',' ')
            pagecontent = pagecontent.split('\n')[5:-3] #the headings and the extra strings are deleted


    #         print(pagecontent)
        elif pn == (number_of_pages-1): # for the last page 
            pagecontent = pagecontent.replace(' \n',' ')
            pagecontent = pagecontent.split('\n')[:-2] #the extra string of date is removed

    #         print(pagecontent)
        else :     #for all other pages
            pagecontent = pagecontent.replace(' \n',' ')
            pagecontent = pagecontent.split('\n')[:-1] #for each of the page an extra list is formed which is removed

        h = list(divide_chunks(pagecontent, 5)) #the list is formed as a list of list of 5
    #     print (h)      
        h1.extend(h)
        dfFULLx = pd.DataFrame.from_records(h1,columns=('incident_time','incident_number','incident_location','nature','incident_ori'))
        
    return  dfFULLx



#create db
def createdb():
    conn = sqlite3.connect('NORMANPOLICE.db') #connecting to the db
    c = conn.cursor()
    c.executescript('drop table if exists incidents') #if there is a table incidents exists then its droped prior to creation
    c.execute('''CREATE TABLE incidents (
                incident_time TEXT,
                incident_number TEXT,
                incident_location TEXT,
                nature TEXT,
                incident_ori TEXT);
              ''')
    

#populate db
def populatedb(db,table):
    conn = sqlite3.connect(db)  #forming the connection
    c = conn.cursor()
    table.to_sql('incidents', con=conn, index=False, if_exists='replace')  #to push the data in table

    

# Print Status
def status(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("SELECT nature, count(*) as count FROM incidents GROUP BY nature order by nature ") #query to get the nature with count
    result=c.fetchall()
#    print(result)
    result1=['|'.join(str(n) for n in x) for x in result]  #replacing comma with '|' operator
#    print(result1)
    return result1 



def main(url):
    # Download data
    data=fetchincidents(url) #calling the functions

    # Extract Data
    incidents = extractincidents(data)
	
    # Create Dataase
    createdb()
	
    # Insert Data
    populatedb('NORMANPOLICE.db', incidents)
	
    # Print Status
    print(status('NORMANPOLICE.db'))
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, 
                         help="The incidents summary url.")
     
    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)

