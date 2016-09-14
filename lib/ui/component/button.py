import urwid

class Button:
	PALETTE = [("reversed", "standout", "")]

	def __init__(self, text="", on_click=None, args=()):
		self.btn       = urwid.Button(text)
		self.container = urwid.AttrMap(self.btn, None, focus_map="reversed")

		if on_click is not None:
			urwid.connect_signal(self.btn, "click", on_click, args)