#!/usr/bin/env python
# -*- coding: CP1252 -*-
#
# generated by wxGlade 0.7.1 on Tue Mar 14 21:27:06 2017
#

import wx
import funciones as f
import PrincipalAdmin as PA

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class Principal(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Principal.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.frame_1_menubar = wx.MenuBar()
        self.archivo = wx.Menu()
        self.prinicipal = wx.MenuItem(self.archivo, wx.ID_ANY, _(" "), _(" "), wx.ITEM_NORMAL)
        self.archivo.AppendItem(self.prinicipal)
        self.frame_1_menubar.Append(self.archivo, _(" "))
        self.SetMenuBar(self.frame_1_menubar)
        # Menu Bar end
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("Bloquear Usuario"))
        self.bitmap_1 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("iconos/Inicio_sesion.gif", wx.BITMAP_TYPE_ANY))
        self.label_3 = wx.StaticText(self, wx.ID_ANY, _("Usuario"))
        self.txtNombre = wx.TextCtrl(self, wx.ID_ANY, "")
        self.bitmap_button_4 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("iconos/buscar.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_2 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("iconos/9152064-boton-de-nombre-de-usuario-y-contrasena-ademas-de-inicio-de-sesion-en-un-candado-para-acceso-seguro-.jpg", wx.BITMAP_TYPE_ANY))
        self.label_4 = wx.StaticText(self, wx.ID_ANY, _("Clave"))
        self.txtClave = wx.TextCtrl(self, wx.ID_ANY, "",style=wx.TE_PASSWORD)
        self.bitmap_3 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("iconos/nuevo.png", wx.BITMAP_TYPE_ANY))
        self.label_2 = wx.StaticText(self, wx.ID_ANY, _("Tipo"))
        self.cobTipo = wx.ComboBox(self, wx.ID_ANY, choices=[_("ADMINISTRADOR"), _("SECRETARIA")], style=wx.CB_DROPDOWN)
        self.button_1 = wx.Button(self, wx.ID_ANY, _("Bloquear"))
        self.button_2 = wx.Button(self, wx.ID_ANY, _("Limpiar"))

        self.__set_properties()
        self.txtNombre.SetValidator(ContieneDatos())#activa la validacion
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.OnSalir, self.prinicipal)
        self.Bind(wx.EVT_BUTTON, self.OnBuscar, self.bitmap_button_4)
        self.Bind(wx.EVT_BUTTON, self.OnBloquear, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.OnLimpiar, self.button_2)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Principal.__set_properties
        self.SetTitle(_("Bloquear Usuario"))
        self.SetSize((400, 293))
        self.label_1.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.bitmap_button_4.SetSize(self.bitmap_button_4.GetBestSize())
        self.txtClave.Enable(False)
        self.cobTipo.Enable(False)
        self.cobTipo.SetSelection(-1)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Principal.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(5, 4, 0, 0)
        grid_sizer_2 = wx.GridSizer(1, 2, 0, 0)
        sizer_2.Add(self.label_1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 20)
        grid_sizer_1.Add(self.bitmap_1, 0, 0, 0)
        grid_sizer_1.Add(self.label_3, 0, 0, 0)
        grid_sizer_1.Add(self.txtNombre, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.bitmap_button_4, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_2, 0, 0, 0)
        grid_sizer_1.Add(self.label_4, 0, 0, 0)
        grid_sizer_1.Add(self.txtClave, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_3, 0, 0, 0)
        grid_sizer_1.Add(self.label_2, 0, 0, 0)
        grid_sizer_1.Add(self.cobTipo, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_2.Add(self.button_1, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_2.Add(self.button_2, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.AddGrowableCol(2)
        sizer_2.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_2)
        self.Layout()
        self.Centre()
        # end wxGlade

    def OnSalir(self, event):  # wxGlade: Principal.<event_handler>
        dlg = wx.MessageDialog(None, '¿Desea Salir?',
                           'Dialogo de Mensage', wx.OK|wx.CANCEL|
                            wx.ICON_QUESTION)
        #dlg.ShowModal()
        

        if dlg.ShowModal()==wx.ID_OK:
            
            self.Hide()
        dlg.Destroy()  

    def OnBuscar(self, event):  # wxGlade: Principal.<event_handler>
        if self.Validate():
            f.BuscarU2(self)

    def OnBloquear(self, event):  # wxGlade: Principal.<event_handler>
         if self.Validate():
            dlg = wx.MessageDialog(None, '¿Desea Bloquear?',
                           'Diálogo de Mensage', wx.OK|wx.CANCEL|
                            wx.ICON_QUESTION)
        #dlg.ShowModal()
        

            if dlg.ShowModal()==wx.ID_OK:
            
                f.Bloquear(self)
                self.txtNombre.Clear()
                self.txtClave.Clear()
                self.cobTipo.Clear()
            dlg.Destroy() 
            

    def OnLimpiar(self, event):  # wxGlade: Principal.<event_handler>
        self.txtNombre.Clear()
        self.txtClave.Clear()
        self.cobTipo.Clear()

# end of class Principal
class ContieneDatos(wx.PyValidator):
    def __init__(self):
        wx.PyValidator.__init__(self)

    def Clone(self):
        """
        Note que todo validador debe implementar
        # el método Clone().
        """
        return ContieneDatos()

    def Validate(self, win):
        textCtrl = self.GetWindow()
        text = textCtrl.GetValue()
        if len(text) == 0:
            wx.MessageBox("Este campo debe contener algún texto!",
                          "Error")
            textCtrl.SetBackgroundColour("red")
            textCtrl.SetFocus()
            textCtrl.Refresh()
            return False
        else:
            textCtrl.SetBackgroundColour(
                               wx.SystemSettings_GetColour(
                               wx.SYS_COLOUR_WINDOW))
            textCtrl.Refresh()
            return True

    def TransferToWindow(self):
        return True

    def TransferFromWindow(self):
        return True
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.App()
    #wx.InitAllImageHandlers()
    frame_1 = Principal(None, wx.ID_ANY, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
