#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.7.1 on Wed Jul  5 21:00:37 2017
#

import wx
import funciones as f
import os
from datetime import datetime, date, time, timedelta
from time import time
import datetime
# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class Principal(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Principal.__init__
        wx.Frame.__init__(self, *args, **kwds)
        self.label_2 = wx.StaticText(self, wx.ID_ANY, _("Desde:"))
        self.txtDesde = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_3 = wx.StaticText(self, wx.ID_ANY, _("Hasta"))
        self.txtHasta = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_2 = wx.Button(self, wx.ID_ANY, _("Buscar"))
        self.button_3 = wx.Button(self, wx.ID_ANY, _("Limpiar"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TEXT_ENTER, self.Rango, self.txtDesde)
        self.Bind(wx.EVT_TEXT, self.Rango, self.txtDesde)
        self.Bind(wx.EVT_TEXT_ENTER, self.Rango, self.txtHasta)
        self.Bind(wx.EVT_TEXT, self.Rango, self.txtHasta)
        self.Bind(wx.EVT_BUTTON, self.OnBuscar, self.button_2)
        self.Bind(wx.EVT_BUTTON, self.OnLimpiar, self.button_3)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Principal.__set_properties
        self.SetTitle(_("Rango de Fecha"))
        self.txtDesde.SetMinSize((150, 32))
        self.txtHasta.SetMinSize((150, 32))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Principal.__do_layout
        grid_sizer_1 = wx.FlexGridSizer(3, 8, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_2, 0, 0, 0)
        grid_sizer_1.Add(self.txtDesde, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_3, 0, 0, 0)
        grid_sizer_1.Add(self.txtHasta, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.button_2, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.button_3, 0, wx.ALIGN_CENTER, 0)
        self.SetSizer(grid_sizer_1)
        grid_sizer_1.Fit(self)
        self.Layout()
        self.Centre()
        # end wxGlade

    def Rango(self, event):  # wxGlade: Principal.<event_handler>
        frm=self
    
        campo=frm.txtDesde.GetValue()
        campo2=frm.txtHasta.GetValue()

        for i in campo:
            if chr(45)==i or chr(33)==i or chr(34)==i or chr(35)==i or chr(36)==i or chr(37)==i or chr(38)==i or chr(39)==i or chr(40)==i or chr(41)==i or chr(42)==i or chr(43)==i or chr(44)==i or chr(45)==i or chr(46)==i or chr(47)==i or chr(48)==i or chr(49)==i or chr(50)==i or chr(51)==i or chr(52)==i or chr(53)==i or chr(54)==i or chr(55)==i or chr(56)==i or chr(57)==i or chr(58)==i or chr(59)==i or chr(60)==i or chr(61)==i or chr(62)==i or chr(63)==i:
                pass
            else:

                dlg=wx.MessageDialog(self,'Debe Ingresar Solo Numeros', 'Atencion', wx.OK)
                dlg.ShowModal()
                dlg.Destroy()
                self.txtDesde.Clear()
                 
        for i in campo2:
            if chr(45)==i or chr(33)==i or chr(34)==i or chr(35)==i or chr(36)==i or chr(37)==i or chr(38)==i or chr(39)==i or chr(40)==i or chr(41)==i or chr(42)==i or chr(43)==i or chr(44)==i or chr(45)==i or chr(46)==i or chr(47)==i or chr(48)==i or chr(49)==i or chr(50)==i or chr(51)==i or chr(52)==i or chr(53)==i or chr(54)==i or chr(55)==i or chr(56)==i or chr(57)==i or chr(58)==i or chr(59)==i or chr(60)==i or chr(61)==i or chr(62)==i or chr(63)==i:
                pass
            else:

                dlg=wx.MessageDialog(self,'Debe Ingresar Solo Numeros', 'Atencion', wx.OK)
                dlg.ShowModal()
                dlg.Destroy()
                self.txtHasta.Clear()
                  



        if len(campo)==2 :
            dia=campo[0]+campo[1]

            self.txtDesde.SetValue(dia+"-")
            self.txtDesde.SetFocus()
        if len(campo)==5:
            dia=campo[0]+campo[1]
            mes=campo[3]+campo[4]
            self.txtDesde.SetValue(dia+"-"+mes+"-")
        if len(campo2)==2 :
            dia2=campo2[0]+campo2[1]

            self.txtHasta.SetValue(dia2+"-")
            self.txtHasta.SetFocus()
        if len(campo2)==5:
            dia2=campo2[0]+campo2[1]
            mes2=campo2[3]+campo2[4]
            self.txtHasta.SetValue(dia2+"-"+mes2+"-")


        if len(campo)>10 :
            dlg=wx.MessageDialog(self,'Debe Escribir la fecha en formato dd-mm-aaaa', 'Atencion', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
            self.txtDesde.Clear()
            self.txtHasta.Clear()
        elif len(campo2)>10:
            dlg=wx.MessageDialog(self,'Debe Escribir la fecha en formato dd-mm-aaaa', 'Atencion', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
            
            self.txtHasta.Clear()


    def OnBuscar(self, event):  # wxGlade: Principal.<event_handler>
        frm=self
        
        campo=frm.txtDesde.GetValue()
        campo2=frm.txtHasta.GetValue()
        
        
        
        if len(self.txtDesde.GetValue())==0 and len(self.txtHasta.GetValue())==0:
            dlg = wx.MessageDialog(None, 'Campos en blanco traera la informacion en su totalidad ¿Desea continuar?',
                           'Dialogo de Mensage', wx.OK|wx.CANCEL|
                            wx.ICON_QUESTION)
            #dlg.ShowModal()
            

            if dlg.ShowModal()==wx.ID_OK:
                
                f.ReporPostulantes(self)
                self.Hide()
                
            dlg.Destroy()
        else:
            dia=campo[0]+campo[1]
            mes=campo[3]+campo[4]
            ano=campo[6]+campo[7]+campo[8]+campo[9]
            dia2=campo2[0]+campo2[1]
            mes2=campo2[3]+campo2[4]
            ano2=campo[6]+campo[7]+campo[8]+campo[9]
            d=date.today()
            j=int(d.year)

            if (dia>dia2 and mes==mes2) or (mes>mes2)  or (ano2>ano)  :
                dlg=wx.MessageDialog(self,'La fecha DESDE no debe ser mayor a HASTA', 'Atencion', wx.OK)
                dlg.ShowModal()
                dlg.Destroy()


            elif (dia>="32" or dia2>="32") or (dia>="31" or dia2>="31" and (mes=="04" or mes2=="04")) or (dia>="31" or dia2>="31" and (mes=="06" or mes2=="06")) or (dia>="31" or dia2>="31" and (mes=="09" or mes2=="09")) or (dia>="31" or dia2>="31" and (mes=="11" or mes2=="11")) or (dia=="29" and mes=="02") or (dia=="30" and mes=="02") or (dia=="31" and mes=="02") or (dia2=="29" and mes2=="02") or (dia2=="30" and mes2=="02") or (dia2=="31" and mes2=="02"):
                dlg=wx.MessageDialog(self,'Fecha errada', 'Atencion', wx.OK)
                dlg.ShowModal()
                dlg.Destroy()

                
            elif (int(ano) > j)or (int(ano2)>j):

                dlg=wx.MessageDialog(self,'El año no puede ser mayor al actual', 'Atencion', wx.OK)
                dlg.ShowModal()
                dlg.Destroy()
            else:
                f.ReporPostulantesFecha(self)
                self.Hide()

    def OnLimpiar(self, event):  # wxGlade: Principal.<event_handler>
        dlg = wx.MessageDialog(None, '¿Desea Limpiar?',
                           'Dialogo de Mensage', wx.OK|wx.CANCEL|
                            wx.ICON_QUESTION)
        #dlg.ShowModal()
        

        if dlg.ShowModal()==wx.ID_OK:
            
            self.txtDesde.Clear()
            self.txtHasta.Clear()
            
        dlg.Destroy()

# end of class Principal
