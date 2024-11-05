#!/bin/bash

function create_app {
  python3 manage.py startapp $1;
  mv $1 apps/$1;
  cd apps/$1;
  mkdir views && touch views/__init__.py && mv views.py views/;
  mkdir urls && touch urls/__init__.py;
  mkdir models && touch models/__init__.py && mv models.py models/;
  mkdir performs && touch performs/__init__.py;
  mkdir serializers && touch serializers/__init__.py;
  cd ../..;
  python3 app_fixer.py $1;
}

function clear_migrations {
  rm -rf apps/$1/migrations/ && mkdir apps/$1/migrations && touch apps/$1/migrations/__init__.py;
}

case $1 in
  'app')
    echo $1;
    create_app ${@:2};
  ;;
  'clear')
    if [ $2 == 'mig' ]; then
      if [ $3 == 'all' ]; then
        python3 app_fixer.py clear_migrations;
      else
        clear_migrations $3;
      fi
    else
      python3 app_fixer.py clear;
    fi
  ;;
  *)
    python3 manage.py ${@:1};
  ;;
esac