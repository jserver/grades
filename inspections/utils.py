def clean(field):
    return field.decode('iso-8859-1').encode('utf8').strip()
