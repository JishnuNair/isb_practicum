#!/bin/bash

file_dir="/home/jishnu/Documents/ISB/Term3/practicum/workspace/data_collection/data/daily_data"

find $file_dir -name "*_tweets_*" -print0 | xargs -0 ls -1 -t | head -3 > "${file_dir}/files_tmp"

while read line; do
    tr '\n' ' ' < $line | sed -e "s/###TWEET_NO:/\n/g" > "${line}_processed"

    awk 'BEGIN{FS="###!###";OFS="###!###"}{gsub(/###TWEET_NO:/,"",$1);gsub(/USER:/,"",$2);gsub(/DATE_TIME:/,"",$3);gsub(/LOCATION:/,"",$4);gsub(/TWEET:/,"",$5);print}' "${line}_processed" > tmp && mv tmp "${line}_processed"
done<"${file_dir}/files_tmp"
rm "${file_dir}/files_tmp"