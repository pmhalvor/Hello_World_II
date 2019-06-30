from tkinter import *

class Application(Frame):
    def say_hi(self):
        print("hi there, everyone!")

    def createWidgets(self): #My question here is what is QUIT?
        self.QUIT = Button(self)
        self.QUIT["text"] = "Click here if you want to quit"
        self.QUIT["fg"]   = "red"  #"blue" "black" "green" "yellow" "purple"
        self.QUIT["command"] =  self.quit #.quit is the actual call to end program

        self.QUIT.pack()#{"side": "right"}) #try to remove, see what happens

        self.hi_there = Button(self) #New button called hi_there created
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi #calls say_hi function

        self.hi_there.pack({"side": "right"}) #dont know yet

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets() #sets up widget

root = Tk() #creates stage
app = Application(master=root) #creates what will be preformed on the stage
app.mainloop() #sets peice in motion
root.destroy() #assuming to avoid memory leakage? or maybe ends program in terminal when stage is closed?



"""
All About a Buttons:
config(**options) [#]
Modifies one or more widget options. If no options are given, the method returns a dictionary containing all current option values.

**options
	Widget options.
		activebackground=
			What background color to use when the button is active. The default is system specific. (the option database name is activeBackground, the class is Foreground)
		activeforeground=
			What foreground color to use when the button is active. The default is system specific. (activeForeground/Background)
		anchor=
			Controls where in the button the text (or image) should be located. Use one of N, NE, E, SE, S, SW, W, NW, or CENTER. Default is CENTER. (anchor/Anchor)
		background=
			The background color. The default is system specific. (background/Background)
		bg=
			Same as background.
		bitmap=
			The bitmap to display in the widget. If the image option is given, this option is ignored. (bitmap/Bitmap)
		borderwidth=
			The width of the button border. The default is platform specific, but is usually 1 or 2 pixels. (borderWidth/BorderWidth)
		bd=
			Same as borderwidth.
		command=
			A function or method that is called when the button is pressed. The callback can be a function, bound method, or any other callable Python object. If this option is not used, nothing will happen when the user presses the button. (command/Command)
		compound=
			Controls how to combine text and image in the button. By default, if an image or bitmap is given, it is drawn instead of the text. If this option is set to CENTER, the text is drawn on top of the image. If this option is set to one of BOTTOM, LEFT, RIGHT, or TOP, the image is drawn besides the text (use BOTTOM to draw the image under the text, etc.). Default is NONE. (compound/Compound)
		cursor=
			The cursor to show when the mouse is moved over the button. (cursor/Cursor)
		default=
			If set, the button is a default button. Tkinter will indicate this by drawing a platform specific indicator (usually an extra border). The default is DISABLED (no default behavior). (default/Default)
		disabledforeground=
			The color to use when the button is disabled. The background is shown in the background color. The default is system specific. (disabledForeground/DisabledForeground)
		font=
			The font to use in the button. The button can only contain text in a single font. The default is system specific. (font/Font)
		foreground=
			The color to use for text and bitmap content. The default is system specific. (foreground/Foreground)
		fg=
			Same as foreground.
		height=
			The height of the button. If the button displays text, the size is given in text units. If the button displays an image, the size is given in pixels (or screen units). If the size is omitted, it is calculated based on the button contents. (height/Height)
		highlightbackground=
			The color to use for the highlight border when the button does not have focus. The default is system specific. (highlightBackground/HighlightBackground)
		highlightcolor=
			The color to use for the highlight border when the button has focus. The default is system speciific. (highlightColor/HighlightColor)
		highlightthickness=
			The width of the highlight border. The default is system specific (usually one or two pixels). (highlightThickness/HighlightThickness)
		image=
			The image to display in the widget. If specified, this takes precedence over the text and bitmap options. (image/Image)
		justify=
			Defines how to align multiple lines of text. Use LEFT, RIGHT, or CENTER. Default is CENTER. (justify/Justify)
		overrelief=
			Alternative relief to use when the mouse is moved over the widget. If empty, always use the relief value. (overRelief/OverRelief)
		padx=
			Extra horizontal padding between the text or image and the border. (padX/Pad)
		pady=
			Extra vertical padding between the text or image and the border. (padY/Pad)
		relief=
			Border decoration. Usually, the button is SUNKEN when pressed, and RAISED otherwise. Other possible values are GROOVE, RIDGE, and FLAT. Default is RAISED. (relief/Relief)
		repeatdelay=
			(repeatDelay/RepeatDelay)
		repeatinterval=
			(repeatInterval/RepeatInterval)
		state=
			The button state: NORMAL, ACTIVE or DISABLED. Default is NORMAL. (state/State)
		takefocus=
			Indicates that the user can use the Tab key to move to this button. Default is an empty string, which means that the button accepts focus only if it has any keyboard bindings (default is on, in other words). (takeFocus/TakeFocus)
		text=
			The text to display in the button. The text can contain newlines. If the bitmap or image options are used, this option is ignored (unless the compound option is used). (text/Text)
		textvariable=
			Associates a Tkinter variable (usually a StringVar) to the button. If the variable is changed, the button text is updated. (textVariable/Variable)
		underline=
			Which character to underline, in a text label. Default is -1, which means that no character is underlined. (underline/Underline)
		width=
			The width of the button. If the button displays text, the size is given in text units. If the button displays an image, the size is given in pixels (or screen units). If the size is omitted, or zero, it is calculated based on the button contents. (width/Width)
		wraplength=
			Determines when a button’s text should be wrapped into multiple lines. This is given in screen units. Default is 0 (no wrapping). (wrapLength/WrapLength)

flash() [#]
Flash the button. This method redraws the button several times, alternating between active and normal appearance.

invoke() [#]
Call the command associated with the button.
"""
