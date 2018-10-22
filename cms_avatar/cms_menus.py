from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu

class AvatarMenu(CMSAttachMenu):

    name = _("Avatar Menu")

    def get_nodes(self, request):
        nodes = []
        n1 = NavigationNode(_('Add'), reverse('avatar:avatar_add'),1, attr={'visible_for_anonymous': False})
        n2 = NavigationNode(_('Change'), reverse('avatar:avatar_change'),2, attr={'visible_for_anonymous': False})
        n3 = NavigationNode(_('Delete'), reverse('avatar:avatar_delete'),3, attr={'visible_for_anonymous': False})
        nodes += [n1,n2,n3]
        return nodes

menu_pool.register_menu(AvatarMenu)
