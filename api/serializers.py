from rest_framework import serializers
from posts.models import Posts


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id', 'task', 'task_text', 'deadline', 'importance', 'urgency')
