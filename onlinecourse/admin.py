from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission, Enrollment

# <HINT> Register QuestionInline and ChoiceInline classes here


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4

class QuestionInline(admin.ModelAdmin):
    list_display = ['question_text']
    inlines = [ChoiceInline]

# <HINT> Register Question and Choice models here

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'date_enrolled', 'mode', 'rating']



admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionInline)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
