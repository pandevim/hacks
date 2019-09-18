from faker import Faker
from faker.providers import phone_number
import sqlite3
import random
import string

fake = Faker('hi_IN')
fake.add_provider(phone_number)

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
	pass

c.execute("""CREATE TABLE IF NOT EXIST DUMMY_DATA (
	name text,
	reg_no integer,
	roll_no integer,
	mob_no integer
)""")

for _ in range(0, 10):
	c.execute("INSERT INTO DUMMY_DATA VALUES (?,?,?,?)" , (
		fake.first_name() + ' ' + fake.last_name(),
		str(random.randint(11700000, 11799999)),
		str(random.randint(1, 68)),
		fake.phone_number().replace('-', '').replace('+', '').replace(' ', '')
	))

# c.execute("DELETE FROM DUMMY_DATA")
c.execute("SELECT * FROM DUMMY_DATA")
input_data = c.fetchall()



connect.commit()
connect.close()
