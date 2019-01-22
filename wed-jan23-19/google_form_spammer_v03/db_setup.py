import sqlite3

connect = sqlite3.connect('dummy_data.db')
c = connect.cursor()

try:
	c.execute("""CREATE TABLE DUMMY_DATA (
		name text,
		reg_no integer,
		roll_no integer,
		mob_no integer
	)""")
except sqlite3.OperationalError:
	None

# c.execute("""CREATE TABLE IF NOT EXIST DUMMY_DATA (
# 	name text,
# 	reg_no integer,
# 	roll_no integer,
# 	mob_no integer
# )""")

c.execute("INSERT INTO DUMMY_DATA VALUES ('Amir Khan', 11756893, 43, 9657894847)")
c.execute("SELECT * FROM DUMMY_DATA")
c.fetchall()

connect.commit()
connect.close()
