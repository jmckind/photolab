SHELL := /bin/bash

HOST_IP=0.0.0.0
HOST_PORT=8080
LOCAL_SETTINGS=photolab/local_settings.py
MEDIA_DIR=media
VENV=.venv
VENV_ACTIVATE=source $(VENV)/bin/activate

setup:
	test -d $(VENV) || virtualenv $(VENV) --no-site-packages
	./$(VENV)/bin/pip install -r requirements.txt
	test -d $(LOCAL_SETTINGS) || touch $(LOCAL_SETTINGS)
	test -d $(MEDIA_DIR) || mkdir -p $(MEDIA_DIR)
	$(VENV_ACTIVATE) && python manage.py migrate --noinput
	$(VENV_ACTIVATE) && python manage.py collectstatic --noinput

run:
	$(VENV_ACTIVATE) && python manage.py runserver $(HOST_IP):$(HOST_PORT)

clean:
	rm -fr $(VENV)
	rm -fr *.sqlite3
	rm -fr media static
