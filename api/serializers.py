from rest_framework import serializers

from .models import Post, Comment


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "author_name",
            "content",
            "creation_date",
            "post",
        )


class PostSerializer(serializers.HyperlinkedModelSerializer):

    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "link",
            "creation_date",
            "amount_of_upvotes",
            "author_name",
            "comments",
        )
