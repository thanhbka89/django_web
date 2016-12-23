from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3 #bao nhiêu form nhập vào được hiển thị khi hiển thị bảng cha

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text'] #Khai bao thuộc tính trong model mà chúng ta muốn hiện ra trong trang Admin

    #gom nhóm các thuộc tính lại với nhau. Mỗi nhóm đều có thể có tiêu đề hoặc không có.
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date') #khai báo danh sách các thuộc tính cần hiển thị ra
    list_filter = ['pub_date']
    search_fields = ['question_text'] #Them o tim kiem

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
