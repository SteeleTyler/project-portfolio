### IP Lookup and Threading

This project explores the benefits of multithreading and programmatically identifying IP addresses.

I used the python module ipwhois and its IPWhois class. When you pass in an IP address to the IPWHois constructor, it
 collects public data regarding that address. 

One program uses multithreading and one does not. Often, the multithreading version is significantly faster. I 
actually found this to be an odd combination of lessons as calls to the network are fundamentally asynchronous and 
inconsistent, so sometimes the single-threaded program actually runs faster.

A great takeaway from this is the use of python's time module. Beyond timing multithreading, this can be used to test
 the efficiency of code and compare different approaches to the same problem. 