FROM python:3.6
#MAINTAINER alimoslehirad

# Creating Application Source Code Directory
RUN mkdir -p /k8s_production_mon/src
RUN mkdir -p /k8s_production_mon/files
#RUN mkdir -p /k8s_production_mon/src/app
# Setting Home Directory for containers
#WORKDIR /k8s_production_mon/src

# Installing python dependencies
#COPY requirements.txt /k8s_production_mon/src
#COPY main.py /k8s_production_mon/src
#COPY URLFileRead.py /k8s_production_mon/src
COPY URLs.txt /k8s_production_mon/files
COPY . /k8s_production_mon/src
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install requests
#RUN pip install threading
RUN pip install telegram
RUN pip install websocket-client
RUN pip install cherrypy
RUN pip install tinydb
# Copying src code to Container
#COPY . /k8s_production_mon/src/app

# Application Environment variables
ENV APP_ENV development
ENV APP_ENV_URL1 https://mon.qcluster.org
ENV APP_ENV_URL2 https://prometheus.qcluster.org
ENV APP_ENV_URL3 https://alertmanager.qcluster.org

RUN chmod  777 -R  /k8s_production_mon

# Exposing Ports
EXPOSE 5035

# Setting Persistent data
VOLUME ["/app-data"]
RUN chmod  777 -R /app-data
WORKDIR /k8s_production_mon/src
# Running Python Application
CMD ["python", "main.py"]
#STOPSIGNAL SIGTERM
# Specify the command to run when the container starts.
#CMD ["./start.sh"]
#RUN ./start.sh
