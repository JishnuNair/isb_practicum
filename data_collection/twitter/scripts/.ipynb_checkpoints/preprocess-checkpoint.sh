#!/bin/bash

file_dir="/home/jishnu/Documents/ISB/Term3/practicum/workspace/data_collection/data/daily_data"

latest_file=`find $file_dir -name "tweets_*" -print0 | xargs -0 ls -1 -t | head -1`

tr '\n' ' ' < $latest_file | sed -e "s/###TWEET_NO:/\n/g" > "${latest_file}_processed"

awk 'BEGIN{FS="###!###";OFS="###!###"}{gsub(/###TWEET_NO:/,"",$1);gsub(/USER:/,"",$2);gsub(/DATE_TIME:/,"",$3);gsub(/LOCATION:/,"",$4);gsub(/TWEET:/,"",$5);print}' "${latest_file}_processed" > tmp && mv tmp "${latest_file}_processed"