from django import template
from ideas.models import IdeasUsers

register = template.Library()

class UserIdeaNode(template.Node):
    def __init__(self, obj):
        self.obj = template.Variable(obj)
        self.user = template.Variable('request.user')

    def render(self, context):
        obj = self.obj.resolve(context)
        user = self.user.resolve(context)
        try:
            points = IdeasUsers.objects.get(idea=obj, user=user).points
        except IdeasUsers.DoesNotExist:
            points = 0
        return points

@register.tag
def user_voted_for(parser, token):
    """
    Returns an integer representing the number of points allocated to
    a particular object.

    Syntax:
    
        {% user_voted_for obj %}
    """
    try:
        tag_name, obj = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires a single argument" % token.contents.split()[0]
    return UserIdeaNode(obj)
