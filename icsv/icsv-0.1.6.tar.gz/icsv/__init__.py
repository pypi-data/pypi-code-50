#!/usr/bin/env python3

import csv

class reader(object):
   '''
      A simple class used to perform read operations
      on a csv file.
   '''

   def read(self, csv_file):
      '''
         simply read a csv file and return its contents
      '''

      with open(csv_file, 'r') as f:
        cs = csv.reader(f)

        cs = [row for row in cs]

      df = dict()
      for key in cs[0]:
         df[key] = []

      df_keys = [key for key in df.keys()]
      for row in cs[1: ]:
         for i, col in enumerate(row):
            df[df_keys[i]].append(col)

      return df

class writer(object):
   '''
      Contains all methods designed to make
      creating csv files a breeze
   '''
   def __init__(self):
      pass

   def write(self, filename: str, data: dict):
      '''
         Create a csv file from data

         `param`:
            filename - The full path where you want to save the csv
         `param`:
            data - A dictionary containing the data to be exported to csv
      '''
      keys = [x for x in data.keys()]
      with open(filename, 'w') as f:
         cols = ','.join(keys)
         f.write(cols+'\n')

         total_rows = len(data[keys[0]])

         for t in range(total_rows):
            line = []
            for k in keys:
               line.append(data[k][t])
            row = ','.join(line)
            f.write(row+'\n')

      return True