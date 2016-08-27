FROM python:3.5

RUN mkdir /code

COPY requirements.txt /code/
# Docker Python image doesn't like pkg-resources
RUN sed -i '/^pkg-resources.*/d' /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt

COPY . /code
COPY cmd.sh /

RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
RUN mkdir -p /var/run/uwsgi
RUN chown -R uwsgi:uwsgi /var/run/uwsgi
RUN mkdir -p /var/www/static
RUN chown -R uwsgi:uwsgi /var/www/static

USER uwsgi
CMD ["/cmd.sh"]
