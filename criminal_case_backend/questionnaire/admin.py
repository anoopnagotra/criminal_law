from django.contrib import admin
from .models import Questionnaire, Age, QuesAnswer, QuestionnaireType

# Customised Admin view for Block users List
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','ques_type','is_active')
    list_display_links = ('id','name')

class AgeAdmin(admin.ModelAdmin):
    list_display = ('id', 'age', 'is_active')
    list_display_links = ('id','age')

class QuestionnaireTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'q_type')
    list_display_links = ('id','q_type')

class QuesAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'ques', 'answer')
    list_display_links = ('id','ques')

# Registering the Admin View
admin.site.register(Questionnaire, QuestionnaireAdmin)
# admin.site.register(Age, AgeAdmin)
admin.site.register(QuesAnswer, QuesAnswerAdmin)
# admin.site.register(QuestionnaireType, QuestionnaireTypeAdmin)
