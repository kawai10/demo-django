from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True, verbose_name="이메일")
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=15, verbose_name="이름")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일")

    class Meta:
        db_table = "users"
        ordering = ["-id"]
        verbose_name_plural = "계정"

    def __str__(self):
        return self.name
