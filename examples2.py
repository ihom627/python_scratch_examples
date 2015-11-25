#!/usr/bin/env python


#python shares references to a single collection
a = [0 , 1]
b = a
print a
print b
a[0] = -1
print a
print b


#difference between range and xrange
#range returns an entire list in memory 
#xrange returns a sequence object that evaluates lazily by returning one by one
#use xrange when working on a massive collection and are memory sensitive
#use range if you are going to iterate over many times because it is cached




