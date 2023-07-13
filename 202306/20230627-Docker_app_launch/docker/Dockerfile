
# FROM python:3.9 AS test-stage
# WORKDIR /app
# COPY requirements.txt .
# RUN pip install -r requirements.txt
# COPY test_translator.py .
# CMD python -m unittest test_translator.py



FROM python:3.9
WORKDIR /app
COPY requirements.txt . 
RUN pip install -r requirements.txt
COPY source/ . 
CMD python -m unittest; python main.py