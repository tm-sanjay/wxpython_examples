import wx
from wx.core import Panel

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


#Frame for the UI
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame,self).__init__(parent, title=title, size=(500,200))
        
        # add your panel here
        # self.panel = MyBoxSizer(self)
        # MyGridSizer(self)
        # MyButtonEvent(self)
        MyCheckBox(self)

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