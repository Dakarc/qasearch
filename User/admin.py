from django.contrib import admin
from .models import TddsQuestions,TddsAnswers

# Register your models here.
#自定义模型管理类
class TddsQuestionsAdmin(admin.ModelAdmin):
    list_display = ['id','question_desc','question_tags','question_next','created_time']

class TddsAnswersAdmin(admin.ModelAdmin):
    list_display = ['id','question_id','answer_desc','created_time','ques']


#注册模型类
admin.site.register(TddsQuestions,TddsQuestionsAdmin)
admin.site.register(TddsAnswers,TddsAnswersAdmin)