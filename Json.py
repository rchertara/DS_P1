import sys
import json
import pickle
import argparse
import timeit
import os
from optparse import OptionParser  

from collections import OrderedDict
#
total_time_s=0
total_time_d=0
comma=","
colon=":"


def parse_file_to_json(file_name):
    jsonArr=[]
    f = open(file_name, "r")
    start=timeit.default_timer() 
    for line in f:
        
        firstPair=True
        HasEmail=True
        json_record=OrderedDict()
        first_name=None
        last_name=None
        email=None
        id_no=0
        course_marks=[]

        recordArr=line.split(colon)
        for el in recordArr: 
            fieldArr=el.split(comma)
            
            if firstPair:
                if len(fieldArr) == 4:
                    json_record["lastname"]=fieldArr[1]
                    json_record["firstname"]=fieldArr[2]
                    id_no=int(fieldArr[0].replace('-',''))
                    email=fieldArr[3]
                else:
                    json_record["lastname"]=fieldArr[1]
                    json_record["firstname"]=fieldArr[2]
                    id_no=int(fieldArr[0].replace('-',''))
                    HasEmail=False

                firstPair=False
            else:
                course_marks.append({"CourseScore":int(fieldArr[1]),"CourseName":fieldArr[0]})
        
        json_record["CourseMarks"]=course_marks
        json_record["id"]=id_no
        if HasEmail:
            json_record["email"]=email
        
        jsonArr.append(json_record)
    
    end=timeit.default_timer()
    diff=end-start
    with open('result.json', 'w') as wf:
        json.dump(jsonArr, wf,indent=4)
    
    millis =  diff * 1000
    return millis


    
def parse_json_to_file(file_name):
    json_dict_arr=None
    text_file=""
    with open('result.json', 'r') as f:
        json_dict_arr = json.load(f)
    
    start=timeit.default_timer()
    for json_dict in json_dict_arr:
        id=str(json_dict["id"])
        tid=id[0:3]+'-'+id[3:5]+'-'+id[5:]+','
        text_file+=tid
        text_file+=json_dict["lastname"]+','
        text_file+=json_dict["firstname"]
        if json_dict.get("email"):
            text_file+=','+json_dict["email"]
        course_marks=json_dict["CourseMarks"]
        for c in course_marks:
            text_file+=':'+c["CourseName"]+','+str(c["CourseScore"])
        text_file+='\n'
    
    end=timeit.default_timer()
    diff=end-start
    milis=( diff * 1000)
    output_file = open("output_json.txt", "w")
    n = output_file.write(text_file)
    output_file.close()
    return milis



parser = argparse.ArgumentParser()
parser.add_argument('-j','--jsonFile',help='Input File',required=False)
parser.add_argument('-s',help='Serialization Flag',action='store_true')
parser.add_argument('-d',help='Deserialization Flag',action='store_true')
parser.add_argument('-t',help="Time flag",action='store_true')
options= vars(parser.parse_args())

nameFile=options['jsonFile']
filestat=os.stat(nameFile)
time_s_j=0
time_d_j=0



if options['s'] and nameFile:
    parse_file_to_json(nameFile)
    print("Serialized Json")
if options['d'] and nameFile:
    parse_json_to_file(nameFile)
    print("De-Serialized Json")
if options['t'] and nameFile.endswith('.json'):
    time_d_j=parse_json_to_file(nameFile)
    print("File Size in bits:" +str(8*filestat.st_size))
    rate_d_j=(filestat.st_size*8) / time_d_j
    print("Time of JSON De-serialization:"+str(time_d_j)+',Rate of De-Serialization(bits/ms):'+str(rate_d_j))
if options['t'] and nameFile.endswith('.txt'):
    time_s_j=parse_file_to_json(nameFile)
    print("File Size in bits:" +str(8*filestat.st_size))
    rate_s_j= (filestat.st_size *8) / time_s_j
    print("Time of JSON Serialization:"+str(time_s_j)+',Rate of Serialization(bits/ms):'+str(rate_s_j))
