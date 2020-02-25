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
    json_dict_arr=None
    text_file=""
    with open('result.json', 'r') as f:
        json_dict_arr = json.load(f)
    
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
    
    output_file = open("output_json.txt", "w")
    n = output_file.write(text_file)
    output_file.close()




        


#parse_file_to_json("input.txt")

#parse_json_to_file("result.json")


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
