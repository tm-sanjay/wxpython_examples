import wx

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

#Frame for the UI
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame,self).__init__(parent, title=title, size=(500,300))
        
        self.panel = MyBoxSizer(self)

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