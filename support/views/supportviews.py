from django.core.urlresolvers import reverse_lazy
from django.forms import formset_factory
from django.shortcuts import render 
from django.views.generic import DetailView, FormView, ListView, UpdateView

from support.forms import ActivityForm, CaseForm, CaseDetailForm, CasesList
from support.models import Cases, Activiteiten


#############################################################################
# Alle views die specifiek zijn voor de support app worden hieronder gebracht
#############################################################################


# Placeholder view voor het testen van de / of index route

class CasesListView(ListView):
    model = Cases
    template_name = 'support/index.html'
    context_object_name = 'cases'


# def index(request):
#     cases_list = Cases.objects.order_by('-datumMelding')
#     # print(cases_list)
#     context_dict = {'cases_list': cases_list}
#     CasesListFormSet = formset_factory(CasesList, extra=1)
#
#     return render(request, 'support/index.html', {'formset': CasesListFormSet(), 'cases_list': cases_list})


def activity_add(request):
    # context = RequestContext(request)
    if request.method == 'POST':
        form = ActivityForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return add_activity(request)
        else:
            print(form.errors)

    else:
        form = ActivityForm(initial={"uitvoerende": request.user})

    return render(request, 'support/activity_add.html', {'form': form})


def case_add(request):
    # context = RequestContext(request)
    if request.method == 'POST':
        form = CaseForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print(form.errors)

    else:
        form = CaseForm(initial={"uitvoerende": request.user})

    return render(request, 'support/case_add.html', {'form': form})

# def case_detail(request, case_id):
#     # context = RequestContext(request)
#     if request.method == 'POST':
#         form = CaseForm(request.POST)
#
#         if form.is_valid():
#             form .save(commit=True)
#
#             return index(request)
#         else:
#             print(form.errors)
#     else:
#         case_detail_data = get_object_or_404(Cases, id=case_id)
#         print(case_detail_data.omschrijving)
#         form = CaseDetailForm(instance=case_detail_data)
#
#     return render(request, 'support/case_detail.html', {'form': form, 'case_detail_data': case_detail_data})


# class case_detail(FormView, case_id):
#     template_name = 'support/case_detail.html'
#     form_class = CaseDetailForm
#     success_url = '/'
#
#     def form_valid(self, form):
#         return super(case_detail, self).form_valid(form)


class AddCaseView(FormView):
    template_name = 'support/case_add.html'
    form_class = CaseForm
    success_url = 'support/'


class UpdateCaseView(UpdateView):
    model = Cases
    template_name = 'support/case_update.html'
    # success_url = 'support/'
    # success_url = reverse_lazy('index')
    form_class = CaseForm
    # fields = '__all__'
