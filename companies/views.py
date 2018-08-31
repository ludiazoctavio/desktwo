from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Department, Company
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# CRUD Department
class DepartmentListView(ListView):
    model = Department

    def get_queryset(self):
        queryset = super(DepartmentListView, self).get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(DepartmentListView, self).get_context_data(**kwargs)
        return context


class DepartmentCreateView(CreateView):
    model = Department
    fields = ('name',)
    success_url = reverse_lazy('department:list')

    def get_context_data(self, **kwargs):
        context = super(DepartmentCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.user_create = self.request.user
        form.save()
        return super(DepartmentCreateView, self).form_valid(form)


class DepartmentUpdateView(UpdateView):
    model = Department
    fields = ('name')
    success_url = reverse_lazy('department:list')

    def get_context_data(self, **kwargs):
        context = super(DepartmentUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.save()
        return super(DepartmentUpdateView, self).form_valid(form)


class DepartmentDeleteView(DeleteView):
    model = Department
    success_url = reverse_lazy('department:list')

    def get_context_data(self, **kwargs):
        context = super(DepartmentDeleteView, self).get_context_data(**kwargs)
        data = {
            'name': self.object,
        }
        context.update(data)
        return context

    def delete(self, request, *args, **kwargs):
        return super(DepartmentDeleteView, self).delete(request, *args, **kwargs)


# CRUD Company
class CompanyListView(ListView):
    model = Company

    def get_queryset(self):
        queryset = super(CompanyListView, self).get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)
        return context


class CompanyCreateView(CreateView):
    model = Company
    fields = ('name', 'latitude', 'longitude')
    success_url = reverse_lazy('company:list')

    def get_context_data(self, **kwargs):
        context = super(CompanyCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.user_create = self.request.user
        form.save()
        return super(CompanyCreateView, self).form_valid(form)


class CompanyUpdateView(UpdateView):
    model = Company
    fields = ('name', 'latitude', 'longitude')
    success_url = reverse_lazy('company:list')

    def get_context_data(self, **kwargs):
        context = super(CompanyUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.save()
        return super(CompanyUpdateView, self).form_valid(form)


class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('company:list')

    def get_context_data(self, **kwargs):
        context = super(CompanyDeleteView, self).get_context_data(**kwargs)
        data = {
            'name': self.object,
        }
        context.update(data)
        return context

    def delete(self, request, *args, **kwargs):
        return super(CompanyDeleteView, self).delete(request, *args, **kwargs)