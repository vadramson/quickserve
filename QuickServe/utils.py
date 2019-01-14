# import cStringIO as StringIO
import os
from io import BytesIO
from os.path import join

from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

from django.conf import settings
from django.conf.urls.static import static


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result,  link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def fetch_resources(uri, rel):
    path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))

    return path
