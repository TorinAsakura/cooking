# -*- encoding: utf-8 -*-
import os
import datetime

from django.http import HttpResponseBadRequest
from django.conf import settings

#from setman import settings as custom_settings
from sorl.thumbnail import get_thumbnail

import Image, ImageEnhance

def reduce_opacity(im, opacity):
    """Returns an image with reduced opacity."""
    assert opacity >= 0 and opacity <= 1
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    else:
        im = im.copy()
    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)
    return im

def watermark(im, mark, position, opacity=1):
    """Adds a watermark to an image."""
    if opacity < 1:
        mark = reduce_opacity(mark, opacity)
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    # create a transparent layer the size of the image and draw the
    # watermark in that layer.
    layer = Image.new('RGBA', im.size, (0,0,0,0))
    if position == 'tile':
        for y in range(0, im.size[1], mark.size[1]):
            for x in range(0, im.size[0], mark.size[0]):
                layer.paste(mark, (x, y))
    elif position == 'scale':
        # scale, but preserve the aspect ratio
        ratio = min(
            float(im.size[0]) / mark.size[0], float(im.size[1]) / mark.size[1])
        w = int(mark.size[0] * ratio)
        h = int(mark.size[1] * ratio)
        mark = mark.resize((w, h))
        layer.paste(mark, ((im.size[0] - w) / 2, (im.size[1] - h) / 2))
    else:
        layer.paste(mark, position)
    # composite the watermark with the layer
    return Image.composite(layer, im, layer)


def ajax_required(f):
    """
    AJAX request required decorator
    use it in your views:

    @ajax_required
    def my_view(request):
        ....

    """    
    def wrap(request, *args, **kwargs):
            if not request.is_ajax():
                return HttpResponseBadRequest()
            return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap


def crop_image(src_img, out_img, coords):
    img = Image.open(unicode(src_img))
    cropped = img.crop(coords)
    cropped.save(out_img)
    os.chmod(out_img, 33261)
    return cropped


def get_avatar(request, size):
    """
    Size is list/tuple of two element.
    First element used if user has profile and avatar.
    Second one for setting default avatar size.
    """
    if request.user.is_authenticated() and request.user.profile.avatar:
        avatar = get_thumbnail(request.user.profile.avatar, size)
    else:
        avatar = get_thumbnail('http://collegeinn.com/images/recipes/recipe-default.jpg', size)
    return avatar


def add_watermark(image):
    srcimage_path = image.path
    srcimage_dir = '/'.join(str(image).split('/')[:-1])
    filename = srcimage_path.split('/')[-1]
    extension = '.' + filename.split('.')[-1]
    filename_root = '.'.join(filename.split('.')[:-1]) # if filename contains dots
    marked_filename = filename_root + '.' + 'marked' + extension
    marked_img = os.path.join(srcimage_dir, marked_filename)
    marked_img_fullpath = os.path.join(settings.MEDIA_ROOT, marked_img)
    if not os.path.exists(marked_img_fullpath) and 'marked' not in filename:
        im = Image.open(srcimage_path)
        mark = Image.open(settings.MARK_FILE_PATH)
        mark_posx, mark_posy = im.size
        result_img = watermark(im, mark, (mark_posx-280, mark_posy-260), 0.3)
        result_img.save(marked_img_fullpath)
        return marked_img
    return False


def timestampbased_filename(filename):
    name, extension = os.path.splitext(filename)
    format = "%Y-%m-%d_%H-%M-%S_%f"
    new_name = datetime.datetime.now().strftime(format)
    filename = new_name + extension
    return filename
