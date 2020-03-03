import urllib.request
import PyPDF2
import urllib
import tempfile
import re
import sqlite3
import argparse
import pandas as pd

def divide_chunks(l, n): 
      
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 
  

#fetch incidents
def fetchincidents(url):

    data = urllib.request.urlopen(url).read()
    return data



#extract incidents
def extractincidents(data):
    temp=tempfile.TemporaryFile()
    temp.write(data)
    temp.seek(0)
    pdfReader = PyPDF2.pdf.PdfFileReader(temp)
    number_of_pages =pdfReader.getNumPages()
    h1 = []
    for pn in range(number_of_pages):
        p=pdfReader.getPage(pn)
        pagecontent=p.extractText() 
    #     print(repr(pagecontent))
        if pn == 0:
            pagecontent = pagecontent.replace(' \n',' ')
            pagecontent = pagecontent.split('\n')[5:-3]


    #         print(pagecontent)
        elif pn == (number_of_pages-1):
            pagecontent = pagecontent.replace(' \n',' ')
            pagecontent = pagecontent.split('\n')[:-2]

    #         print(pagecontent)
        else :
            pagecontent = pagecontent.replace(' \n',' ')
            pagecontent = pagecontent.split('\n')[:-1]

        h = list(divide_chunks(pagecontent, 5)) 
    #     print (h)      
        h1.extend(h)
        dfFULLx = pd.DataFrame.from_records(h1,columns=('incident_time','incident_number','incident_location','nature','incident_ori'))
        
    return  dfFULLx



#create db
def createdb():
    conn = sqlite3.connect('NORMANPOLICE.db')
    c = conn.cursor()
    c.executescript('drop table if exists incidents')
    c.execute('''CREATE TABLE incidents (
                incident_time TEXT,
                incident_number TEXT,
                incident_location TEXT,
                nature TEXT,
                incident_ori TEXT);
              ''')
    

#populate db
def populatedb(db,table):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    table.to_sql('incidents', con=conn, index=False, if_exists='replace')

    

# Print Status
def status(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("SELECT nature, count(*) as count FROM incidents GROUP BY nature order by nature ")
    result=c.fetchall()
#    print(result)
    result1=['|'.join(str(n) for n in x) for x in result]
#    print(result1)
    return result1 



def main(url):
    # Download data
    data=fetchincidents(url)

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

