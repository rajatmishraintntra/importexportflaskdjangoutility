#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 10:19:25 2021

@author: er
"""

import pandas as pd 
from import_export.Import_export import ImportExportUtility
data=ImportExportUtility()
final=data.import_file(constr="sqlite:///Chinook_Sqlite.sqlite",table_name="Album",excel_sheet=df)
