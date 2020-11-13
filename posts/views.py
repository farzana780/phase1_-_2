from django.shortcuts import render
import requests

# POSTS VIEW ENDPOINT
def posts(request):
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    post =r.json
    return render(request, 'blog-listing.html', {'post':post})


# POST DETAILS VIEW ENDPOINT
def post_details(request,):
    r = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    details = r.json
    c = requests.get("https://jsonplaceholder.typicode.com/posts/1/comments")
    comment = c.json
    return render(request, 'blog-post.html', {'details':details, 'comment':comment})