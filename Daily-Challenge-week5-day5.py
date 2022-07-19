# Importing the libraries

from urllib.request import urlopen
from time import time

# URL WEBSITE
website = urlopen('https://www.google.fr/')

# Return the number of seconds
# passed since epoch
open_time = time()

# Read the complete website
#The read() method returns the specified number of bytes from 
# the file. Default is -1 which means the whole file.
output = website.read()

# Return the number of seconds 
# passed since epoch
#Pythom time method time() returns the time as a floating 
# point number expressed in seconds since the epoch
close_time = time()

# Close the website
#The close() method closes an open file.
website.close()

# Subtract and print the open time 
# of website from close time
print('The loading time of website is',round(close_time-open_time,3),'seconds')
