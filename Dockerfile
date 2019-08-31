FROM amazonlinux:2018.03

RUN yum update -y
RUN yum install -y curl unzip \
    python35 python35-setuptools python35-devel git

RUN yum install -y gcc libffi-devel python-devel openssl-devel

RUN rm /usr/bin/python && ln -s /usr/bin/python3 /usr/bin/python

RUN curl -o /tmp/get_pip.py https://bootstrap.pypa.io/get-pip.py
RUN python35 /tmp/get_pip.py
RUN pip install --upgrade pip

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /usr/local/src/pygeohash4
