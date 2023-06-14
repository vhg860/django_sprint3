import datetime

from django.shortcuts import get_object_or_404, render

from blog.models import Category, Post


def output_published(posts_object):
    return (
        posts_object.filter(
            is_published=True, category__is_published=True
        )
        .filter(pub_date__date__lte=datetime.datetime.today()))


def index(request):
    return render(request, 'blog/index.html', {
        'post_list': output_published(Post.objects.all(),)[:5], })


def post_detail(request, post_id):
    return render(request, 'blog/detail.html', {
        'post': get_object_or_404(
            output_published(Post.objects.all(),), pk=post_id,),
    })


def category_posts(request, category_slug):
    category = get_object_or_404(Category.objects.all(), slug=category_slug,
                                 is_published=True)
    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': output_published(category.posts,)},)
