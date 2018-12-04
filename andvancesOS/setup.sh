#!/bin/sh

# this is the setup to create a large file and check python dependencies
# docker and coker-compose checks are available but not required for testing

# append to file to make it a bit bigger
a=0

# remove temp.txt file if exists
rm temp.txt
while [ $a -lt 10000 ]
   do
      echo $a
      # cat 1513-0.txt >> python/temp.txt
      cat test.txt >> temp.txt
      a=`expr $a + 1`
   done

if [[ $(python --version 2>&1) =~ 2\.7 ]]
    then
        echo "python version 2.7 is installed"
    else
        echo "python version 2.7 is not installed please install and run setup again"
fi

if [[ $(docker --version 2>&1) =~ 18\.09 ]]
   then
      echo "docker is installed and is in the required version"
   else
      echo "docker is not installed or wrong version"
fi

if [[ $(docker-compose --version 2>&1) =~ 1\.21 ]]
   then
      echo "docker-compose is installed feel free to use the example docker-compose.yml"
   else  
      echo "docker-compose is not installed or not in the correct version"
      echo "you cannot use the docker-compose example"
      echo "please check the docker-compose file and execute the command in the local terminal"
fi