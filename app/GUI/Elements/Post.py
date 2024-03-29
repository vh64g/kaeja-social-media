from kivy.uix.image import Image as KvImage
from kivy.graphics.texture import Texture
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.core.window import Window

import classes.converters.images as imageConverter
from GUI.Design.py.Label import colored_label
from GUI.Elements.Popup import PopupWindow
import data.basicData as bD

import cv2
import sparse

Builder.load_string(colored_label)


class ColoredLabel(Label):
    pass


class Image(KvImage):
    def __init__(self, normal_texture, **kwargs):
        super(Image, self).__init__(**kwargs)
        self.normal_texture = normal_texture

    def maximize(self):
        PopupWindow("Image", self.normal_texture, Window.size, image=True)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.maximize()


class Post:
    """Add widgets to Grid Layout"""
    def __init__(self, widget, post):
        """Create a post with the given data"""

        '''header'''
        header = ColoredLabel(text=str(post.header), size_hint=(0.5, None), background_color=(0.1, 0.1, 0.1, 0.7))
        header.bind(texture_size=header.setter('size'))

        '''image'''
        try:
            if bD.POST_TYPE_IMAGE in post.post_type:
                post.image = cv2.flip(cv2.cvtColor(post.image, cv2.COLOR_BGR2RGB), 0)
                self.image_array_preview = post.image.copy()

                self.image = imageConverter.array2image(post.image)

                if bD.POST_TYPE_SPOILER_NSFW in post.post_type:
                    self.blur_amount = (int(self.image.width * bD.BLUR_AMOUNT), int(self.image.height * bD.BLUR_AMOUNT))
                    if self.blur_amount[0] > 0:
                        self.image_array_preview = cv2.blur(self.image_array_preview, self.blur_amount)
                    else:
                        pass
                else: self.image_array_preview = post.image

                self.image_preview = imageConverter.array2image(self.image_array_preview)

                self.texture = Texture.create(size=(self.image.width, self.image.height))
                self.texture_preview = Texture.create(size=(self.image_preview.width, self.image_preview.height))

                self.texture.blit_buffer(self.image.tobytes(), colorfmt='rgb', bufferfmt='ubyte')
                self.texture_preview.blit_buffer(self.image_preview.tobytes(), colorfmt='rgb', bufferfmt='ubyte')
        except:
            return

        '''text'''
        text = ""
        if bD.POST_TYPE_TEXT in post.post_type:
            text = ColoredLabel(text=str(post.content), size_hint=(0.5, None),  background_color=bD.post_background_color)
            text.bind(texture_size=text.setter('size'))

        # '''sizer'''
        # sizer = ColoredLabel(text=" ", size_hint=(1, None), size=(0, 1), background_color=bD.sizer_color)
        # widget.add_widget(sizer)

        '''render objects on screen'''
        widget.add_widget(header)
        if bD.POST_TYPE_IMAGE in post.post_type: widget.add_widget(Image(texture=self.texture_preview, size_hint=(1, None), size=(0, 300), normal_texture=self.texture))
        if bD.POST_TYPE_TEXT in post.post_type: widget.add_widget(text)
