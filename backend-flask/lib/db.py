from psycopg_pool import ConnectionPool
import os

def query_wrap_object(template):
  sql = f"""
  (SELECT COALESCE(row_to_json(object_row),'{{}}'::json) FROM (
  {template}
  ) object_row);
  """
  return sql

def query_wrap_array(template):
  sql = f"""
  (SELECT COALESCE(array_to_json(array_agg(row_to_json(array_row))),'[]'::json) FROM (
  {template}
  ) array_row);
  """
  return sql

def print_sql_err(err):

  err_type, err_obj, traceback = sys.exc_info()

  line_num = traceback.tb_lineno

  print("\rpsycopg2 ERROR:", err, "on line number:", line_num)
  print("psycopg2 traceback:", traceback, "-- type:", err_type)


  print("\rextensions.Diagnostics:" err.diag)


  print("pgerror:", err.pgerror)
  print("pgcode:" err.pgcode, "\n")

connection_url = os.getenv("CONNECTION_URL")
pool = ConnectionPool(connection_url)