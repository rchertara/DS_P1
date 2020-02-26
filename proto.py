import sys
import protocol_defn_pb2 as proto
import argparse

total_time_s=0
total_time_d=0
comma=","
colon=":"

def add_student(student,data):
    if(len(data)==4):
        student.email=data[3]

    student.id=data[0].replace('-','')
    student.lastname=data[1]
    student.firstname=data[2]
    
    return

def add_courseMarks(marks,data):
    marks.name=data[0]
    marks.score=int(data[1])
    return 


def parse_file_to_proto(file_name):
    result = proto.Result()
    f = open(file_name, "r")
    count=0
    for line in f:
        firstPair=True
        recordArr=line.split(colon)
        for el in recordArr:
            fieldArr=el.split(comma)
            if firstPair:
                add_student(result.student.add(),fieldArr)
                firstPair=False
            else:
                add_courseMarks(result.student[count].marks.add(),fieldArr)
        
        count+=1#next student
    f.close()

    wf = open("result_protobuf.proto", "wb")
    wf.write(result.SerializeToString())
    wf.close()
    return 

def parse_proto_to_file(file_name):
   text_file=""
   result = proto.Result()
   f = open(file_name, "rb")
   result.ParseFromString(f.read())
   f.close()
   for student in result.student:
       i=str(student.id)
       tid=i[0:3]+'-'+i[3:5]+'-'+i[5:]+','
       text_file+=tid
       text_file+=student.lastname+','
       text_file+=student.firstname
       if student.email:
           text_file+=','+student.email
       for course in student.marks:
            text_file+=':'+course.name+','+str(course.score)
       text_file+='\n'
    
   output_file=open("output_protobuf.txt","w")
   n=output_file.write(text_file)
   output_file.close()




parser = argparse.ArgumentParser()
parser.add_argument('-p','--protoFile',help='Input File',required=False)
parser.add_argument('-s',help='Serialization Flag',action='store_true')
parser.add_argument('-d',help='Deserialization Flag',action='store_true')

options= vars(parser.parse_args())

print(options)
nameFile=options['protoFile']
if options['s'] and nameFile:
    parse_file_to_proto(nameFile)
if options['d'] and nameFile:
    parse_proto_to_file(nameFile)





