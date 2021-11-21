from django.contrib import admin
from .models import Board, Comment, Like, Note, Notification, Pin, Section, Tag, User

admin.site.register(User)
admin.site.register(Pin)
admin.site.register(Board)
admin.site.register(Tag)
admin.site.register(Section)
admin.site.register(Note)
admin.site.register(Notification)
admin.site.register(Comment)
admin.site.register(Like)

