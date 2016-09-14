from ..component.button import Button
from .  	  	 	    import Window
import urwid

class LogWindow(Window):
	PALETTE = [
		("log_header", "white", "dark red")
	]

	def __init__(self, **kwargs):
		self.width        = kwargs.get("width", ("relative", 80))
		self.height       = kwargs.get("height", ("relative", 70))
		self.align        = kwargs.get("align", "center")
		self.valign       = kwargs.get("valign", "middle")
		self.btn_ok_click = kwargs.get("btn_ok_click", None)
		self.logs         = []
		self.walker       = urwid.SimpleListWalker(self.logs)

	def log_callback(self, message=None):
		self.add_log(message)

	def add_log(self, message=None):
		assert message is not None, "message is not defined."
		self.logs.append(urwid.Text(message))
		self.redraw()

	def redraw(self):
		self.walker.contents[:] = self.logs

	def render(self):
		txt_header 		 = urwid.Text("Log Viewer","center")
		header_container = urwid.AttrMap(txt_header, "log_header")
		log_container    = urwid.ListBox(self.walker)

		frame = urwid.Frame(
			    header = header_container,
			      body = log_container,
			    footer = Button("OK", on_click=self.btn_ok_click).container,
			focus_part = "footer"
		)

		return urwid.Overlay(
			   top_w = frame,
			bottom_w = urwid.SolidFill(" "),
			   width = self.width,
			  height = self.height,
			   align = self.align,
			  valign = self.valign
		)