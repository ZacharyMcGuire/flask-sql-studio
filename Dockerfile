FROM python:slim
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apt-get update && \
    apt-get install -y gnupg curl && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install msodbcsql17 -y && \
    apt-get install -y gcc python3-dev python3-pip && \
    apt-get install -y libxml2-dev libxslt1-dev zlib1g-dev g++ && \
    apt-get install -y tdsodbc unixodbc-dev && \
    apt-get install -y gcc && \
    apt-get clean -y
# RUN apt-get update && \
#     apt-get install --no-install-recommends -y python && \
#     apt-get clean && rm -rf /var/lib/apt/lists/*
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
RUN odbcinst -i -s -f db.cfg -l
CMD ["flask", "run"]