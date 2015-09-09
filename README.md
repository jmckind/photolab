# PhotoLab

A simple photo gallery application.

## Development

Check out the source code to a directory on your local machine. We will refer to this location as the `<PROJECT_DIR>`.

    $ git clone https://github.com/jmckind/photolab.git

Setup the virtual environment and dependencies.

    $ cd <PROJECT_DIR>/photolab
    $ mkvirtualenv photolab
    $ pip install -r requirements.txt

Once the dependencies have been installed, start the development server and get to work.

    $ ./manage.py runserver 0.0.0.0:8080

This will start the development server on the local machine, listening on port 8080. You should be able to access the application at [http://localhost:8080/](http://localhost:8080).
