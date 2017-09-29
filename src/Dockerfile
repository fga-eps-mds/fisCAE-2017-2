FROM django:onbuild
WORKDIR /usr/src/app
RUN pip install
RUN python manage.py migrate
CMD python manage.py runserver 0.0.0.0:$PORT

