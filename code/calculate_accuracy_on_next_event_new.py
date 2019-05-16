'''
this script takes as input the output of evaluate_suffix_and_remaining_time.py
therefore, the latter needs to be executed first

Author: Niek Tax
'''

from __future__ import division
import unicodecsv
import csv
eventlog = "event_log.csv"
csvfile = open('output_files/results/suffix_and_remaining_time_%s' % eventlog, 'r')
#csvfile = open('output_files/results/next_activity_and_time_%s' % eventlog, 'r')
r = csv.reader(csvfile ,delimiter=',', quotechar='|')
#r = unicodecsv.reader(csvfile ,encoding='utf-8')
#r.next() # header
next(r, None)
next(r, None)
vals = dict()

for row in r:

    l = list()
    if row[0] in vals.keys():
        l = vals.get(row[0])
    if len(row[2])==0 and len(row[3])==0:
        l.append(1)
    elif len(row[2])==0 and len(row[3])>0:
        l.append(0)
    elif len(row[2])>0 and len(row[3])==0:
        l.append(0)
    else:
        l.append(int(row[2][0]==row[3][0]))
    vals[row[0]] = l
    #print(vals)
    next(r, None)
l2 = list()
for k in vals.keys():
    #print('{}: {}'.format(k, vals[k]))
    l2.extend(vals[k])
    res = sum(vals[k])/len(vals[k])
    print('{}: {}'.format(k, res))

print('total: {}'.format(sum(l2)/len(l2)))
