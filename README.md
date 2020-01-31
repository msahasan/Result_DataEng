# Submission of Test Result
link : https://github.com/msahasan/Result_DataEng
## Section 1: Data pipeline
The script contains to process the data that will run on scheduled time interval
File name: data-processing.py 

`dataset_out.csv` will give result of after data processing done.

- Cron Job

Assign job to crontab on 1am everyday
assign following statement

0 1 * * * /usr/ibrahim/MLCode/Result_DataEng/datapro.sh

## Section 2: database
- Dockerfile contains basic script to run on docker container

- The car dealership database created in docker init.sql file
Dockerfile contains of information in basic script to run

- Entity relationship diagram file name is ER_Diagram.png

## Section 3: System Design
The simple design architecture of system design image processing in AWS services.
File name: System_Design.pptx