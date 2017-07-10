from django.forms import widgets
from rest_framework import serializers
from .models.post import Post


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'photo',
            'created_date',
            'modified_date',
            'author_id',
            'my_comment_id',
            'video_id',
        )
