FROM registry.access.redhat.com/ubi8/ubi
RUN yum -y install python3 python3-devel gcc make lsof
RUN pip3 install fastapi  "uvicorn[standard]"
RUN mkdir /app
WORKDIR /app
COPY app.py app.py
EXPOSE 8000
CMD uvicorn app:app --host 0.0.0.0 --port 8000