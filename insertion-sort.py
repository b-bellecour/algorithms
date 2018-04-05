#!/usr/bin/python
#-*- coding: utf-8 -*-
#vim: tabstop=2 expandtab shiftwidth=2 softtabstop=2

#----------------------------------------config------------------------------------------------#
import sys
#--------------------------------------prog start---------------------------------------------#
def insertion_sort(_list):                                            # sorting function
    count = 1
    for index in range(1,len(_list)):                                 # for loop, defining the length of array 
         current_value = _list[index]                                 # defining current value of the pointer
         position = index                                             # defining current position of the pointer

         while position > 0 and _list[position-1] > current_value:    # while loop, if the position is greater than 0 and if the pointer current_value is lesser than the previous pointer value then:
            _list[position] = _list[position-1]                       # the pointer value is replaced by the previous pointer value.
            position = position-1                                     # move the current pointer position to the previous one
         _list[position]= current_value                               # the pointer value is replaced by the current_value
         print "\ninsertion " + str(count)
         print _list
         count = count + 1

_list = [37,89,90,12,1,6,7,96,45,45,96,342,78,92,134,678,78,9,0,05,2343,15689765,367,876,945]
insertion_sort(_list)
print "\nDone\n"
     

