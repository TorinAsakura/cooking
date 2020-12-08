# -*- coding: utf-8 -*-
import datetime
import os
from django import template


register = template.Library()


try:
    import ipdb as pdb
except ImportError:   
    import pdb


class PdbNode(template.Node):
    def render(self, context):
        pdb.set_trace()
        return ''


@register.filter
def fromtimestamp(timestamp):
	return datetime.date.fromtimestamp(timestamp)


@register.tag
def pdb_debug(parser, token):
    return PdbNode()

@register.filter
def strstr(value):    
    return str(value)

@register.filter
def div( value, arg ):
    '''
    Divides the value; argument is the divisor.
    Returns empty string on any error.
    '''
    try:
        value = int( value )
        arg = int( arg )
        if arg: return value / arg
    except: pass
    return ''

from django.core.files.uploadedfile import InMemoryUploadedFile
from base64 import b64encode

@register.filter
def get_cached_image(widget):     
    if widget == None: 
        return None
    upFile = widget.value()
    if upFile: 
        if type(upFile) is InMemoryUploadedFile:
            data = upFile.read()
            encoded = b64encode(data)
            mime = "image/jpeg"
            mime = mime + ";" if mime else ";"
            return "data:%sbase64,%s" % (mime, encoded);
        prj_path = os.path.realpath(os.path.dirname(__file__)+"/../../..")            
        return str(widget.value().file).replace(prj_path, '')
    else:
        return None

@register.filter
def get_range( value ):
  """
    Filter - returns a list containing range made from given value
    Usage (in template):

    <ul>{% for i in 3|get_range %}
      <li>{{ i }}. Do something</li>
    {% endfor %}</ul>

    Results with the HTML:
    <ul>
      <li>0. Do something</li>
      <li>1. Do something</li>
      <li>2. Do something</li>
    </ul>

    Instead of 3 one may use the variable set in the views
  """
  return range( value )

@register.filter
def lookup(d, key):
    if len(d)>key:
        return d[key]
    else:
        return None

@register.filter
def gallery_image(d,key):
    if len(d)>key+1:
        return d[key+1].image
    else:
        return None

@register.filter
def ipdb( value ):
    import ipdb; ipdb.set_trace()
    return value


@register.filter
def get_dict_value_by_key(obj, key):
    return obj.get(key)


@register.filter
def split(string, separator):
    try:
        return string.split(separator)
    except Exception:
        return string


@register.simple_tag
def get_sort_link(request, srt, order):

    sort_part = 'sort=%s&order=%s' % (srt, order)

    href = ['']
    if 'sort' in str(request.get_full_path()):
        href = str(request.get_full_path()).split('sort')

    print request.get_full_path()

    if href[0]:
        return href[0]+sort_part
    else:
        if request.GET:
            return request.get_full_path() + '&%s' % sort_part
        else:
            return '?%s' % sort_part