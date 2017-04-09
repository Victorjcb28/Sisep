#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.7.1 on Sun Apr  9 13:03:10 2017
#

import wx
import funciones as f
import entrada as E

#Usuarios
import GuardarUsuario as GU
import BuscarUsuario as BU
import ModificarUsuario as MU

#Bloquear y Desbloquear
import BloquearUsuario as BQU
import DesbloquearUsuario as DU

#Postulante
import GuardarPostulante as GP
import BuscarPostulante as BP

#Reportes
import MedioUsuarios as MEU
# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class Principal(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Principal.__init__
        kwds["style"] = wx.MAXIMIZE
        wx.Frame.__init__(self, *args, **kwds)
        self.notebook_1 = wx.Notebook(self, wx.ID_ANY)
        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.bitmap_button_2 = wx.BitmapButton(self.notebook_1_pane_1, wx.ID_ANY, wx.Bitmap("/home/victorjcb28/Psp-master/iconos/RegistrarU1.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_3 = wx.BitmapButton(self.notebook_1_pane_1, wx.ID_ANY, wx.Bitmap("/home/victorjcb28/Psp-master/iconos/BuscarP1.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_4 = wx.BitmapButton(self.notebook_1_pane_1, wx.ID_ANY, wx.Bitmap("/home/victorjcb28/Psp-master/iconos/ModificarU1.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_5 = wx.BitmapButton(self.notebook_1_pane_1, wx.ID_ANY, wx.Bitmap("/home/victorjcb28/Psp-master/iconos/Userlock1.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_6 = wx.BitmapButton(self.notebook_1_pane_1, wx.ID_ANY, wx.Bitmap("/home/victorjcb28/Psp-master/iconos/Userunlock1.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_1 = wx.BitmapButton(self.notebook_1_pane_1, wx.ID_ANY, wx.Bitmap("/home/victorjcb28/Psp-master/iconos/exit1.png", wx.BITMAP_TYPE_ANY))
        self.notebook_2 = wx.Notebook(self, wx.ID_ANY)
        self.notebook_2_pane_1 = wx.Panel(self.notebook_2, wx.ID_ANY)
        self.bitmap_button_9 = wx.BitmapButton(self.notebook_2_pane_1, wx.ID_ANY, wx.Bitmap("/home/victorjcb28/Psp-master/iconos/RegistrarP1.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_8 = wx.BitmapButton(self.notebook_2_pane_1, wx.ID_ANY, wx.Bitmap("/home/victorjcb28/Psp-master/iconos/BuscarP1.png", wx.BITMAP_TYPE_ANY))
        self.notebook_3 = wx.Notebook(self, wx.ID_ANY)
        self.notebook_3_pane_1 = wx.Panel(self.notebook_3, wx.ID_ANY)
        self.bitmap_button_10 = wx.BitmapButton(self.notebook_3_pane_1, wx.ID_ANY, wx.Bitmap("/home/victorjcb28/Psp-master/iconos/ReporU1.png", wx.BITMAP_TYPE_ANY))
        self.notebook_4 = wx.Notebook(self, wx.ID_ANY)
        self.notebook_4_pane_1 = wx.Panel(self.notebook_4, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.OnRegistrarU, self.bitmap_button_2)
        self.Bind(wx.EVT_BUTTON, self.OnBuscarU, self.bitmap_button_3)
        self.Bind(wx.EVT_BUTTON, self.OnEditarU, self.bitmap_button_4)
        self.Bind(wx.EVT_BUTTON, self.OnBloquear, self.bitmap_button_5)
        self.Bind(wx.EVT_BUTTON, self.OnDesbloquear, self.bitmap_button_6)
        self.Bind(wx.EVT_BUTTON, self.OnSalir, self.bitmap_button_1)
        self.Bind(wx.EVT_BUTTON, self.OnRegistrarP, self.bitmap_button_9)
        self.Bind(wx.EVT_BUTTON, self.OnBuscarP, self.bitmap_button_8)
        self.Bind(wx.EVT_BUTTON, self.OnReportes, self.bitmap_button_10)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Principal.__set_properties
        self.SetTitle(_("frame_1"))
        self.bitmap_button_2.SetToolTip(wx.ToolTip(_("Registrar Usuario")))
        self.bitmap_button_2.SetSize(self.bitmap_button_2.GetBestSize())
        self.bitmap_button_3.SetToolTip(wx.ToolTip(_("Buscar Usuarios")))
        self.bitmap_button_3.SetSize(self.bitmap_button_3.GetBestSize())
        self.bitmap_button_4.SetToolTip(wx.ToolTip(_("Editar Usuarios")))
        self.bitmap_button_4.SetSize(self.bitmap_button_4.GetBestSize())
        self.bitmap_button_5.SetToolTip(wx.ToolTip(_("Bloquear Usuarios")))
        self.bitmap_button_5.SetSize(self.bitmap_button_5.GetBestSize())
        self.bitmap_button_6.SetToolTip(wx.ToolTip(_("Desbloquear Usuarios")))
        self.bitmap_button_6.SetSize(self.bitmap_button_6.GetBestSize())
        self.bitmap_button_1.SetSize(self.bitmap_button_1.GetBestSize())
        self.bitmap_button_9.SetToolTip(wx.ToolTip(_("Registrar Postulante")))
        self.bitmap_button_9.SetSize(self.bitmap_button_9.GetBestSize())
        self.bitmap_button_8.SetToolTip(wx.ToolTip(_("Buscar Postulante")))
        self.bitmap_button_8.SetSize(self.bitmap_button_8.GetBestSize())
        self.bitmap_button_10.SetToolTip(wx.ToolTip(_("Reportes")))
        self.bitmap_button_10.SetSize(self.bitmap_button_10.GetBestSize())
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Principal.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_3 = wx.FlexGridSizer(1, 3, 0, 0)
        grid_sizer_2 = wx.FlexGridSizer(1, 3, 0, 0)
        grid_sizer_1 = wx.FlexGridSizer(1, 10, 0, 0)
        grid_sizer_1.Add(self.bitmap_button_2, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_button_3, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_button_4, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_button_5, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_button_6, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_button_1, 0, wx.ALIGN_RIGHT, 0)
        self.notebook_1_pane_1.SetSizer(grid_sizer_1)
        grid_sizer_1.AddGrowableRow(0)
        grid_sizer_1.AddGrowableCol(9)
        self.notebook_1.AddPage(self.notebook_1_pane_1, _("Usuarios"))
        sizer_1.Add(self.notebook_1, 1, wx.EXPAND, 0)
        grid_sizer_2.Add(self.bitmap_button_9, 0, 0, 0)
        grid_sizer_2.Add((20, 20), 0, 0, 0)
        grid_sizer_2.Add(self.bitmap_button_8, 0, 0, 0)
        self.notebook_2_pane_1.SetSizer(grid_sizer_2)
        grid_sizer_2.AddGrowableRow(0)
        self.notebook_2.AddPage(self.notebook_2_pane_1, _("Postulantes"))
        sizer_1.Add(self.notebook_2, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.bitmap_button_10, 0, 0, 0)
        self.notebook_3_pane_1.SetSizer(grid_sizer_3)
        self.notebook_3.AddPage(self.notebook_3_pane_1, _("Reportes"))
        sizer_1.Add(self.notebook_3, 1, wx.EXPAND, 0)
        self.notebook_4.AddPage(self.notebook_4_pane_1, _("Informacion"))
        sizer_1.Add(self.notebook_4, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def OnRegistrarU(self, event):  # wxGlade: Principal.<event_handler>
        Ventana=GU.Principal(self)
        Ventana.Show()
    def OnBuscarU(self, event):  # wxGlade: Principal.<event_handler>
        Ventana=BU.Principal(self)
        Ventana.Show()

    def OnEditarU(self, event):  # wxGlade: Principal.<event_handler>
        Ventana=MU.Principal(self)
        Ventana.Show()

    def OnBloquear(self, event):  # wxGlade: Principal.<event_handler>
        Ventana=BQU.Principal(self)
        Ventana.Show()

    def OnDesbloquear(self, event):  # wxGlade: Principal.<event_handler>
        Ventana=DU.Principal(self)
        Ventana.Show()

    def OnSalir(self, event):  # wxGlade: Principal.<event_handler>
        dlg = wx.MessageDialog(None, '¿Desea Salir?',
                           'Dialogo de Mensage', wx.OK|wx.CANCEL|
                            wx.ICON_QUESTION)
        #dlg.ShowModal()
        

        if dlg.ShowModal()==wx.ID_OK:
            Ventana=E.Principal(self)
            Ventana.Show()
            self.Hide()
        dlg.Destroy()  

    def OnRegistrarP(self, event):  # wxGlade: Principal.<event_handler>
        Ventana=GP.Principal(self)
        Ventana.Show()
    def OnBuscarP(self, event):  # wxGlade: Principal.<event_handler>
        Ventana=BP.Principal(self)
        Ventana.Show()

    def OnReportes(self, event):  # wxGlade: Principal.<event_handler>
        Ventana=MEU.Principal(self)
        Ventana.Show()

# end of class Principal
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.App()
    #wx.InitAllImageHandlers()
    frame_1 = Principal(None, wx.ID_ANY, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
