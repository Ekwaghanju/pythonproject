from kivy.app import App
from kivy.clock import Clock
from datetime import datetime
# gettinfg font
from kivy.core.text import LabelBase
#window size
from kivy.config import Config
# changing background color
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.properties import ObjectProperty

#Config.set('graphics','width','960')
#Config.set('graphics','height','540')  #16:9

#class ClockLayout(BoxLayout):
 #   time_prop = ObjectProperty(None)

class HelloApp(App):
    sw_started=False
    sw_seconds=0

    
    def update_time(self,nap):
        if self.sw_started:
            self.sw_seconds +=nap
            minutes,seconds =divmod(self.sw_seconds,60)
            self.root.ids.stopwatch.text =('%02d:%02d.[size=30]%2d[/size]'%(int(minutes),int(seconds),int(seconds*100%100)))
            
        now =datetime.now()
        self.root.ids.time.text = now.strftime('%B %d, %Y\n          [b]%H[/b]:%M:%S')
        

    def on_start(self):
        Clock.schedule_interval(self.update_time,0)

    def start_stop(self):
        self.root.ids.start_stop.text =('Start' 
                                        if self.sw_started else'Stop')
        self.sw_started=not self.sw_started


    def reset(self):
        if self.sw_started:
            self.root.ids.start_stop.text ='Start'
            self.sw_started=False
        self.sw_seconds=0
        self.root.ids.stopwatch.text ='00:00.[size=30]00[/size]'


if __name__=='__main__':
    Window.clearcolor = get_color_from_hex('#Ab0082')
    LabelBase.register(name='roboto',fn_regular='C:/Fonts/roboto/RobotoCondensed-Regular.ttf')
    LabelBase.register(name='Aller',fn_regular='C:/Fonts/Aller/Aller_Bd.ttf')
    HelloApp().run()