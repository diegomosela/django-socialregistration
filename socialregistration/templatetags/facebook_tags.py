from django import template
from django.conf import settings

register = template.Library()

FACEBOOK_APP_ID = getattr(settings, 'FACEBOOK_APP_ID', None)
FACEBOOK_EXTENDED_PERMISSIONS = getattr(settings, 'FACEBOOK_EXTENDED_PERMISSIONS', [])

@register.inclusion_tag('socialregistration/facebook_js.html', takes_context=True)
def facebook_js(context):
    if not 'request' in context:
        raise AttributeError, 'Please add the ``django.core.context_processors.request`` context processors to your settings.TEMPLATE_CONTEXT_PROCESSORS set'
    return {'next': context['next'] if 'next' in context else None,
            'request': context['request'],
            'logged_in': context['request'].user.is_authenticated(),
            'facebook_app_id' : FACEBOOK_APP_ID,
            'facebook_extended_permissions': ','.join(FACEBOOK_EXTENDED_PERMISSIONS)}

@register.inclusion_tag('socialregistration/facebook_button.html', takes_context=True)
def facebook_button(context):
    if not 'request' in context:
        raise AttributeError, 'Please add the ``django.core.context_processors.request`` context processors to your settings.TEMPLATE_CONTEXT_PROCESSORS set'
    return {'request': context['request'],
            'facebook_extended_permissions': ','.join(FACEBOOK_EXTENDED_PERMISSIONS)}

