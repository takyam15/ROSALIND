FROM python:3.7
ARG DIR_WORK=/work
WORKDIR ${DIR_WORK}
ARG REQ_TXT=requirements.txt
COPY ${REQ_TXT} ${DIR_WORK}/
RUN apt-get update && apt-get install -y libgomp1
RUN pip install --upgrade pip && \
    pip install --trusted-host pypi.python.org -r ${REQ_TXT}
