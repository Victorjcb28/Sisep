#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# generated by wxGlade 0.7.1 on Tue Mar 21 10:19:48 2017
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
        self.vntPpal_BarraMenu = wx.MenuBar()
        self.archivo = wx.Menu()
        self.principal = wx.MenuItem(self.archivo, wx.ID_ANY, _("Principal"), _("Principal"), wx.ITEM_NORMAL)
        self.archivo.AppendItem(self.principal)
        self.vntPpal_BarraMenu.Append(self.archivo, _("Archivo"))
        self.SetMenuBar(self.vntPpal_BarraMenu)
        # Menu Bar end
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("Postulante Chofer"))
        self.label_4 = wx.StaticText(self, wx.ID_ANY, _(u"A\u00f1os de \nExperiencia:"))
        self.cobExperiencia = wx.ComboBox(self, wx.ID_ANY, choices=[_("0 > 3"), _("4 > 7"), _("7 > 10"), _(u"Mas de 11 a\u00f1os")], style=wx.CB_DROPDOWN)
        self.label_9 = wx.StaticText(self, wx.ID_ANY, _("Posee conocimientos\nde mecanica basica:"))
        self.cobMecanica = wx.ComboBox(self, wx.ID_ANY, choices=[_("SI"), _("NO")], style=wx.CB_DROPDOWN)
        self.label_6 = wx.StaticText(self, wx.ID_ANY, _("Se integra\nfacilmente a\ngrupos de trabajo:"))
        self.cobGTrabajo = wx.ComboBox(self, wx.ID_ANY, choices=[_("SI"), _("NO")], style=wx.CB_DROPDOWN)
        self.label_5 = wx.StaticText(self, wx.ID_ANY, _("Esta dispuesto a\ntrabajar horas extras:"))
        self.cobHoras = wx.ComboBox(self, wx.ID_ANY, choices=[_("SI"), _("NO")], style=wx.CB_DROPDOWN)
        self.label_2 = wx.StaticText(self, wx.ID_ANY, _("Tendria incoveniente \nen trabajar fuera \nde la ciudad:"))
        self.cobTFuera = wx.ComboBox(self, wx.ID_ANY, choices=[_("SI"), _("NO")], style=wx.CB_DROPDOWN)
        self.label_9_copy_copy = wx.StaticText(self, wx.ID_ANY, _("Aceptaria las normas\nimpuestas por a empresa:"))
        self.cobNormas = wx.ComboBox(self, wx.ID_ANY, choices=[_("SI"), _("NO")], style=wx.CB_DROPDOWN)
        self.label_11_copy_1 = wx.StaticText(self, wx.ID_ANY, _("Que tipo de \nlicencia posee:"))
        self.cobLicencia = wx.ComboBox(self, wx.ID_ANY, choices=[_("1"), _("2"), _("3"), _("4"), _("5")], style=wx.CB_DROPDOWN)
        self.label_13_copy = wx.StaticText(self, wx.ID_ANY, _("Esta dispuesto a aceptar\nlas normas de sus superiores:"))
        self.cobNormasS = wx.ComboBox(self, wx.ID_ANY, choices=[_("SI"), _("NO")], style=wx.CB_DROPDOWN)
        self.label_3 = wx.StaticText(self, wx.ID_ANY, _("Que tipo de transporte\nha manejado:"))
        self.cobTransporte = wx.ComboBox(self, wx.ID_ANY, choices=[_("LIVIANO"), _("PESADO")], style=wx.CB_DROPDOWN)
        self.label_7 = wx.StaticText(self, wx.ID_ANY, _("Ha tenido accidentes\nde transito:"))
        self.cobAccidente = wx.ComboBox(self, wx.ID_ANY, choices=[_("SI"), _("NO")], style=wx.CB_DROPDOWN)
        self.button_1 = wx.Button(self, wx.ID_ANY, _("Guardar"))
        self.button_2 = wx.Button(self, wx.ID_ANY, _("Limpiar"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.OnPrincipal, self.principal)
        self.Bind(wx.EVT_BUTTON, self.OnGuardar, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.OnLimpiar, self.button_2)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Principal.__set_properties
        self.SetTitle(_("Postulante Chofer"))
        self.SetSize((688, 558))
        self.label_1.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.cobExperiencia.SetMinSize((156, 40))
        self.cobExperiencia.SetSelection(-1)
        self.cobMecanica.SetMinSize((156, 40))
        self.cobMecanica.SetSelection(-1)
        self.cobGTrabajo.SetSelection(-1)
        self.cobHoras.SetSelection(-1)
        self.cobTFuera.SetSelection(-1)
        self.cobNormas.SetSelection(-1)
        self.cobLicencia.SetSelection(-1)
        self.cobNormasS.SetSelection(-1)
        self.cobTransporte.SetSelection(-1)
        self.cobAccidente.SetSelection(-1)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Principal.__do_layout
        vntPrincipal = wx.BoxSizer(wx.VERTICAL)
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(12, 5, 0, 0)
        sizer_1.Add(self.label_1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 20)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_4, 0, 0, 0)
        grid_sizer_1.Add(self.cobExperiencia, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_9, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.cobMecanica, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_6, 0, 0, 0)
        grid_sizer_1.Add(self.cobGTrabajo, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_5, 0, 0, 0)
        grid_sizer_1.Add(self.cobHoras, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_2, 0, 0, 0)
        grid_sizer_1.Add(self.cobTFuera, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_9_copy_copy, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.cobNormas, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_11_copy_1, 0, 0, 0)
        grid_sizer_1.Add(self.cobLicencia, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_13_copy, 0, 0, 0)
        grid_sizer_1.Add(self.cobNormasS, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_3, 0, 0, 0)
        grid_sizer_1.Add(self.cobTransporte, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_7, 0, 0, 0)
        grid_sizer_1.Add(self.cobAccidente, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.button_1, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.button_2, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.AddGrowableCol(1)
        grid_sizer_1.AddGrowableCol(3)
        sizer_1.Add(grid_sizer_1, 1, 0, 0)
        vntPrincipal.Add(sizer_1, 1, wx.EXPAND, 0)
        self.SetSizer(vntPrincipal)
        self.Layout()
        self.Centre()
        # end wxGlade

    def OnPrincipal(self, event):  # wxGlade: Principal.<event_handler>
        self.Close()

    def OnGuardar(self, event):  # wxGlade: Principal.<event_handler>
        f.GuardarChofer(self)
    

    def OnLimpiar(self, event):  # wxGlade: Principal.<event_handler>
        print "Event handler 'OnLimpiar' not implemented!"
        event.Skip()

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
            wx.MessageBox("Este campo debe contener algun texto!",
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
