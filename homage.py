__author__ = 'danga_000'
from models import general_param
from data import db

from models import general_param
gps = general_param.get_general_params()
g = gps[0]
print g.val
# database = db.Database()
#
# #CleanUp Operation
# del_query = "DELETE FROM basic_python_database"
# db.insert(del_query)
#
# # Data Insert into the table
# query = """
#     INSERT INTO basic_python_database
#     (`name`, `age`)
#     VALUES
#     ('Mike', 21),
#     ('Michael', 21),
#     ('Imran', 21)
#     """
#
# # db.query(query)
# db.insert(query)
#
# # Data retrieved from the table
# select_query = """
#     SELECT * FROM basic_python_database
#     WHERE age = 21
#     """
#
# people = db.query(select_query)
#
# for person in people:
#     print "Found %s " % person['name']