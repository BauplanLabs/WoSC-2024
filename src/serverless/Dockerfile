FROM public.ecr.aws/lambda/python:3.9

RUN pip install prophet==1.1.5

COPY app.py ${LAMBDA_TASK_ROOT}

CMD [ "app.lambda_handler" ]
