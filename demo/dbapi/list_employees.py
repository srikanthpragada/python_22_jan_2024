# List employees from EMPLOYEES table of hr.db

import sqlite3
import dbutil

try:
    con = sqlite3.connect(dbutil.DBNAME)
    cur = con.cursor()
    try:
        cur.execute("select * from employees order by sal ")  # SQL Command

        for id, name, job, salary in cur.fetchall():
            print(f"{id:2} {name:20} {job:10} {salary:10}")
    except Exception as ex:
        print("Error while executing SELECT command : ", ex)

    cur.close()
    con.close()
except Exception as ex:
    print('Error :', ex)
