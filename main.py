
from interface import Interface




"""
This file contains only the code which is not posssible to run repeatedly in the app.
I.e. only the beginning and the end message.
All the rest is handled through Interface object, which then initializes other objects
(in this case Customer and Database).
"""
print()
print("***EVIDENCE POJISTENYCH***")
print()

Interface()

print('This is The End.')