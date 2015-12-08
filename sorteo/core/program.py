#!/usr/bin/python
import wx
import wx.grid as gridlib
import draw

class DrawUI(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'DrawUI', size=(353,270))
        self.panel=wx.Panel(self)
        #self.panel.SetBackgroundColour('#4f5049')

        names_button = wx.Button(self.panel,label='Names file',pos=(10,10),size=(-1,40))
        dates_button = wx.Button(self.panel,label='Dates file',pos=(10,50),size=(-1,40))
        result_button = wx.Button(self.panel,label='Result file',pos=(10,90),size=(-1,40))
        begin_draw_button = wx.Button(self.panel,label='Begin!',pos=(10,300),size=(-1,40))



        self.Bind(wx.EVT_BUTTON, self.receive_names_file, names_button)
        self.Bind(wx.EVT_BUTTON, self.receive_dates_file, dates_button)
        self.Bind(wx.EVT_BUTTON, self.receive_result_file, result_button)
        
        self.place_of_answer = wx.StaticText(self.panel,-1,pos=(150,300),size=(260,-1),style=wx.ALIGN_CENTER)
        self.Bind(wx.EVT_BUTTON, self.begin_draw, begin_draw_button)
        
        self.Bind(wx.EVT_CLOSE,  self.closewindow)

    def receive_names_file(self,event):
        box = wx.TextEntryDialog(None,'Write down the path to the file of names:','Names file','...here')
        if box.ShowModal() == wx.ID_OK:
            self.names_file = box.GetValue()

    def receive_dates_file(self,event):
        box = wx.TextEntryDialog(None,'Write down the path to the file of dates:','Dates file','...here')
        if box.ShowModal() == wx.ID_OK:
            self.dates_file = box.GetValue()

    def receive_result_file(self,event):
        box = wx.TextEntryDialog(None,'Write down the path to the file where you want the output:','Result file','...here')
        if box.ShowModal() == wx.ID_OK:
            self.result_file = box.GetValue()

    def begin_draw(self,event):
        try:
            if self.result_file  and self.names_file and self.dates_file:
                draw.begin_draw(self.names_file, self.dates_file, self.result_file)
                self.place_of_answer.SetLabel("Done! Go to see: %s file" % self.result_file)
        except AttributeError,e :
            self.place_of_answer.SetLabel("Error, missing some file path: %s" % e)
        except Exception, e:
            self.place_of_answer.SetLabel("Internal error: %s" % e)
        return
            
    def closewindow(self,event):
      self.Destroy()



if __name__=='__main__':
    app = wx.PySimpleApp()
    frame = DrawUI(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
