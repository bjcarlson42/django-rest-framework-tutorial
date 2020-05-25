from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)    
    title = serializers.CharField(required=True, allow_blank=False, max_length=100)
    content = serializers.CharField(style={'base_template': 'textarea.html'})
    author = serializers.CharField(required=True, allow_blank=False, max_length=100)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance