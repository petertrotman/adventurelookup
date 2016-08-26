FROM python:3.5

RUN mkdir /code
COPY requirements.txt /code/

WORKDIR /code
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code
COPY cmd.sh /

RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
RUN mkdir -p /var/run/uwsgi
RUN chown -R uwsgi:uwsgi /var/run/uwsgi

USER uwsgi
CMD ["/cmd.sh"]
