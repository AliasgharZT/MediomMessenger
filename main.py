'''
[[[START]]] ==>>>{"Bogs"}
1)not access name or text to onelinelistitem in on press in conversation
2)can not create more one line in onlinelistitem >>>OK<<<
[[[End]]]
'''
from kivymd.app import MDApp
from kivy .lang import Builder
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.dialog import MDDialog
from AZ_MDBoxLayout import AZMDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivy.properties import ObjectProperty
from AZ_FileManager import MDFileManager
from kivymd.uix.list import IconRightWidgetWithoutTouch,OneLineRightIconListItem
from kivymd.toast import toast
from kivymd.uix.textfield import MDTextField

Builder.load_file('style.kv')

class Style(MDAnchorLayout):

    user_info={'name':None,'family':None,'number':None}
    # user_info={'name':'Aliasghar','family':'Zahdyan','number':'09054392674'}
    # name_user=ObjectProperty()
    # family_user=ObjectProperty()
    # number_user=ObjectProperty()
    user_photo=ObjectProperty()
    ml=ObjectProperty()
    address_photo=None
    t=0
    name_chat=[]
    mn=ObjectProperty()
    # l_buttons=[]
    # tlb=0 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.f=MDFileManager(
            exit_manager=self.close_add_user_photo,
            icon_selection_button='content-save-check-outline',
            select_path=self.get_user_photo,
            size_hint=(0.6,0.7),
            preview=True,
        )

    get_user_info='''
AZMDBoxLayout:
    orientation:'vertical'
    spacing:7

    name:name
    family:family
    number:number

    MDTextField:
        id:name
        helper_text:'Enter Name'
    MDTextField:
        id:family
        helper_text:'Enter Family'
    MDTextField:
        id:number
        helper_text:'Enter Number'
        input_filter:'int'
    MDAnchorLayout:
        anchor_x:'center'
        anchor_y:'center'
        MDFillRoundFlatButton:
            text:'Rejister'
            on_press:
                root.get_user_info()
'''

    get_user_chat='''
AZMDBoxLayout:
    orientation:'vertical'
    spacing:7

    namechat:namechat

    MDTextField:
        id:namechat
        helper_text:'Enter Name'
    MDAnchorLayout:
        anchor_x:'center'
        anchor_y:'center'
        MDFillRoundFlatButton:
            text:'Rejister'
            on_press:
                root.get_chat_info()
'''

    def about(self): 
        self.about_d=MDDialog(title='About :\n',
                              text='This program was created by Ali Asghar Zahdyan\n'+
                              '                                            < < < A . Z > > >')
        self.about_d.open()

    def add_user(self):
        self.add_user_d=MDDialog(title='Information :\n\n\n\n\n\n\n\n\n\n\n\n',type='custom',
                                 content_cls=Builder.load_string(self.get_user_info),
                                 buttons=[MDFlatButton(text='Back',on_press=self.close_add_user)  ] )
        self.add_user_d.size_hint=0.4,0.63
        self.add_user_d.open()   
    def close_add_user(self,obj):
        self.add_user_d.dismiss()
        self.user_info=AZMDBoxLayout.user_info
        # print(self.user_info)
        # print(AZMDBoxLayout.user_info)

    def add_user_photo(self):
        self.f.selection_button.on_press=self.set_user_photo
        self.f.show_disks()
    def close_add_user_photo(self,*args):
        self.f.close() 

    def get_user_photo(self,path):
        self.address_photo=path
        # self.user_photo.source=path
    def set_user_photo(self,*args):
        if self.address_photo==None:
            pass
        else:
            self.user_photo.source=self.address_photo
            self.address_photo=None 
            self.close_add_user_photo()

    def new_chat(self):
        self.new_chat_d=MDDialog(title='InformationChat :\n\n\n\n\n\n\n\n\n\n\n\n',type='custom',
                                 content_cls=Builder.load_string(self.get_user_chat),
                                 buttons=[MDFlatButton(text='Back',on_press=self.close_new_chat_d)  ] )
        self.new_chat_d.size_hint=0.4,0.63
        self.new_chat_d.open() 
    def close_new_chat_d(self,obj):
        self.new_chat_d.dismiss()
        if self.user_info['name']==None:
            toast('<< Fill out UserInformation >>')
        else:
            name=AZMDBoxLayout.name_chat
            # print(name['name'])
            name=name['name']
            # print(name)
            if (name=='') or (name in self.name_chat):pass
            else:
                self.t+=1
                if self.t==1:
                    self.ml.clear_widgets()
                else:
                    pass 
                one=OneLineRightIconListItem(
                    IconRightWidgetWithoutTouch(icon='chat'),
                    text=name+' & '+self.user_info['name'][0]+self.user_info['family'][0],
                    on_press=self.press_new_chat,
                    )
                # one.on_press=self.press_new_chat
                self.ml.add_widget(one) 
                self.name_chat.append(name)
                # self.l_buttons.append(one)
            # print(self.name_chat)
            # print(self.name_chat[self.t-1]) 
    def press_new_chat(self,instance):
        self.mn.current='fake'
        # self.ids.lbl_chat.text=self.name_chat[self.t-1]+' & '+self.user_info['name']
        self.ids.lbl_chat.text=instance.text 
        # print(self.l_buttons)
        # print(self.l_buttons[0].text)
        # self.l_buttons[0].on_press=print('ok')

    def messages(self):
        if self.ids.txt.text=='':pass
        else:
            # self.ids.ml2.add_widget(OneLineRightIconListItem(text=self.ids.txt.text))
            self.ids.ml2.add_widget(MDTextField(text=self.ids.txt.text,multiline=True,readonly=True))
            self.ids.txt.text=''

class MainApp(MDApp):
    
    def build(self):
        self.title='AZenger'
        self.icon='icon-app.jpg'
        self.theme_cls.theme_style='Dark'
        self.theme_cls.primary_palette='BlueGray'
        self.theme_cls.primary_hue='900'
        return Style()


MainApp().run()

