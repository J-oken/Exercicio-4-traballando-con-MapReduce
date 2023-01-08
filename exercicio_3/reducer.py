#!/usr/bin/python
import sys

dict_data={}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    if thisKey not in dict_data.keys():
        dict_data[thisKey]=thisSale
    elif float(dict_data[thisKey])<float(thisSale):
        dict_data[thisKey]=thisSale
    else:
        pass;

for i, j in dict_data.items():
	print(i+"\t"+j)
