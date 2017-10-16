import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

courses = csv.DictReader(open("data/courses.csv"))
people = csv.DictReader(open("data/peeps.csv"))

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE


command = ""          #put SQL statement in this string
c.execute(command)    #run SQL statement

#==========================================================
db.commit() #save changes
db.close()  #close database


