# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 21:42:41 2020

@author: User
"""

from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
confusion_matrix(y_true, y_pred)