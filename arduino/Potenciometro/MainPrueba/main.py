from mainFrame import MainFrame
from tkinter import Tk

def main():
	root = Tk()
	root.wm_title("Sensor y actuador - Arduino")
	app = MainFrame(root)
	app.mainloop()

if __name__ =="__main__":
	main()