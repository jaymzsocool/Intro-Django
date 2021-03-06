from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')
    # def create(self, validated_data):
    #     import pdb; pdb.set_trace()  # Start the debugger here
    #     pass
    def create(self, validated_data):
        user = self.context['request'].user
        # import pdb; pdb.set_trace()  # Start the debugger here
        # pass
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note

    

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.none()

    def get_queryset(self):
        logged_in_user = self.request.user

        if logged_in_user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=logged_in_user)