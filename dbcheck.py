#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 10:35:19 2021

@author: er
"""

import pandas as pd 
import sqlite3

con=sqlite3.connect("Chinook_Sqlite.sqlite")

df=pd.read_sql_query("select * from Album", con)

print(df)