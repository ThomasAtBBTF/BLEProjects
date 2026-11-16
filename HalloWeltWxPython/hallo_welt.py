#!/usr/bin/env python3
"""Ein einfaches "Hallo Welt"-Programm mit wxPython."""

import wx


class HalloWeltFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Hallo Welt", size=(320, 180))

        panel = wx.Panel(self)
        text = wx.StaticText(panel, label="Hallo Welt!")
        font = text.GetFont()
        font.PointSize += 10
        font = font.Bold()
        text.SetFont(font)

        button = wx.Button(panel, label="Beenden")
        button.Bind(wx.EVT_BUTTON, lambda event: self.Close())

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.AddStretchSpacer()
        sizer.Add(text, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        sizer.Add(button, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        sizer.AddStretchSpacer()
        panel.SetSizer(sizer)

        self.Centre()


def main():
    app = wx.App()
    frame = HalloWeltFrame()
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
