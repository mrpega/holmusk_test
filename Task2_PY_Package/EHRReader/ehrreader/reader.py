import psycopg2
import pandas.io.sql as sqlio
#import pandas.io.sql as psql
import logging
import sys
from dotenv import load_dotenv
import os

# can be configured to log to stdout and file
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# We create a class to hold all the functions for better maintability and modularity.
class Reader:
	
	# make connection to postgres and pass connection to function that requires it to query
	def init_conn(func):						
		def wrapper(self, conn_cursor, query):
			load_dotenv()
			connection = None
			try:
				connection = psycopg2.connect(
											user=os.environ['USER'],
											password=os.environ['PASSWORD'],
											host=os.environ['HOST'],
											port=os.environ['PORT'],
											database=os.environ['DATABASE']
											)
				logging.info('Connection established') 
				res = func(self, connection, query)
				return res
			except Exception as e:
				#logging.error(e.format_exc())
				print(e)
				logging.error("Error while fetching data from PostgreSQL")#, e)
				raise
			finally:
				# close connection if error or successfull call
				if connection:
					connection.close()
					logging.info('Connection closed')
		return wrapper

	# Function that queries the database based on an input string
	# use decorator to pass in db connections
	@init_conn
	def query_data(self, connection=None, query=None):
		logging.info('Querying data') 
		# read as pandas dataframe and return it
		results_df = sqlio.read_sql_query(query, connection)
		return results_df

	# Function that retrieves patients by IDs
	# use decorator to pass in db connections
	@init_conn
	def get_person(self, connection, patient_ids):
		if len(patient_ids) == 0:
			raise ValueError('Input list is empty!')

		#print([str(i) for i in set(patient_ids)])
		ids_str = ','.join([str(i) for i in set(patient_ids)])
		ids_str = '('+ids_str+')'
		query2 = f"select * from cdm_schema.person where person_id in {ids_str}"
		logging.info(query2)
		# read as pandas dataframe and return it
		results_df = sqlio.read_sql_query(query2, connection)
		return results_df

def main():
	read_obj = ReadEHR()
	query = "select * from cdm_schema.person"

	# for task 2.2
	res_df = read_obj.query_data(None,query)

	# for task 2.3
	# inserted mock data into DB, so there's only patientid==1
	res_df = read_obj.get_person(None, [1, 123, 456])


