from rest_framework import serializers
from .models import Song




class SongSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id','title','date_released','likes','artiste_id')
        model  = Song
