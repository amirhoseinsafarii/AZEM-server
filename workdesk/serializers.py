from rest_framework import serializers

from .models import WorkDesk, WorkDeskMembership


class WorkDeskSerializer(serializers.ModelSerializer):

    members = serializers.SerializerMethodField()
    # creator = serializers.StringRelatedField(read_only=True)
    # creator = serializers.SlugRelatedField(read_only=True)

    class Meta:
        model = WorkDesk
        fields = ["name", "collaborators", "members"]

    def get_members(self, obj):
        result = obj.members.all()
        return WorkDeskMembershipSerializer(instance=result, many=True).data

    # def create(self, validated_data):
    #     workdesk = WorkDesk(**validated_data)
    #     workdesk.save()
    #     return workdesk


class WorkDeskMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkDeskMembership
        fields = ["workdeskName", "member", "role"]
