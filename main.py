from kivy.app import App
from kivy.uix.button import Button
import os

class FlashVPN(App):
    def build(self):
        btn = Button(text='CONNECT FLASH VPN', font_size='20sp', background_color=(0, 0.7, 1, 1))
        btn.bind(on_press=self.start_vpn)
        return btn

    def start_vpn(self, instance):
        instance.text = "VPN STARTING..."
        os.system("./v2ray run --config config.json &")

if __name__ == '__main__':
    FlashVPN().run()

