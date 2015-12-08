# -*- coding:utf-8 -*-

from openerp.tests import common


class TestDocumentPageCreateMenu(common.TransactionCase):
    """document_page_create_menu test class."""

    def test_page_menu_creation(self):
        """Test page menu creation."""

        menu_parent = self.env.ref('base.menu_base_partner')

        menu_created = self.env['document.page.create.menu'].create({
             'menu_name': 'Wiki Test menu',
             'menu_parent_id': menu_parent.id
        })

        menu = self.env['document.page.create.menu'].search([('id', '=', menu_created.id)])
        menu.with_context(active_id=[self.ref('document_page.demo_page1')]).document_page_menu_create()
