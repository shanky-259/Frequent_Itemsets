# Frequnet_Itemsets
Finding Frequent Itemsets using Apriori and PCY algorithm.

This project is built with the motive of finding frequent
items of size K(=1,2,3,..) from a large dataset using the 
Apriori algorithm.Apriori Algorithm enhances the processing
speed of finding the frequent items because it works on the 
principle of montonocity.This is different from how a Naive 
Bayes algorithm would find frequent items.
The running/processing time of this code is enhanced by a 
factor of ~10 % by deploying PCY algorithm which uses a 
bitmap in the second pass of going over the baskets.The 
PCY algorithm uses the spare main memory in the first pass
which is not done in Apriori algorithm to store buckets and 
hash items to the buckets.


