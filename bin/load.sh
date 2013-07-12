#!/bin/bash
echo "Removing DB"
rm db/sql.db
./manage.py syncdb
echo "Actions..."
./manage.py loadactions ~/Downloads/nyc_rest/Action.txt
echo "Cuisine..."
./manage.py loadcuisines ~/Downloads/nyc_rest/Cuisine.txt
echo "Violation..."
./manage.py loadviolations ~/Downloads/nyc_rest/Violation.txt
echo "WebExtract..."
./manage.py loadextract ~/Downloads/nyc_rest/WebExtract.txt
