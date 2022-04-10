#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 18:58:56 2022

@author: priyankadas
"""

from tkinter import *
root = Tk()

root.title("Bag")
root.geometry("600x600")

label_series = Label(root)
label_flower = Label(root)
label_spirals = Label(root)
label_sum = Label(root)
input_sum = Entry(root)

def Fibonacci():
    number = int(input_sum.get())
    counter = 1
    number_un = 0
    number_duex = 1
    sumone = 0
    sumone2 = 0
    
    while counter <= number:
        print(number_un, number_duex, sumone, sumone2)
        label_series["text"] += str(sumone) + " "
        label_flower["text"] = "flower has bloomed"
        counter = counter + 1
        sumone = number_un + number_duex
        number_un = number_duex
        number_duex = sumone
        sumone2 = sumone2 + sumone
        label_spirals["text"] = "spirals in right directions are " + str(number_un) + " spirals in the left directions are " + str(number_duex) + "total spirals are" + str(sumone)
        label_sum["text"] = "Fibonacci sum : " + str(sumone2)
button = Button(root, command = Fibonacci, text = "Generate the sequence")
button.pack()
label_flower.pack()
label_series.pack()
label_spirals.pack()
label_sum.pack()
input_sum.pack()
        

root.mainloop()

#0 = x 1 = y 1 = sumone 2 3 5