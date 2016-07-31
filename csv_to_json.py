# -*- coding: utf-8 -*-
import numpy as np
import codecs
import string
import json

def csv_to_json(filename):
    if filename == '必修_系訂選修.csv':
        filename = "data/" + filename
        arr = np.fromiter(codecs.open(filename, encoding="utf-8"), dtype="<U40")
        json_data = []
        size = arr[1:].size
        course = []
        for x in arr[1:]:
            x = string.replace(x, '\n', '')
            course.append( x.split(',') )
        course = np.array(course).reshape(size,3)
        name = np.unique(course[:,0][1:])
        for x in name:
            j = {'name':x,
                 'subcategories':[]}
            subcategories, idx = np.unique(course[course[:,0] == x][:,1], return_index=True)
            subcategories = course[course[:,0] == x][:,1][np.sort(idx)]
            for s in subcategories:
                classes = course[course[:,1] == s][:,2].tolist()
                sub = {'name':s,
                       'course':classes}
                j['subcategories'].append(sub)
            json_data.append(j)
        with open('api/course.json', 'w') as outfile:
            json.dump(json_data, outfile, indent=4)

if __name__ == '__main__':
    csv_to_json('必修_系訂選修.csv')
