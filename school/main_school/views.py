from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Teacher, Timetable, Call_schedule, News_main, Gallery, Pride_school


def main_menu(request):
    """
    show main menu
    :param request:
    :return html page:
    """
    all_news = News_main.objects.all()
    all_gallary = Gallery.objects.all()
    all_pride = Pride_school.objects.all()

    return render(request, 'main_school/main_menu.html',
                  context={'news': all_news, 'image': all_gallary, 'pride': all_pride})


class NewsDeteilView(DetailView):
    model = News_main

    template_name = 'main_school/details_view.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        global model

        context = super().get_context_data(**kwargs)

        news_id = self.kwargs['pk']
        context['article'] = News_main.objects.get(pk=news_id)
        context['gallery'] = Gallery.objects.filter(article_id=news_id)
        return context


class Teacher_list(ListView):
    model = Teacher
    template_name = 'main_school/teacher_list.html'
    context_object_name = 'data_teacher'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_selected'] = 0
        return context




class Show_Teacher(DetailView):

    model = Teacher
    template_name = 'main_school/show_teacher.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'data_teacher'

    # def get_context_data(self, **kwargs):
    #     global model
    #
    #     context = super().get_context_data(**kwargs)
    #
    #     teacher_id = self.kwargs['pk']
    #     context['data_teacher'] = Teacher.objects.get(pk=teacher_id)
    #     return context


# def teacher_list(request):
#     """
#     show teacher from database
#     :param request:
#     :return context(data about teacher):
#     """
#     all_teacher = Teacher.objects.all()
#
#     return render(request, 'main_school/teacher_list.html', context={'data_teacher': all_teacher})




def lesson_timetable(request):

    # all_timetable = Timetable.objects.all()

    context = {
        # 'timetable': Timetable.objects.order_by('-id')[:7]
        'timetable': Timetable.objects.order_by('-date_of_publication')[:7]
    }
    return render(request, 'main_school/lesson_timetable.html', context=context)


def call_schedule(request):
    all_call = Call_schedule.objects.all()
    return render(request, 'main_school/call_achedule.html', context={'call': all_call})
