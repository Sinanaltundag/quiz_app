from django.contrib import admin
import nested_admin
from quiz.models import Answer, Category, Question, Quiz

# Register your models here.

class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    min_num = 2
    max_num = 5
    extra = 1

class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    extra = 1
    inlines = [AnswerInline]

class QuizAdmin(nested_admin.NestedModelAdmin):
    model = Quiz
    inlines = [QuestionInline]
    list_display = ('title', 'category', 'question_count')
    list_filter = ('category',)
    search_fields = ('title',)
    ordering = ('title',)


admin.site.register(Quiz, QuizAdmin)

# class AnswerInline(admin.TabularInline):
#     model = Answer
#     min_num= 2
#     max_num= 5
#     extra = 1
# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ('title', "difficulty", "quiz")
#     list_filter = ('quiz',)
#     list_editable = ('difficulty',)
#     inlines = (AnswerInline,)
    
# class QuestionInline(admin.TabularInline):
#     model = Question
#     extra = 1

#     inlines = (AnswerInline,)

# class QuizAdmin(admin.ModelAdmin):
#     list_display = ('title', "category")
#     list_filter = ('category',)
#     inlines = (QuestionInline, AnswerInline,)
#     fieldsets = (
#         (None, {
#             'fields': ('title', 'category')
#         }),
#     )

admin.site.register([ Category,])
# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Quiz, QuizAdmin)

    
    # list_display = ('title', 'difficulty', 'quiz')
    # list_filter = ('difficulty', 'quiz')
    # search_fields = ('title',)
    # ordering = ('quiz', 'difficulty')
    # list_per_page = 10
    # list_display_links = ('title',)
    # list_select_related = ('quiz',)
    # raw_id_fields = ('quiz',)
    # autocomplete_fields = ('quiz',)
    # fieldsets = (
    #     (None, {
    #         'fields': ('title', 'difficulty', 'quiz')
    #     }),
    # )


    # filter_horizontal = ('answers',)
    # def get_queryset(self, request):
    #     qs = super(QuestionAdmin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(quiz__category__in=request.user.categories.all())
    # def get_readonly_fields(self, request, obj=None):
    #     if request.user.is_superuser:
    #         return self.readonly_fields
    #     return self.readonly_fields + ('quiz',)
    # def get_fieldsets(self, request, obj=None):
    #     if request.user.is_superuser:
    #         return self.fieldsets
    #     return self.fieldsets + ((None, {'fields': ('quiz',)}),)
    # def get_form(self, request, obj=None, **kwargs):
    #     if request.user.is_superuser:
    #         return super(QuestionAdmin, self).get_form(request, obj, **kwargs)
    #     return super(QuestionAdmin, self).get_form(request, obj, **kwargs)
    # def get_formset(self, request, obj=None, **kwargs):
    #     if request.user.is_superuser:
    #         return super(QuestionAdmin, self).get_formset(request, obj, **kwargs)
    #     return super(QuestionAdmin, self).get_formset(request, obj, **kwargs)
