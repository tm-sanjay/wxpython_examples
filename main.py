import wx
from wx.core import Choice, Panel

# Panel for sized box
class MyBoxSizer(wx.Panel):
    def __init__(self, parent):
        super(MyBoxSizer,self).__init__(parent)
        
        # wx.StaticText(self, label = "Box sizer")
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        label1 = wx.StaticText(self, label = "Label 1",style = wx.ALIGN_CENTER)
        vbox.Add(label1, 0, wx.EXPAND)
        
        label2 = wx.StaticText(self, label = "Label 2",style = wx.ALIGN_CENTER)
        vbox.Add(label2, 0, wx.EXPAND)
        
        label3 = wx.StaticText(self, label = "Label 3",style = wx.ALIGN_CENTER)
        hbox.Add(label3, 0, wx.EXPAND)  
        
        label4 = wx.StaticText(self, label = "Label 4",style = wx.ALIGN_CENTER)
        hbox.Add(label4, 0, wx.EXPAND)
        
        vbox.Add(hbox)
        #must add in the end when sizer is created
        self.SetSizer(vbox)

# Panel for Grid Sizer
class MyGridSizer(wx.Panel):
    def __init__(self,parent):
        super(MyGridSizer,self).__init__(parent)
        
        wx.StaticText (self, label='Grid Sizer')
        
        # grid(x,y,spaceX,spaceY)                     
        gridSizer = wx.GridSizer(4,5,3,6)
        """
        # adds labels as grid elements
        for i in range(1,21):
            ele = 'element-'+ str(i)
            gridSizer.Add(wx.StaticText(self, label = ele), 0, wx.EXPAND)
            self.SetSizer(gridSizer)
        """
        # adds buttons as grid elements
        for i in range(1,21):
            btn = 'button-'+ str(i)
            gridSizer.Add(wx.Button(self, label = btn), 0, wx.EXPAND)
            self.SetSizer(gridSizer)

# Panel for Button actions(events)
class MyButtonEvent(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.title = wx.StaticText(self, label='Button Event')
        
        self.label1 = wx.StaticText(self, label='Not Clicked')
        self.label2 = wx.StaticText(self, label='Toggle')
        
        self.btn = wx.Button(self, label = "Click")
        self.btn.Bind(wx.EVT_BUTTON,self.onClick)
        
        self.toggleBtn = wx.ToggleButton(self, label='Toggle')
        self.toggleBtn.Bind(wx.EVT_TOGGLEBUTTON, self.onToggle)
        
        image = wx.Image("images/play.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmapBtn = wx.BitmapButton(self, id = -1, bitmap = image,size = (image.GetWidth()+100 ,image.GetHeight()+100))
        self.bitmapBtn.SetLabel("Play")
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.title, 0, wx.ALIGN_CENTER)
        sizer.Add(self.label1)
        sizer.Add(self.btn)
        sizer.Add(self.label2)
        sizer.Add(self.toggleBtn)
        sizer.Add(self.bitmapBtn)
        
        #must add in the end when sizer is created
        self.SetSizer(sizer)
    
    def onClick(self, event):
        self.label1.SetLabelText("Button CLicked")
    
    def onToggle(self, event):
        state = event.GetEventObject().GetValue()
        
        if state == True:
            self.label2.SetLabel("OFF")
            event.GetEventObject().SetLabel("Click to OFF")
        else:
            self.label2.SetLabel("ON")
            event.GetEventObject().SetLabel("Click to ON")

# Panel for checkbox and its events
class MyCheckBox(wx.Panel):
    def __init__(self, parent):
        super(MyCheckBox, self).__init__(parent)
        
        checkBox1 = wx.CheckBox(self, label = "Car")
        checkBox2 = wx.CheckBox(self, label = 'Bus')
        
        self.label1 = wx.StaticText(self, label = '')
        self.label2 = wx.StaticText(self, label = '')
        self.label3 = wx.StaticText(self, label = '')

        #bind when any checkbox is clicked (use binding only one time)
        # self.Bind(wx.EVT_CHECKBOX, self.onChecked)
        checkBox1.Bind(wx.EVT_CHECKBOX, self.onChecked1)
        checkBox2.Bind(wx.EVT_CHECKBOX, self.onChecked2)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(checkBox1)
        vbox.Add(self.label1)
        vbox.Add(checkBox2)
        vbox.Add(self.label2)
        vbox.Add(self.label3)
        self.SetSizer(vbox)
    
    def onChecked(self, event):
        cb = event.GetEventObject()
        self.label3.SetLabelText(cb.GetLabel())
        print('Checked')
    
    def onChecked1(self, event):
        cb = event.GetEventObject()
        self.label1.SetLabelText(str(cb.GetValue()))
    
    def onChecked2(self, event):
        cb = event.GetEventObject()
        self.label2.SetLabelText(str(cb.GetValue()))

# Panel for Radio Button and its events
class MyRadioButton(wx.Panel):
    def __init__(self, parent):
        super(MyRadioButton, self).__init__(parent)
        
        rb1 = wx.RadioButton(self, label = "Car", style = wx.RB_GROUP)
        # try style = wx.RB_SINGLE
        rb2 = wx.RadioButton(self, label = "Bus")
        
        self.label = wx.StaticText(self, label = "")
        
        self.Bind(wx.EVT_RADIOBUTTON, self.onRadioButton)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(rb1)
        vbox.Add(rb2)
        vbox.Add(self.label)
        self.SetSizer(vbox)
    
    def onRadioButton(self, event):
        rb = event.GetEventObject()
        self.label.SetLabel('Selected ' + rb.GetLabel())

# Panel for RadioBox and event
class MyRadioBox(wx.Panel):
    def __init__(self, parent):
        super(MyRadioBox,self).__init__(parent)
        
        self.label = wx.StaticText(self, label = "", pos = (120,20))
        rbList = ['Cat','Dog','Bird']
        rbox = wx.RadioBox(self, label = 'RadioBox', pos = (20,20), choices = rbList,style = wx.RA_SPECIFY_ROWS)
        self.Bind(wx.EVT_RADIOBOX, self.onRadioBox)
    
    def onRadioBox(self, event):
        rb = event.GetEventObject()
        self.label.SetLabel('Pet selected ' + rb.GetStringSelection())

# Panel for MySlider 
class MySlider(wx.Panel):
    def __init__(self, parent):
        super(MySlider,self).__init__(parent)
        slider  = wx.Slider(self, value = 10, minValue = 1,  maxValue = 20, pos = (10,10),
                            style = wx.SL_HORIZONTAL|wx.SL_LABELS)
        
        self.label = wx.StaticText(self, label = 'wxPython', pos = (30, 50))
        slider.Bind(wx.EVT_SLIDER, self.onSlider)
    
    def onSlider(self, event):
        # Change the font size using slider
        obj = event.GetEventObject()
        val = obj.GetValue()
        font  = self.GetFont()
        font.SetPointSize(val)
        self.label.SetFont(font)

class MyComboBox(wx.Panel):
    def __init__(self, parent):
        super(MyComboBox,self).__init__(parent)
        
        label = wx.StaticText(self, label= 'Select any Language', pos = (10,10))
        self.label1  = wx.StaticText(self, label = '',  pos = (100, 30))
        self.label2  = wx.StaticText(self, label = '',  pos = (100, 70))
        
        # list that will be shown in Combobox(editable)
        languages = ['C', 'C++', 'Python', 'Dart', 'Golang', 'Rust', 'Java']
        combo = wx.ComboBox(self, choices = languages, pos = (10,30))
        combo.Bind(wx.EVT_TEXT, self.onCombo)
        # combo.Bind(wx.EVT_COMBOBOX, self.onCombo)
        
        # list that will be shown in Choice(read-only)
        choice = wx.Choice(self, choices = languages, pos = (10,70))
        choice.Bind(wx.EVT_CHOICE, self.onChoice)
    
    def onCombo(self, event):
        cb = event.GetEventObject()
        self.label1.SetLabel('Combo selection ' + cb.GetValue())
    
    def onChoice(self, event):
        cb = event.GetEventObject()
        self.label2.SetLabel('Choice selection ' + cb.GetString(cb.GetSelection()))

class MyTextCtrl(wx.Panel):
    def __init__(self, parent):
        super(MyTextCtrl, self).__init__(parent)
        
        label  = wx.StaticText(self, label = "Text Field", pos = (10,10))
        self.label1 = wx.StaticText(self, label = "Type and press Enter", pos = (150,35))
        # enter the text and press ender
        txt = wx.TextCtrl(self, pos = (10,30), style = wx.TE_PROCESS_ENTER)
        txt.Bind(wx.EVT_TEXT_ENTER, self.onTextCtrl)
        
        self.label2 = wx.StaticText(self, label = "Type something", pos = (150,65))
        txt1 = wx.TextCtrl(self, pos = (10,60))
        txt1.Bind(wx.EVT_TEXT, self.onTextCtrl1)
        
        # read-only style
        txt2 = wx.TextCtrl(self, value = "Read Only Text",
                            style = wx.TE_READONLY | wx.TE_CENTER, pos = (10,90))
        # Multiline form
        label3 = wx.StaticText(self, label ='Multi Line', pos = (230,125))
        txt3 = wx.TextCtrl(self, size = (200,100),style = wx.TE_MULTILINE, pos = (10,120))
    
    def onTextCtrl(self, event):
        self.label1.SetLabel('Entered text = '+ event.GetString())
    
    def onTextCtrl1(self, event):
        self.label2.SetLabel('Typed text = '+ event.GetString())

# Panel for MessageBox and different events
class MyMessageBox(wx.Panel):
    def __init__(self, parent):
        super(MyMessageBox, self).__init__(parent)
        
        btn1  = wx.Button(self, label = "Message 1", pos = (10,10))
        btn1.Bind(wx.EVT_BUTTON, self.onBtn1)
        
        btn2  = wx.Button(self, label = "Message 2", pos = (10,40))
        btn2.Bind(wx.EVT_BUTTON, self.onBtn2)
        
        btn3  = wx.Button(self, label = "Message 3", pos = (10,70))
        btn3.Bind(wx.EVT_BUTTON, self.onBtn3)
    
    def onBtn1(self, event):
        wx.MessageBox('OK Message', caption =  "Message 1", style = wx.OK | wx.ICON_INFORMATION)
    
    def onBtn2(self, event):
        wx.MessageBox('Warning Message', caption =  "Message 2", style = wx.OK | wx.ICON_WARNING)
    
    def onBtn3(self, event):
        wx.MessageBox('error Message', caption =  "Message 3", style = wx.OK | wx.ICON_ERROR)

#Frame for the UI
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame,self).__init__(parent, title=title, size=(500,200))
        
        # add your panel here
        # self.panel = MyBoxSizer(self)
        # MyGridSizer(self)
        # MyButtonEvent(self)
        # MyCheckBox(self)
        # MyRadioButton(self)
        # MyRadioBox(self)
        # MySlider(self)
        # MyComboBox(self)
        # MyTextCtrl(self)
        MyMessageBox(self)

class MyApp(wx.App):
    def OnInit(self):
        #add locale to avoid errors related to C++ locale
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        frame = MyFrame(parent=None, title='wxPython GUI')
        frame.Show()
        
        # must return 'True' in the end
        return True

def main():
    app = MyApp()
    app.MainLoop()

if __name__ == '__main__':
    __name__ = 'main'
    main()