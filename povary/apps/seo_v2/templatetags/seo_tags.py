from django import template
from django.db import models
from django.utils.safestring import mark_safe
from seo_v2.models import *

register = template.Library()


class SeoNode(template.Node):
    def __init__(self, kind, target, var_name, with_html=False):
        self.kind = kind
        self.target = target
        self.var_name = var_name
        self.with_html = with_html

    def render(self, context):
        target = template.Variable(self.target).resolve(context) if self.target is not None else None
        template_context = template.RequestContext(context["request"], {})
        template_context.update(context)
        url = context["request"].path # get current url

        try:
            if self.target is None:
                # seo by url
                template_obj = SeoTemplate.objects.for_url(url)
            elif isinstance(target, models.Model):
                # seo by object
                try:
                    template_obj = SeoTemplate.objects.for_object(target)
                    if not getattr(template_obj, self.kind):
                        raise SeoTemplate.DoesNotExist()
                except SeoTemplate.DoesNotExist:
                    
                    template_obj = SeoTemplate.objects.for_url(url)
                else:
                    template_context["seo_obj"] = target
            else:
                # seo by target
                template_obj = SeoTemplate.objects.for_target(target)
        except SeoTemplate.DoesNotExist:
            template_str = ""
        else:
            template_str = getattr(template_obj, self.kind) # get necessary seo field specified in kind argument

        template_ = template.Template(template_str)
        data = template_.render(template_context).replace("\n", "").replace("\r", "").strip()

        if self.with_html and data:
            if self.kind in ["description", "keywords"]:
                data = mark_safe(u"<meta name=\"%s\" content=\"%s\">" % (self.kind, data))
            elif self.kind == "title":
                data = mark_safe(u"<title>%s</title>" % data)
            else:
                data = mark_safe(data)

        if self.var_name is not None:
            context[self.var_name] = data
            return u""
        else:
            return data
        

def parse_arguments(token):
    """
    Parse argument for both tags
    """
    bits = token.split_contents()
    tag_name = bits[0]

    if len(bits)%2:
        raise template.TemplateSyntaxError("%r tag requires odd number of arguments" % tag_name)

    kind = bits[1]

    target = None
    var_name = None

    for i in xrange(2, len(bits), 2):
        name = bits[i]
        value = bits[i+1]

        if name == "for":
            target = value
        elif name == "as":
            var_name = value

    return kind, target, var_name

def do_seo_html(parser, token):
    """
    Seo tag used to generate seo html tags like 'title', 'keywords' and 'description'
    Example usage: 
    {% seo_html title/description/keywords for object/"<target_name>" %}
    {% seo_html title/description/keywords %}
    {% seo_html title/description/keywords for object/"<target_name>" as var %}
    """
    return SeoNode(*parse_arguments(token), with_html=True)

def do_seo(parse, token):
    """
    Seo tag used to generate seo text that can be used inside html tags
    Example usage:
    {% seo title/description/keywords as var %}
    <meta name="..." content="{{ var }}">
    """
    return SeoNode(*parse_arguments(token), with_html=False)


register.tag('seo_html', do_seo_html)
register.tag('seo', do_seo)
