from django.contrib import admin
from .models import Livro
admin.site.register(Livro)
from .models import Emprestimo
admin.site.register(Emprestimo)

# Register your models here.
