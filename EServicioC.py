#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# generated by wxGlade 0.7.1 on Tue Apr 11 21:15:32 2017
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
        self.SetMenuBar(self.vntPpal_BarraMenu)
        # Menu Bar end
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("Postulante Servicio Cliente"))
        self.label_4 = wx.StaticText(self, wx.ID_ANY, _(u"\u00bfTiene experiencia ?"))
        self.cobExperiencia = wx.ComboBox(self, wx.ID_ANY, choices=[_("NO, PERO SOY UNA PERSONA QUE APRENDE RAPIDO Y MOTIVADA"), _("NO, PERO TENGO LOS CONOCIMIENTOS NECESARIOS PARA EL CARGO"), _("SI")], style=wx.CB_DROPDOWN)
        self.label_9 = wx.StaticText(self, wx.ID_ANY, _(u"\u00bfHa mejorado sus conocimientos en el ultimo a\u00f1o?"))
        self.cobMecanica = wx.ComboBox(self, wx.ID_ANY, choices=[_("SI, HE AUMENTADO MIS CONOCIMIENTOS LABORALES"), _("NO, HE ESTADO ESTANCADO"), _("MUY POCO")], style=wx.CB_DROPDOWN)
        self.label_6 = wx.StaticText(self, wx.ID_ANY, _(u"\u00bfSabe trabajar en equipo?"))
        self.cobGTrabajo = wx.ComboBox(self, wx.ID_ANY, choices=[_("SI"), _("NO"), _("MUY POCO")], style=wx.CB_DROPDOWN)
        self.label_5 = wx.StaticText(self, wx.ID_ANY, _(u"\u00bfQue haria si un cliente es grosero con Ud?"))
        self.cobHoras = wx.ComboBox(self, wx.ID_ANY, choices=[_("LE RESPONDE DE MANERA GROSERA"), _("HACE CASO OMISO DE SUS PROVOCACIONES"), _("ES AMABLE Y ESCUCHA LAS QUEJAS")], style=wx.CB_DROPDOWN)
        self.label_2 = wx.StaticText(self, wx.ID_ANY, _(u"\u00bfTrabaja bajo presion?"))
        self.cobTFuera = wx.ComboBox(self, wx.ID_ANY, choices=[_("NO, PERO HAY QUE AFRONTAR LA SITUACION"), _("NO, PREFIERO TRABAJAR A MI PROPIO RITMO"), _("SI, CREO QUE TRABAJO BIEN BAJO PRESION")], style=wx.CB_DROPDOWN)
        self.label_9_copy_copy = wx.StaticText(self, wx.ID_ANY, _(u"\u00bfQue hace cuando se encuentra en una situacion de estres?"))
        self.cobNormas = wx.ComboBox(self, wx.ID_ANY, choices=[_("ANALIZA LA SITUACION Y ABORDA LOS PROBLEMAS DE LA MANERA MAS EFICIENTE Y EFICAZ"), _("DEJA QUE LOS DEMAS HAGAN EL TRABAJO POR USTED"), _("PIERDE EL CONTROL DE LA SITUACION Y NO SABE QUE HACER")], style=wx.CB_DROPDOWN)
        self.label_11_copy_1 = wx.StaticText(self, wx.ID_ANY, _(u"\u00bfHabla con brusqueda a extra\u00f1os?"))
        self.cobLicencia = wx.ComboBox(self, wx.ID_ANY, choices=[_("RARA VEZ"), _("A VECES"), _("A MENUDO")], style=wx.CB_DROPDOWN)
        self.label_13_copy = wx.StaticText(self, wx.ID_ANY, _(u"\u00bfComo te enfrentas a comentarios negativos?"))
        self.cobNormasS = wx.ComboBox(self, wx.ID_ANY, choices=[_("OFRECE SOLUCIONES RAPIDAS Y EFECTIVAS"), _("UTILIZA UN TONO AMISTOSO Y MUESTRA INTERES POR EL PROBLEMA DEL CLIENTE"), _("HACE CASO OMISO A SU COMENTARIO")], style=wx.CB_DROPDOWN)
        self.label_3 = wx.StaticText(self, wx.ID_ANY, _(u"\u00bfTrata con cortesia a desconocidos?"))
        self.cobTransporte = wx.ComboBox(self, wx.ID_ANY, choices=[_("A MENUDO"), _("A VECES"), _("RARA VEZ")], style=wx.CB_DROPDOWN)
        self.label_7 = wx.StaticText(self, wx.ID_ANY, _(u"\u00bfTiene facilidad de expresion ante el publico?"))
        self.cobAccidente = wx.ComboBox(self, wx.ID_ANY, choices=[_("SI, ME EXPRESO DE MANERA NATURAL"), _("NO, ME DA NERVIOS"), _("MUY POCO")], style=wx.CB_DROPDOWN)
        self.button_1 = wx.Button(self, wx.ID_ANY, _("Guardar"))
        self.button_2 = wx.Button(self, wx.ID_ANY, _("Limpiar"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.OnGuardar, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.OnLimpiar, self.button_2)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Principal.__set_properties
        self.SetTitle(_("Postulante Servicio al Cliente"))
        self.SetSize((1144, 558))
        self.label_1.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.cobExperiencia.SetMinSize((250, 32))
        self.cobExperiencia.SetSelection(-1)
        self.cobMecanica.SetMinSize((250, 32))
        self.cobMecanica.SetSelection(-1)
        self.cobGTrabajo.SetMinSize((250, 32))
        self.cobGTrabajo.SetSelection(-1)
        self.cobHoras.SetMinSize((250, 32))
        self.cobHoras.SetSelection(-1)
        self.cobTFuera.SetMinSize((250, 32))
        self.cobTFuera.SetSelection(-1)
        self.cobNormas.SetMinSize((250, 32))
        self.cobNormas.SetSelection(-1)
        self.cobLicencia.SetMinSize((250, 32))
        self.cobLicencia.SetSelection(-1)
        self.cobNormasS.SetMinSize((250, 32))
        self.cobNormasS.SetSelection(-1)
        self.cobTransporte.SetMinSize((250, 32))
        self.cobTransporte.SetSelection(-1)
        self.cobAccidente.SetMinSize((250, 32))
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
        grid_sizer_1.Add(self.cobExperiencia, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_9, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.cobMecanica, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_6, 0, 0, 0)
        grid_sizer_1.Add(self.cobGTrabajo, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_5, 0, 0, 0)
        grid_sizer_1.Add(self.cobHoras, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_2, 0, 0, 0)
        grid_sizer_1.Add(self.cobTFuera, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_9_copy_copy, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.cobNormas, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_11_copy_1, 0, 0, 0)
        grid_sizer_1.Add(self.cobLicencia, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_13_copy, 0, 0, 0)
        grid_sizer_1.Add(self.cobNormasS, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_3, 0, 0, 0)
        grid_sizer_1.Add(self.cobTransporte, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_7, 0, 0, 0)
        grid_sizer_1.Add(self.cobAccidente, 0, 0, 0)
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
        pass

    def OnGuardar(self, event):  # wxGlade: Principal.<event_handler>
        if self.Validate():
            dlg = wx.MessageDialog(None, '¿Desea Guardar?',
                           'Dialogo de Mensage', wx.OK|wx.CANCEL|
                            wx.ICON_QUESTION)
        #dlg.ShowModal()
        

        if dlg.ShowModal()==wx.ID_OK:
            f.GuardarServicioC(self)
            self.Hide()
        dlg.Destroy()
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

