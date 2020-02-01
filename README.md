# Submission of Test Result

## Section 1: Data pipeline
The script contains to process the csv data `data-processing.py` 

After data processing done, the resultset will be like this `dataset_out.csv`.

-- Cron Job:

Assign job to crontab on 1am everyday, that will run on scheduled time interval. 
add following statement in crobtab

0 1 * * * /usr/ibrahim/MLCode/Result_DataEng/datapro.sh

`datapro.sh` bash file contains python script to run

## Section 2: database
- `Dockerfile` contains basic script to run on docker container

- The car dealership database created in docker using initiliaze script `init.sql`

- Entity relationship diagram file name is `ER_Diagram.png`

## Section 3: System Design
The simple design architecture of system design image processing in AWS services.
File name: `System_Design.pptx`