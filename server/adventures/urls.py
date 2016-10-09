"""
Url definitions for the adventures app.
"""
from rest_framework.routers import DefaultRouter

from .views.adventure import AdventureViewSet
from .views.author import AuthorViewSet
from .views.character import CharacterViewSet
from .views.edition import EditionViewSet
from .views.environment import EnvironmentViewSet
from .views.item import ItemViewSet
from .views.item_modifier import ItemModifierViewSet
from .views.item_type import ItemTypeViewSet
from .views.monster import MonsterViewSet
from .views.publisher import PublisherViewSet
from .views.race import RaceViewSet
from .views.setting import SettingViewSet

router = DefaultRouter()
router.register('adventures', AdventureViewSet)
router.register('authors', AuthorViewSet)
router.register('characters', CharacterViewSet)
router.register('editions', EditionViewSet)
router.register('environments', EnvironmentViewSet)
router.register('items', ItemViewSet)
router.register('itemmodifiers', ItemModifierViewSet)
router.register('itemtypes', ItemTypeViewSet)
router.register('monsters', MonsterViewSet)
router.register('publishers', PublisherViewSet)
router.register('races', RaceViewSet)
router.register('settings', SettingViewSet)
