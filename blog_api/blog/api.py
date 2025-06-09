from django.http import HttpRequest
from ninja import Router
from ninja.security import django_auth
from django.contrib.auth import authenticate
from .models import Post
from .schemas import PostSchema, PostCreateSchema
from typing import List
from django.shortcuts import get_object_or_404

router = Router(auth=django_auth)


@router.get("/posts", response=List[PostSchema])
def list_posts(request):
    return Post.objects.all()


@router.get("/posts/{post_id}", response=PostSchema)
def get_post(request, post_id: int):
    return get_object_or_404(Post, id=post_id)


@router.post("/posts", response=PostSchema)
def create_post(request, data: PostCreateSchema):
    post = Post.objects.create(**data.dict())
    return post


@router.put("/posts/{post_id}", response=PostSchema)
def update_post(request, post_id: int, data: PostCreateSchema):
    post = get_object_or_404(Post, id=post_id)
    for key, value in data.dict().items():
        setattr(post, key, value)
    post.save()
    return post


@router.delete("/posts/{post_id}")
def delete_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return {"success": True}
