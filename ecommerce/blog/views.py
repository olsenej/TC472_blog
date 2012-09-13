# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Blog, Comment, CommentForm
from django.http import HttpResponseRedirect

def index(request):
	blogList = Blog.objects.all().order_by('id')
	return render_to_response('blog/index.html', {'blogList':blogList})

def detail(request, blog_id):
	blog = get_object_or_404(Blog, pk = blog_id)
	return render_to_response('blog/detail.html', {'blog':blog})

def comment(request, blog_id):
	if (request.method == 'POST'):
		form = CommentForm(request.POST)
		if form.is_valid():
			newComment = form.save()
			newComment.name = request.session.session_key[:20] 
			newComment.save()
			return HttpResponseRedirect('/blog/' + str(newComment.blog.id))
	else:
		form = CommentForm( {'name':'old', 'tweet':'message', 'blog':blog_id} )
		
	return render_to_response('blog/comment.html', {'form': form, 'blog_id': blog_id})
	
def delComment(request, comment_id):
	# Get the comment to be deleted
	comment = get_object_or_404(Comment, pk = comment_id)
	# Get the comment's blog for redirection
	blog_id = comment.blog.id
	# Delete the comment
	comment.delete()
	# Go back to the blog entry
	return HttpResponseRedirect('/blog/' + str(blog_id))

def userComments(request):
	userBlogs = Comment.objects.filter(name = request.session.session_key[:20])
	return render_to_response('blog/userComments.html', {'userBlogs':userBlogs})

