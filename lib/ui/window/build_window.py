from ..component.button import Button
from . 				    import Window
import urwid

class BuildWindow(Window):
	PALETTE = [
		("build_header", "white", "dark red")
	]

	def __init__(self, **kwargs):
		Window.__init__(self)
		self.width    		   = kwargs.get("width",("relative",30))
		self.height   		   = kwargs.get("height",("relative", 30))
		self.valign   		   = kwargs.get("valign", "middle")
		self.align             = kwargs.get("align","center")
		self.sections          = kwargs.get("sections",[])
		self.section_on_click  = kwargs.get("section_on_click", None)
		self.btn_exit_on_click = kwargs.get("btn_exit_on_click", None)

	def render(self):
		txt_header       = urwid.Text("Select Section(s)","center")
		header_container = urwid.AttrMap(txt_header, "build_header")

		menu = []
		for section in self.sections:
			btn_section = Button(
				    text = section.name,
				on_click = self.section_on_click,
				    args = (section,)
			)
			menu.append(btn_section.container)
		btn_exit = Button(
			    text = "Exit",
			on_click = self.btn_exit_on_click
		)
		menu.append(btn_exit.container)

		section_list = urwid.ListBox(urwid.SimpleListWalker(menu))

		frame = urwid.Frame(
			header = header_container,
			  body = section_list
		)

		return urwid.Overlay(
			   top_w = frame,
			bottom_w = urwid.SolidFill(" "),
			   width = ("relative", 30),
			  height = ("relative", 30),
			  valign = "middle",
			   align = "center"
		)