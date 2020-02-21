#!/bin/bash

if [ $1 = '-c' ]
then
    ##Compile the code
elif [ $1 = '-s' ]
then
    if [ $2 = '-p' ]
    then
        ###Serialize Protobuf
    elif [ $2 = '-j' ]
    then
        ##Serialize JSON
    fi
elif [ $1 = '-d' ]
then
    if [ $2 = '-j' ]
    then
        ##Deserialize JSON
    elif [ $2 = '-p' ]
    then
        ##Deserialize Protobuf
    fi
elif [ $1 = '-t' ]
then
    if [ $2 = '-j' ]
    then
        ##Metric measurment JSON
        Size_input_text=$(ls -nl $3 | awk '{print $5}')
        declare result=($(./json 3 $3))
        Serial_time=${result[0]}
        Deserial_time=${result[1]}
        Total_time=${result[2]}
        echo Total time is $Total_time ms
        Size_output_json=$(ls -nl results.json | awk '{print $5}')
        Ss=$(echo "scale=4;$Size_input_text/1000/$Serial_time" | bc -l)
        echo Speed of JSON Serialization $Ss kbps
        Sd=$(echo "scale=4;$Size_output_json/1000/$Deserial_time" | bc -l)
        echo Speed of JSON Deserialization $Sd kbps
    elif [ $2 = '-p' ]
    then
        ##Metric measurment protobuf
        Size_input_text=$(ls -nl $3 | awk '{print $5}')
        declare result=($(./proto 3 $3))
        Serial_time=${result[0]}
        Deserial_time=${result[1]}
        Total_time=${result[2]}
        echo Total time is $Total_time ms
        Size_output_proto=$(ls -nl result_protobuf | awk '{print $5}')
        Ss=$(echo "scale=4;$Size_input_text/1000/$Serial_time" | bc -l)
        echo Speed of PROTOBUF Serialization $Ss kbps
        Sd=$(echo "scale=4;$Size_output_proto/1000/$Deserial_time" | bc -l)
        echo Speed of PROTOBUF Deserialization $Sd kbps
    fi
fi
