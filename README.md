# KivyOnTop

Makes Kivy windows stay on top of others. Works by manipulating window tags via `win32gui` library. Install with `python -m pip install KivyOnTop`.

## Features
 - Set AOT flag for Kivy window
 - Unset AOT flag for Kivy window
 - Bind window drawing to setting AOT flag for case the window is moved or resized by the app
 - Unbind window drawing

## Usage
```
from kivy.App import App
from kivy.core.window import Window
from KivyOnTop import register_topmost, unregister_topmost

class KivyontopApp(App):
    def on_start(self, *args):
     TITLE = 'KivyOnTop'
     Window.set_title(TITLE)
     register_topmost(Window, TITLE)

     # Not necessary
     self.bind(on_stop=lambda *args, w=Window, t=TITLE: unregister_topmost(w, t))
 
if __name__ == '__main__':
    KivyontopApp().run()
```
