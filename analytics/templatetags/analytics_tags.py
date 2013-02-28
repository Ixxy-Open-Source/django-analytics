from django import template
from django.conf import settings
register = template.Library()

@register.inclusion_tag('google_analytics.html')
def google_analytics():
    """
    google analytics javascript
    """
    analytics_id = settings.GOOGLE_ANALYTICS_ID
    analytics_use_enhanced = getattr(settings, 'GOOGLE_ANALYTICS_USE_ENHANCED', False)
    return {
        'analytics_id' : analytics_id, 
        'analytics_use_enhanced': analytics_use_enhanced,
        }
