FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
COPY docker/wait-for-postgres.sh /docker/wait-for-postgres.sh
RUN chmod +x docker/wait-for-postgres.sh
# Set the timezone.
ENV TZ=Asia/Karachi
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone