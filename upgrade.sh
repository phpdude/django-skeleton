#!/bin/sh

cd `dirname $0`

ENV_DIR='env'

if [ ! -d $ENV_DIR ]; then
    echo "Not found environment. Trying to create new one..."

    virtualenv env
fi

if [ ! -d $ENV_DIR ]; then
    echo "Not found virtualenv directory. Tried to create it, but looks without success. Upgrade aborted."
    exit -1
fi

source $ENV_DIR/bin/activate

pip install -U pip

pip install -r requirements.txt -U

python manage.py migrate