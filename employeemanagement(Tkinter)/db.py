import sqlite3
class Database:
    def __init__(self,db):#when we create object for database for the given table connection is made and cursor is also made
        self.con=sqlite3.connect(db)#con is variable we are connect function to connect database called db
        self.cur=self.con.cursor()#wecan use cursor for all things loike insert,delete,update and many if we put this inside
        #constructor  if the database exists it will not create or else it will create
        sql="""
        CREATE TABLE IF NOT EXISTS employees(   
         id Integer Primary Key,
         name text,
         age text,
         doj text,
         email text,
         gender text,
         contact text,
         address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

#insert function
    def insert(self, name,age,doj,email,gender,contact,address):
        self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,?)",
                     (name,age,doj,email,gender,contact,address))
        self.con.commit()
#fetch all data from DB
    def fetch(self):
        self.cur.execute("select * from employees")
        rows=self.cur.fetchall()
       # print(rows)
        return  rows
    #delete a rec
    def remove(self,id,):
       self.cur.execute("delete from employees where id=?",(id,))#we hv to put comma or else it is considered as string

       self.con.commit()
    #update a record
    def update(self,id,name,age,doj,email,gender,contact,address):
        self.cur.execute("update employees set name=?, age=?, doj=?, email=?, gender=?, contact=?, address=? where id=? ",
                         (name, age, doj, email, gender, contact, address,id))
        self.con.commit()
