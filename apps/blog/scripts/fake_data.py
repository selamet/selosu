import os
import random

import django
from django.contrib.auth.models import User

from faker import Faker

from apps.blog.models import Post, PostImage

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'selosu.settings')

django.setup()


def create_user():
    fake = Faker(['en_US'])

    f_name = fake.first_name()
    l_name = fake.last_name()
    u_name = f'{f_name.lower()}_{l_name.lower()}'
    email = f'{u_name}@{fake.domain_name()}'
    print(f_name, l_name, email)

    user_check = User.objects.filter(username=u_name)

    while user_check.exists():
        u_name = u_name + str(random.randrange(1, 99))
        user_check = User.objects.filter(username=u_name)

    user = User(
        username=u_name,
        first_name=f_name,
        last_name=l_name,
        email=email,
        is_staff=fake.boolean(chance_of_getting_true=50),
    )

    user.set_password('qwe123123')
    user.save()

    print('Kullanıcı kaydedildi', u_name)


def create_post(count):
    fake = Faker(['en_US'])
    post_list = list()
    for i in range(0, count):
        authors = User.objects.all()
        selected_author_id = random.randrange(0, authors.count())
        content = fake.paragraph()
        title = fake.text()
        author = authors[selected_author_id]
        status = 1 if fake.boolean(chance_of_getting_true=50) else 0
        slug = fake.bothify(text=f"{title}-")
        post = Post(
            content=content,
            title=title,
            author=author,
            status=status,
            slug=slug
        )
        print(title, author.first_name, author.last_name, status)
        post_list.append(post)

    Post.objects.bulk_create(post_list)


def create_image(count):
    posts = Post.objects.all()
    image = PostImage.objects.get(id=1)
    post_image_list = list()
    for i in range(0, count):
        selected_post_id = random.randrange(0, posts.count())
        post = posts[selected_post_id]
        post_image_list.append(
            PostImage(image=image.image.url, post=post)
        )
        print(f"Added image this post: {post.id}")
    PostImage.objects.bulk_create(post_image_list)
