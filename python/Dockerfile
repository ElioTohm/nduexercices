FROM python:2.7

ADD . /

RUN pip install docopt

CMD [ "python", "./wordcount_mapreduce_parallel.py", ".", "1" ]
