from django.contrib import admin

# Register your models here.
from .models import organisation , country , user , contest , user_contest_rank , organisation_contest_participation, country_contest_participation


admin.site.register(organisation)
admin.site.register(country)
admin.site.register(user)
admin.site.register(contest)
admin.site.register(user_contest_rank)
admin.site.register(organisation_contest_participation)
admin.site.register(country_contest_participation)

