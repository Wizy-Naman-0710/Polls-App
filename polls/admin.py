from django.contrib import admin
# Register your models here.

from .models import Question, Choice



# all these names, model, extra are names used by django during execution 
class ChoiceInline(admin.TabularInline): 
    model = Choice 
    extra = 3 

class QuestionAdmin(admin.ModelAdmin): 


    '''
    You can click on the column headers to sort by those values – except in the case of the was_published_recently header, 
    because sorting by the output of an arbitrary method is not supported. 
    Also note that the column header for was_published_recently is, by default, the name of the method (with underscores replaced with spaces),
    and that each line contains the string representation of the output.
    '''
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]})
    ]

    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
