# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Company, Comment, Recommendations
from .forms import CommentForm, RecommendForm, CompanyForm

def company_detail(request, slug):
    template_name = 'company_detail.html'
    company = get_object_or_404(Company, slug=slug)
    comments = company.comments.filter(active=True)
    new_comment = None 
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        # if comment_form.is_valid(): this can be used to add CSRF token validation
 
        # Create Comment object but don't save to database yet
        new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
        new_comment.company = company
            # Save the comment to the database
        new_comment.save()
    else:
        comment_form = CommentForm()  
 
    return render(request, template_name, {'company': company,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

class companyListView(ListView):
    model = Company
    template_name = 'company_list.html' 

class companyDetailView(DetailView):
    model = Company
    template_name = 'company_detail.html'

def recommend_detail(request):
    template_name = 'index.html'
    new_recommend = None
    if request.method == 'POST':
        recommendation_form = RecommendForm(data=request.POST)
        new_recommend = recommendation_form.save(commit=False)
        new_recommend.save()
    else:
        recommendation_form = RecommendForm()
    return render(request, template_name, {'new_recommendation': new_recommend,
                                           'recommendation_form': recommendation_form})

class ywca_admin(ListView):
    template_name = 'ywca_admin.html' 
    context_object_name = 'company_list' 
    queryset = Company.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ywca_admin, self).get_context_data(**kwargs)
        context['comments_list'] = Comment.objects.all()
        context['recommend_list'] = Recommendations.objects.all()
        return context

def company_update(request, slug):
    instance = get_object_or_404(Company, slug=slug)
    form = CompanyForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        "name": instance.name,
        "description": instance.description,
        "website": instance.website,
        "country": instance.country,
        "state": instance.state,
    }
    return render(request, "", context) 