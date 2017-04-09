#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.7.1 on Mon Apr  3 23:43:11 2017
#

import wx
import os
import FuncionesReportes as FR
# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class Principal(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Principal.__init__
        wx.Frame.__init__(self, *args, **kwds)
        self.bitmap_button_1 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("/home/victorjcb28/Psp-master/iconos/Administrativo1.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_3 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("/home/victorjcb28/Psp-master/iconos/chofer1.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_4 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("/home/victorjcb28/Psp-master/iconos/GerenteVentas1.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_5 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("/home/victorjcb28/Psp-master/iconos/chofer1.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_6 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("/home/victorjcb28/Psp-master/iconos/chofer1.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_2 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("/home/victorjcb28/Psp-master/iconos/Vigilante1.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_7 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("/home/victorjcb28/Psp-master/iconos/Vendedor1.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_8 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("/home/victorjcb28/Psp-master/iconos/Asistente1.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_3_copy_3 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("/home/victorjcb28/Psp-master/iconos/chofer1.png", wx.BITMAP_TYPE_ANY))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.OnAdministrativo, self.bitmap_button_1)
        self.Bind(wx.EVT_BUTTON, self.OnChofer, self.bitmap_button_3)
        self.Bind(wx.EVT_BUTTON, self.OnAVentas, self.bitmap_button_4)
        self.Bind(wx.EVT_BUTTON, self.OnVigilante, self.bitmap_button_2)
        self.Bind(wx.EVT_BUTTON, self.OnGVentas, self.bitmap_button_7)
        self.Bind(wx.EVT_BUTTON, self.OnAsistenteA, self.bitmap_button_8)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Principal.__set_properties
        self.SetTitle(_("Seleccion de Postulantes"))
        self.bitmap_button_1.SetToolTip(wx.ToolTip(_("Administrativo")))
        self.bitmap_button_1.SetSize(self.bitmap_button_1.GetBestSize())
        self.bitmap_button_3.SetToolTip(wx.ToolTip(_("Chofer")))
        self.bitmap_button_3.SetSize(self.bitmap_button_3.GetBestSize())
        self.bitmap_button_4.SetToolTip(wx.ToolTip(_("Asistente de Ventas")))
        self.bitmap_button_4.SetSize(self.bitmap_button_4.GetBestSize())
        self.bitmap_button_5.SetSize(self.bitmap_button_5.GetBestSize())
        self.bitmap_button_6.SetSize(self.bitmap_button_6.GetBestSize())
        self.bitmap_button_2.SetToolTip(wx.ToolTip(_("Vigilante")))
        self.bitmap_button_2.SetSize(self.bitmap_button_2.GetBestSize())
        self.bitmap_button_7.SetToolTip(wx.ToolTip(_("Gerente de Ventas")))
        self.bitmap_button_7.SetSize(self.bitmap_button_7.GetBestSize())
        self.bitmap_button_8.SetToolTip(wx.ToolTip(_("Asistente Administrativo")))
        self.bitmap_button_8.SetSize(self.bitmap_button_8.GetBestSize())
        self.bitmap_button_3_copy_3.SetSize(self.bitmap_button_3_copy_3.GetBestSize())
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Principal.__do_layout
        grid_sizer_1 = wx.FlexGridSizer(3, 9, 0, 0)
        grid_sizer_1.Add(self.bitmap_button_1, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_button_3, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_button_4, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_button_5, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_button_6, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_button_2, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_button_7, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_button_8, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_button_3_copy_3, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        self.SetSizer(grid_sizer_1)
        grid_sizer_1.Fit(self)
        self.Layout()
        self.Centre()
        # end wxGlade

    def OnAdministrativo(self, event):  # wxGlade: Principal.<event_handler>
        FR.PostulantesAdministratativo(self)
        os.system('xdg-open "ReportePostulantesAdministrativo.pdf"') #works for urls too

    def OnChofer(self, event):  # wxGlade: Principal.<event_handler>
        print "Event handler 'OnChofer' not implemented!"
        event.Skip()
    def OnVigilante(self, event):  # wxGlade: Principal.<event_handler>
        print "Event handler 'OnVigilante' not implemented!"
        event.Skip()
    def OnGVentas(self, event):  # wxGlade: Principal.<event_handler>
        print "Event handler 'OnGVentas' not implemented!"
        event.Skip()
    def OnAVentas(self, event):  # wxGlade: Principal.<event_handler>
        print "Event handler 'OnAVentas' not implemented!"
        event.Skip()
    def OnAsistenteA(self, event):  # wxGlade: Principal.<event_handler>
        print "Event handler 'OnAsistenteA' not implemented!"
        event.Skip()
# end of class Principal
