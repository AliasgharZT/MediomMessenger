"""
Components/BoxLayout
====================

:class:`~kivy.uix.boxlayout.BoxLayout` class equivalent. Simplifies working
with some widget properties. For example:

BoxLayout
---------

.. code-block:: kv

    BoxLayout:
        size_hint_y: None
        height: self.minimum_height

        canvas:
            Color:
                rgba: app.theme_cls.primary_color
            Rectangle:
                pos: self.pos
                size: self.size

MDBoxLayout
-----------

.. code-block:: kv

    MDBoxLayout:
        adaptive_height: True
        md_bg_color: app.theme_cls.primary_color

Available options are:
----------------------

- adaptive_height_
- adaptive_width_
- adaptive_size_

.. adaptive_height:
adaptive_height
---------------

.. code-block:: kv

    adaptive_height: True

Equivalent

.. code-block:: kv

    size_hint_y: None
    height: self.minimum_height

.. adaptive_width:
adaptive_width
--------------

.. code-block:: kv

    adaptive_width: True

Equivalent

.. code-block:: kv

    size_hint_x: None
    height: self.minimum_width

.. adaptive_size:
adaptive_size
-------------

.. code-block:: kv

    adaptive_size: True

Equivalent

.. code-block:: kv

    size_hint: None, None
    size: self.minimum_size
"""

__all__ = ("AZMDBoxLayout",)

from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.behaviors import DeclarativeBehavior
from kivy.properties import ObjectProperty
import geonamescache
from kivymd.uix.dialog import MDDialog
from kivy.app import App
from kivymd.toast import toast

class AZMDBoxLayout(
    DeclarativeBehavior, ThemableBehavior, BoxLayout, MDAdaptiveWidget
):
    name=ObjectProperty()
    family=ObjectProperty()
    number=ObjectProperty()
    user_info={'name':None,'family':None,'number':None}

    namechat=ObjectProperty()
    name_chat={'name':None}

    def get_user_info(self):
        name=self.name.text
        family=self.family.text
        number=self.number.text

        t_app=App.get_running_app()
        nu=t_app.root.ids.name_user
        fu=t_app.root.ids.family_user
        nbu=t_app.root.ids.number_user
        tu=t_app.root.ids.user_photo

        if name=='' or family=='' or number=='':
                toast('<<Name or Family or Number is Empty>>')
        elif name=='' and family=='' and number=='':
                toast('<<  Name, Family, Number is Empty >>')
        elif len(number)!=11:
              toast('Number = 09** *** ****')
        elif name!='' and family!='' and number!='':   
            nu.text='Name : '+name
            fu.text='Family : '+family
            nbu.text='Number : '+number
            tu.title=name[0]+family[0]

            self.user_info['name']=name
            self.user_info['family']=family
            self.user_info['number']=int(number)

            self.name.text=''
            self.family.text=''
            self.number.text=''
        else:
              pass 

    def get_chat_info(self):
        self.name_chat['name']=self.namechat.text 
        self.namechat.text=''
        # print(self.name_chat)

    """
    Box layout class.

    For more information, see in the
    :class:`~kivy.uix.boxlayout.BoxLayout` class documentation.
    """
