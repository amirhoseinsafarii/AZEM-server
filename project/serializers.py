from rest_framework import serializers


from .models import Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ["projectTitle", "collaborators"]

    def update(self, instance, validated_data):
        print(validated_data, "validated_data")
        member = validated_data.get("collaborators")

        for i in member:
            print(i.id, "member in serializer >>>>>>>>>>>>")
            instance.collaborators.add(i)
        return instance
