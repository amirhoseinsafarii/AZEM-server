from rest_framework import serializers

from .models import WorkDesk, WorkDeskMembership


class WorkDeskSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkDesk
        fields = ["name", "collaborators"]

    # def create(self, validated_data):
    #     workdesk = WorkDesk(**validated_data)
    #     workdesk.save()
    #     return workdesk


class WorkDeskMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkDeskMembership
        fields = ["workdeskName", "member", "role"]
