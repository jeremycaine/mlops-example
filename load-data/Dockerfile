FROM python:3
ADD load-data.py /
RUN pip install tensorflow
RUN pip install pandas
RUN pip install numpy
RUN pip install matplotlib

CMD [ "python", "./load-data.py"]