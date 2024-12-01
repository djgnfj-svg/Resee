from custom_user.models import CustomUser
from book.models import BookCategory, Book
# 사용자 생성
user1 = CustomUser.objects.create_user(username="user1", email="user1@example.com", password="password123")
user2 = CustomUser.objects.create_user(username="user2", email="user2@example.com", password="password123")
user3 = CustomUser.objects.create_user(username="user3", email="user3@example.com", password="password123")

# 책 카테고리 생성
category1 = BookCategory.objects.create(name="Fiction")
category2 = BookCategory.objects.create(name="Non-Fiction")

# 책 생성
Book.objects.create(user=user1, category=category1, title="Book1-1", simple_explanation="Explanation1-1")
Book.objects.create(user=user1, category=category2, title="Book1-2", simple_explanation="Explanation1-2")
Book.objects.create(user=user1, category=category1, title="Book1-3", simple_explanation="Explanation1-3")

Book.objects.create(user=user2, category=category2, title="Book2-1", simple_explanation="Explanation2-1")
Book.objects.create(user=user2, category=category1, title="Book2-2", simple_explanation="Explanation2-2")
Book.objects.create(user=user2, category=category2, title="Book2-3", simple_explanation="Explanation2-3")

Book.objects.create(user=user3, category=category1, title="Book3-1", simple_explanation="Explanation3-1")
Book.objects.create(user=user3, category=category2, title="Book3-2", simple_explanation="Explanation3-2")
Book.objects.create(user=user3, category=category1, title="Book3-3", simple_explanation="Explanation3-3")

print("Users, categories, and books have been created successfully!")
