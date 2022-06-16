FROM python:3.6

ADD . .

RUN pip install jcs base58 graph-theory dotty-dict

CMD ["python", "-m", "unittest", "-v", "test/test_commitment.py"]