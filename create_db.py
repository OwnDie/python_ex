import os
import sqlite3

db_filename = 'dhcp_snooping.db'
schema_filename = 'dhcp_snooping_schema.sql'

def create_db(db_filename,schema_filename):
	db_exists = os.path.exists(db_filename)
	conn = sqlite3.connect(db_filename)

	if not db_exists:
	    print('Creating schema...')
	    with open(schema_filename, 'r') as f:
	        schema = f.read()
	    conn.executescript(schema)
	    print('Done')
	else:
	    print('Database alredy exists.')

if __name__ == '__main__':
	create_db(db_filename, schema_filename)