

if [ $1 = '-s' ]
then
    ##Compile the code
    if [ $2 = '-p' ]
    then

    python3 proto.py -s -p $3
        ###Serialize Protobuf
    elif [ $2 = '-j' ]
    then
        ##Serialize JSON
    python3 Json.py -s -j $3
    fi
elif [ $1 = '-d' ]
then
    if [ $2 = '-j' ]
    then
    python3 Json.py -d -j $3
        ##Deserialize JSON
    elif [ $2 = '-p' ]
    then
        ##Deserialize Protobuf
    python3 proto.py -d -p $3
    fi
elif [ $1 = '-t' ]
then
    if [ $2 = '-j' ]
    then
        ##Metric measurment JSON
        python3 Json.py -t -j $3
        
    elif [ $2 = '-p' ]
    then
        ##Metric measurment protobuf
        python3 Json.py -t -p $3
        
    fi
fi
