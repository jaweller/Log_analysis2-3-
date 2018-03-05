#!/usr/bin/env python

import psycopg2
from datetime import datetime

# Lists the three most popular articles
db = psycopg2.connect("dbname=news")
c = db.cursor()
c.execute("select * from most_pop")
print("Most popular articles:")
for (title, count) in c.fetchall():
    print("    {} - {} views".format(title, count))
print("-" * 70)
results = c.fetchall()
c.close

# lists top authors
db = psycopg2.connect("dbname=news")
c = db.cursor()
c.execute("select * from top_authors")
print("Top Authors:")
for (title, count) in c.fetchall():
    print("    {} - {} views".format(title, count))
print("-" * 70)
results = c.fetchall()
c.close

# Lists the day with the most errors
db = psycopg2.connect("dbname=news")
c = db.cursor()
c.execute("select * from er_percent")
print("Days with error percent higher than 1")
for (title, count) in c.fetchall():
    print("    {} - {} error_percent".format(title, count))
print("-" * 70)
results = c.fetchall()
