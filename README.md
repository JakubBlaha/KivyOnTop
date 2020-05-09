# KivyOnTop

Makes Kivy windows stay on top of others. Works by manipulating window tags via `win32gui` library. Install with `python -m pip install KivyOnTop`.

**Note: This wrapper only supports the Windows platform at the moment.**

## Features
 - set and reset the always on top flag for a Kivy window

## Usage example
```python
from kivy.App import App
from kivy.core.window import Window
from KivyOnTop import register_topmost, unregister_topmost


TITLE = 'KivyOnTop'


class KivyontopApp(App):
    def on_start(self, *args):
        Window.set_title(TITLE)

        # Register top-most
        register_topmost(Window, TITLE)

        # Unregister top-most (not necessary, only an example)
        self.bind(on_stop=lambda *args, w=Window, t=TITLE: unregister_topmost(w, t))
 

if __name__ == '__main__':
    app = KivyontopApp()
    app.run()
```
