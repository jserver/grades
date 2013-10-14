import os

from fabric.api import local

HOME = os.getenv("HOME")

def load_all():
    local('./manage.py loadactions %s/data/inspections/Action.txt' % HOME)
    local('./manage.py loadcuisines %s/data/inspections/Cuisine.txt' % HOME)
    local('./manage.py loadviolations %s/data/inspections/Violation.txt' % HOME)
    local('./manage.py loadextract %s/data/inspections/WebExtract.txt' % HOME)
