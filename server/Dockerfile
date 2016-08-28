FROM python:3.5

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
# Docker Python image doesn't like pkg-resources
RUN sed -i '/^pkg-resources.*/d' requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code
COPY cmd.sh /

RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
RUN mkdir -p /var/run/adventurelookup
RUN chown -R uwsgi:uwsgi /var/run/adventurelookup
RUN mkdir -p /var/www/adventurelookup/static
RUN chown -R uwsgi:uwsgi /var/www/adventurelookup/static

USER uwsgi
CMD ["/cmd.sh"]
