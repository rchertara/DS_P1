import sys
import json
import pickle


from collections import OrderedDict
#
total_time_s=0
total_time_d=0
comma=","
colon=":"


def parse_file_to_json(file_name):
    jsonArr=[]
    f = open(file_name, "r")
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
    
    with open('result.json', 'w') as wf:
        json.dump(jsonArr, wf,indent=4)
    
    return 

    
def parse_json_to_file(file_name):
    
    return

parse_file_to_json("input.txt")

# if (len(sys.argv)!=3 ):
#     print('invalid amount of arg parameters')
#     exit()
# if (int(sys.argv[1]) == 1):#may not be argv[1] instead argv[0]
#     parse_file_to_json(sys.argv[2])
# if (int(sys.argv[1]) == 2):
#     parse_json_to_file(sys.argv[2])
# if (int(sys.argv[1]) == 3):
#     parse_file_to_json(sys.argv[2])
#     parse_json_to_file("results.json")
#     #time done here 
