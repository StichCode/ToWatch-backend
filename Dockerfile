FROM debian

RUN apt-get update -y && apt-get install -y python3 python3-venv python3-pip python3-dev build-essential

RUN mkdir /toWatch
COPY . /toWatch
WORKDIR /toWatch
RUN pip3 install -r requirments.txt
ENTRYPOINT ["python3", "-m", "flask", "run", "-h", "0.0.0.0", "-p", "8080"]