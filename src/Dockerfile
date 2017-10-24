FROM django:onbuild
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
RUN python manage.py migrate

