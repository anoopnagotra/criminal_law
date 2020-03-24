from rest_framework import serializers
from . import models
from criminal_case_backend.users.models import User
from criminal_case_backend.questionnaire.models import Questionnaire, QuesAnswer

class QuestionnaireSerializer(serializers.ModelSerializer):
    option_list = serializers.SerializerMethodField()
    class Meta:
        model = Questionnaire
        fields = ('name', 'is_active', 'is_dropdown', 'option_list')

    def get_option_list(self, obj):
        options = QuesAnswer.objects.filter(ques_id=obj.id)
        options_list = {}
        if options:
            for option in options:
                # options_list = []
                print()
                print (option)
                data = {}
                if obj.is_dropdown:
                    print(option.answer)
                    data['options'] = list(list(option.answer.split(",")))
                else:
                    data['options'] = option.answer
                options_list.update(data)
        return options_list
