# action will be run in python3 container
FROM python:3
# copying requirements.txt and install the action dependencies
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
# validate-deploy.py is the file that will contain the codes that we want to run for this action.
COPY validate-deploy.py /script.py
# we will just run our validate-dgeploy.py as our docker entrypoint by python validate-deploy.py
CMD ["python", "-u", "/script.py"]