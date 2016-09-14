from lib.builder                import Builder
from lib.ui.component.button    import Button
from lib.ui.window.log_window   import LogWindow
from lib.ui.window.build_window import BuildWindow
from lib.ui.palette             import Palette
import multiprocessing
import urwid

def exit_program(button, args):
	raise urwid.ExitMainLoop()

def section_click(button, args):
	def callback(message):
		log_window.add_log(message)
		screen.draw_screen()
	def exit_section(button, args):
		screen.widget = main
		screen.draw_screen()
	section,      = args
	log_window    = LogWindow(btn_ok_click=exit_section)
	screen.widget = log_window.render()
	screen.draw_screen()
	Builder.build(section, callback)

if __name__ == "__main__":
	palette = Palette()
	palette.append(Button.PALETTE)
	palette.append(LogWindow.PALETTE)
	palette.append(BuildWindow.PALETTE)

	build_window = BuildWindow(
		btn_exit_on_click = exit_program,
		         sections = Builder.get_sections(),
		 section_on_click = section_click
	)
	main = build_window.render()

	global screen
	screen = urwid.MainLoop(widget=main, palette=palette)
	screen.run()