"""
Admin site bindings for coursegraph
"""
import logging

from django.contrib import admin
from django.utils.translation import gettext as _
from edx_django_utils.admin.mixins import ReadOnlyAdminMixin

from .models import CourseGraphCourseDump
from .tasks import ModuleStoreSerializer

log = logging.getLogger(__name__)


def dump_courses(modeladmin, request, queryset):
    """
    TODO
    """
    all_course_keys = queryset.values_list('id', flat=True)
    submitted, skipped = ModuleStoreSerializer(all_course_keys).dump_courses_to_neo4j()
    modeladmin.message_user(
        request,
        _(
            "Enqueued dumps for {} course(s). Skipped {} unchanged course(s)."
        ).format(len(submitted), len(skipped)),
    )
dump_courses.short_description = _("Dump courses to CourseGraph (respect cache)")


def dump_courses_overriding_cache(modeladmin, request, queryset):
    """
    TODO
    """
    all_course_keys = queryset.values_list('id', flat=True)
    submitted, _skipped = ModuleStoreSerializer(all_course_keys).dump_courses_to_neo4j(override_cache=True)
    modeladmin.message_user(
        request,
        _("Enqueued dumps for {} course(s).").format(len(submitted)),
    )
dump_courses_overriding_cache.short_description = _("Dump courses to CourseGraph (override cache)")


class CourseGraphCourseDumpAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    """
    TODO
    """
    list_display = ['id']
    ordering = ['id']
    search_fields = ['id']

    actions = [dump_courses, dump_courses_overriding_cache]


admin.site.register(CourseGraphCourseDump, CourseGraphCourseDumpAdmin)
