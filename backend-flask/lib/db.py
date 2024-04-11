from psycopg_pool import ConnectionPool
import os
import re
import sys

class Db:
  def __init__(self):
    self.init_pool()

  def init_pool(self)
    connection_url = os.getenv("CONNECTION_URL")
    self.pool = ConnectionPool(connection_url)
  
  # we want to commit data such as insert
  # be sure to check for RETURNING in all uppercases
  def query_commit(self,sql,params):
    print("SQL STATEMENT-[commit with returning]------")
    print(sql + "\n")
    
    pattern = r"\bRETURNING\b"
    is_returning_id = re.search(pattern, sql)
    
    try:
      conn = self.pool.connection()
      cur = conn.cursor()
      cur.execute(sql, params)
      if is_returning_id:
        returning_id_id = cur.fetchone()[0]  
      conn.commit()
      if is_returning_id:
        return returning_id
    except Exception as err
      self.print_sql_err(err)
      #conn.rollback()
    
  # when we want to return a json object
  def query_array_json(self,sql):
    print("SQL STATEMENT-[array]-----")
    print(sql + "\n")
    wrapped_sql = self.query_wrap_array(sql)
    with self.pool.connection() as conn:
        with conn.cursor() as cur:
          cur.execute(wrapped_sql)
          # this will return a tuple
          # the first field being the data
          json = cur.fetchone()
          return json[0]

  # When we want to return an array of json objects
  def query_object_json(self,sql):
    print("SQL STATEMENT-[object]-----")
    print(sql + "\n")
    wrapped_sql = self.query_wrap_object(sql)
    with self.pool.connection() as conn:
        with conn.cursor() as cur:
          cur.execute(wrapped_sql)
          # this will return a tuple
          # the first field being the data
          json = cur.fetchone()
          return json[0]


  def query_wrap_object(self,template):
    sql = f"""
    (SELECT COALESCE(row_to_json(object_row),'{{}}'::json) FROM (
    {template}
    ) object_row);
    """
    return sql

  def query_wrap_array(self,template):
    sql = f"""
    (SELECT COALESCE(array_to_json(array_agg(row_to_json(array_row))),'[]'::json) FROM (
    {template}
    ) array_row);
    """
    return sql

  def print_sql_err(self, err):

    err_type, err_obj, traceback = sys.exc_info()

    line_num = traceback.tb_lineno

    print("\rpsycopg2 ERROR:", err, "on line number:", line_num)
    print("psycopg2 traceback:", traceback, "-- type:", err_type)

    #print("\rextensions.Diagnostics:" err.diag)

    print("pgerror:", err.pgerror)
    print("pgcode:" err.pgcode, "\n")

db = Db()

