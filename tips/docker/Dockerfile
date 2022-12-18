FROM python:3
RUN pip install --upgrade pip
WORKDIR /usr/src/app
COPY . ./
RUN pip install -r requirements.txt
COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]