from django.utils.six.moves.urllib import parse as urlparse
from io import BytesIO, StringIO
from django.utils import six

try:
    from django.utils.deconstruct import deconstructible
except ImportError: # Django 1.7+ migrations
    deconstructible = lambda klass, *args, **kwargs: klass


def getFile(content):
    if six.PY3:
        stream_class = StringIO if isinstance(content, six.text_type) else BytesIO
    else:
        stream_class = BytesIO
        content = force_bytes(content)
    return stream_class(content)
