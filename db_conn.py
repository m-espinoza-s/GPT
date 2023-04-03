import pymssql
import pandas as pd


class Innova:

    def __init__(self,usr,pwd):
        self.usr = usr
        self.pwd = pwd

    def innovacion(self,query):
        self.query=query
        conn=pymssql.connect(host=r'10.111.145.180\sqlinnovacion',user=self.usr,password=self.pwd,database='Innova')
        cur=conn.cursor()
        cur.execute(self.query)

        return pd.DataFrame(cur.fetchall(),columns=[i[0] for i in cur.description])
    

