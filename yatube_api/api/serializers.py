from rest_framework import serializers

from posts.models import Comment, Group, Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        if request is None or not hasattr(request, 'user'):
            raise serializers.ValidationError(
                'Не удалось определить пользователя. '
                'Пожалуйста, убедитесь, что запрос отправлен корректно.'
            )
        return super().create({**validated_data, 'author': request.user})


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)
