# importing all necessary modules
# like MDApp, MDLabel Screen, MDTextField
# and MDRectangleFlatButton
import os, sys
import ssl
import smtplib
import certifi
from email.message import EmailMessage

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.floatlayout import FloatLayout
from kivy.resources import resource_add_path
 
# creating Demo Class(base class)
class MainLayout(FloatLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
    
    def load_cards(self):
        print("customize here")
    
    # # defining label with all the parameters
    # l = MDLabel(text="HI PEOPLE!", halign='center',
    #             theme_text_color="Custom",
    #             text_color=(0.5, 0, 0.5, 1),
    #             font_style='Caption')
        
    # # defining Text field with all the parameters
    # name = MDTextField(text="Enter name", pos_hint={
    #                     'center_x': 0.8, 'center_y': 0.8},
    #                     size_hint_x=None, width=100)
        
    # # defining Button with all the parameters
    # btn = MDRectangleFlatButton(text="Submit", pos_hint={
    #                             'center_x': 0.5, 'center_y': 0.3},
    #                             on_release=self.btnfunc)
    # # adding widgets to screen
    # screen.add_widget(name)
    # screen.add_widget(btn)
    # screen.add_widget(l)
    # # returning the screen
    # #return screen
 
    # defining a btnfun() for the button to
    # call when clicked on it
    def btnfunc(self, obj):
        print("button is pressed!!")
    
    def sendEmail(self):
        email_sender = 'markus.corvinus0827@gmail.com'
        email_password = 'yzjbepduvwhfyhal'
        email_receiver = 'mbabiano@sdca.edu.ph'
        
        subject = 'Test Email'
        body    = """
        This is a test email
        """
        
        em = EmailMessage()
        em['From'] = email_sender
        em['To']   = email_receiver
        em['Subject'] = subject
        em.set_content(body)
        
        context = ssl.create_default_context(cafile=certifi.where())
        
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(email_sender,email_password)
            smtp.sendmail(email_sender,email_receiver,em.as_string())
            smtp.quit()
class DemoApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"    
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette= "Blue"
        self.theme_cls.accent_palette= "Teal"
        return MainLayout()
        
 
 
if __name__ == "__main__":
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    DemoApp().run()