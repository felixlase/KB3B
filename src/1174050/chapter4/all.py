# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 21:37:48 2020

@author: User
"""

import pandas as pd# untuk membaca file tex atau csv
data_forest = pd.read_csv("D:/SEMESTER 6/New folder/datakaryawan.csv")#membaca file csv menggunakan fungsi read csv dari padas
print(len(data_forest))#untuk melihat jumlah dari baris data yang telah di import
print(data_forest.head()) #untuk melihat lima baris pertama data yang telah di import
print(data_forest.shape)#untuk mengetahui banyak baris dan kolom dari data yang telah di import.
#In[2]: 
data_train = data_forest[:450]# memasukkan data training sebanyak 450 baris
data_tes = data_forest[450:]# memasukkan data tes sebanyak 50
