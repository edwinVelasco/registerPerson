from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from app.models import Neighborhood, Person, Leader
from app.forms import PersonForm


class NeighborhoodAdmin(admin.ModelAdmin):
    pass


admin.site.register(Neighborhood, NeighborhoodAdmin)


class LeaderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Leader, LeaderAdmin)


class LeaderListFilter(admin.SimpleListFilter):
    title = 'Lideres'
    parameter_name = 'Lider'

    default_value = None

    def lookups(self, request, model_admin):
        list_of_leader = list()

        queryset = Leader.objects.all()
        for leader in queryset:
            list_of_leader.append(
                (str(leader.id), str(leader))
            )
        return sorted(list_of_leader, key=lambda tp: tp[1])

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(leader_id=self.value())
        return queryset

    def value(self):
        value = super(LeaderListFilter, self).value()
        if value is None:
            if self.default_value is None:
                first_leader = Leader.objects.order_by('name').first()
                value = None if first_leader is None else first_leader.id
                self.default_value = value
            else:
                value = self.default_value
        return value


class PersonResource(resources.ModelResource):

    class Meta:
        model = Person
        fields = ('id', 'identification', 'celphone', 'phone', 'name',
                  'last_name', 'state', 'leader',)


# ImportExportModelAdmin
class PersonAdmin(ImportExportModelAdmin):
    form = PersonForm
    list_display = ('id', 'identification', 'name', 'last_name', 'celphone', 'phone',
                    'neighborhood', 'state', 'leader')
    # list_filter = (('state', admin.BooleanFieldListFilter),
    #                ('leader', admin.RelatedOnlyFieldListFilter), )
    list_select_related = ('leader', )
    search_fields = ('identification', )
    list_per_page = 10
    resource_class = PersonResource


admin.site.register(Person, PersonAdmin)
# admin.site.register(Person, PersonAdmin2)





