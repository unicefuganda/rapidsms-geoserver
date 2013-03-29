
from django.contrib import admin

from .models import PollData
from .models import PollCategoryData
from .models import PollResponseData

admin.site.register(PollData)
admin.site.register(PollCategoryData)
admin.site.register(PollResponseData)
