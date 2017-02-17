FROM rallyforge/rally:latest
MAINTAINER Tetiana Korchak

RUN rally deployment create --fromenv --name test_rally


RUN git clone https://github.com/kotavi/mos-initial-check-rally-scenarios.git
RUN cd mos-initial-check-rally-scenarios
RUN source openrc

