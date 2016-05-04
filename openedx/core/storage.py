"""
Django storage backends for Open edX.
"""
from django_pipeline_forgiving.storages import PipelineForgivingStorage
from django.contrib.staticfiles.storage import StaticFilesStorage, CachedFilesMixin
from pipeline.storage import PipelineMixin, NonPackagingMixin
from require.storage import OptimizedFilesMixin
from openedx.core.djangoapps.theming.storage import ComprehensiveThemingAwareMixin


class ProductionStorage(
        PipelineForgivingStorage,
        ComprehensiveThemingAwareMixin,
        OptimizedFilesMixin,
<<<<<<< HEAD
        ThemePipelineMixin,
        ThemeStorage,
=======
        PipelineMixin,
        CachedFilesMixin,
>>>>>>> 8127158e2af778065c3b1324aa0847bf2517fafe
        StaticFilesStorage
):
    """
    This class combines Django's StaticFilesStorage class with several mixins
    that provide additional functionality. We use this version on production.
    """
    pass


class DevelopmentStorage(
        ComprehensiveThemingAwareMixin,
        NonPackagingMixin,
        PipelineMixin,
        StaticFilesStorage
):
    """
    This class combines Django's StaticFilesStorage class with several mixins
    that provide additional functionality. We use this version for development,
    so that we can skip packaging and optimization.
    """
    pass
