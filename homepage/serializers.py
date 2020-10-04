from homepage.models import Post

from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
                'id',
                'roast_or_boast',
                'post_text',
                'up_votes',
                'down_votes',
                'submission_date',
                'score'
                ]
