from django.db import models
import datetime
import uuid


class Copy(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    qtd_books = models.PositiveIntegerField()
    book = models.ForeignKey("books.Book", on_delete=models.PROTECT)
    student_borrowed = models.ManyToManyField(
        "students.Student", through="copies.Borrow", related_name="copies_borrowed"
    )
    is_avaliable = models.BooleanField(default=True)


class Borrow(models.Model):
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE)
    copy = models.ForeignKey("copies.Copy", on_delete=models.CASCADE)
    borrowed_at = models.DateField(auto_now_add=True)
    return_date = models.DateField(auto_now_add=True)
    qtd_borrowed = models.PositiveIntegerField()
