ARG PYTHON_VERSION=3.8

FROM public.ecr.aws/lambda/python:${PYTHON_VERSION}
ENV ADMIN_USER=$ADMIN_USER
ENV ADMIN_PASS=$ADMIN_PASS

COPY requirements.txt ${LAMBDA_TASK_ROOT}

RUN python3 -m ensurepip
RUN pip install -r requirements.txt

ADD api/main.py ${LAMBDA_TASK_ROOT}

CMD ["main.handler"]