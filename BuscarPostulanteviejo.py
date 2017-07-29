#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# generated by wxGlade 0.7.1 on Mon Apr 10 11:58:16 2017
#

import wx
import funciones as f
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
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("Buscar Postulantes"))
        self.notebook_8 = wx.Notebook(self, wx.ID_ANY)
        self.notebook_8_pane_1 = wx.Panel(self.notebook_8, wx.ID_ANY)
        self.label_9 = wx.StaticText(self.notebook_8_pane_1, wx.ID_ANY, _("Nombres:"))
        self.txtNombre = wx.TextCtrl(self.notebook_8_pane_1, wx.ID_ANY, "")
        self.label_13 = wx.StaticText(self.notebook_8_pane_1, wx.ID_ANY, _("Estado:"))
        self.cobEstado = wx.ComboBox(self.notebook_8_pane_1, wx.ID_ANY, choices=[_("Amazonas"), _("Anzoategui"), _("Apure"), _("Aragua"), _("Barinas"), _("Bolivar"), _("Carabobo"), _("Cojedes"), _("Delta Amacuro"), _("Distrito Capital"), _("Falcon"), _("Guarico"), _("Lara"), _("Merida"), _("Miranda"), _("Monagas"), _("Nueva Esparta"), _("Portuguesa"), _("Sucre"), _("Tachira"), _("Trujillo"), _("Vargas"), _("Yaracuy"), _("Zulia")], style=wx.CB_DROPDOWN)
        self.label_10 = wx.StaticText(self.notebook_8_pane_1, wx.ID_ANY, _("Apellidos:"))
        self.txtApellidos = wx.TextCtrl(self.notebook_8_pane_1, wx.ID_ANY, "")
        self.label_14 = wx.StaticText(self.notebook_8_pane_1, wx.ID_ANY, _("Municipio:"))
        self.cobMunicipio = wx.ComboBox(self.notebook_8_pane_1, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.label_11 = wx.StaticText(self.notebook_8_pane_1, wx.ID_ANY, _("Cedula:"))
        self.txtCedula = wx.TextCtrl(self.notebook_8_pane_1, wx.ID_ANY, "")
        self.bitmap_button_1 = wx.BitmapButton(self.notebook_8_pane_1, wx.ID_ANY, wx.Bitmap("iconos/buscar.png", wx.BITMAP_TYPE_ANY))
        self.label_15 = wx.StaticText(self.notebook_8_pane_1, wx.ID_ANY, _("Parroquia:"))
        self.cobParroquia = wx.ComboBox(self.notebook_8_pane_1, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.label_12 = wx.StaticText(self.notebook_8_pane_1, wx.ID_ANY, _("Sexo:"))
        self.CobSexo = wx.ComboBox(self.notebook_8_pane_1, wx.ID_ANY, choices=[_("M"), _("F")], style=wx.CB_DROPDOWN)
        self.label_16 = wx.StaticText(self.notebook_8_pane_1, wx.ID_ANY, _("Direccion:"))
        self.txtDireccion = wx.TextCtrl(self.notebook_8_pane_1, wx.ID_ANY, "")
        self.notebook_9 = wx.Notebook(self, wx.ID_ANY)
        self.notebook_9_pane_1 = wx.Panel(self.notebook_9, wx.ID_ANY)
        self.label_17 = wx.StaticText(self.notebook_9_pane_1, wx.ID_ANY, _("Nivel de Instruccion:"))
        self.cobEducacion = wx.ComboBox(self.notebook_9_pane_1, wx.ID_ANY, choices=[_("PRIMARIA"), _("SECUNDARIA"),_("PREGRADO"), _("POSTGRADO")], style=wx.CB_DROPDOWN)
        self.label_18 = wx.StaticText(self.notebook_9_pane_1, wx.ID_ANY, _("Titulo:"))
        self.txtTitulo = wx.TextCtrl(self.notebook_9_pane_1, wx.ID_ANY, "")
        self.label_19 = wx.StaticText(self.notebook_9_pane_1, wx.ID_ANY, _("Idioma:"))
        self.cobIdioma = wx.ComboBox(self.notebook_9_pane_1, wx.ID_ANY, choices=[_("INGLES"), _("OTROS")], style=wx.CB_DROPDOWN)
        self.notebook_10 = wx.Notebook(self, wx.ID_ANY)
        self.notebook_10_pane_1 = wx.Panel(self.notebook_10, wx.ID_ANY)
        self.label_2 = wx.StaticText(self.notebook_10_pane_1, wx.ID_ANY, _("Salario:"))
        self.cobSalario = wx.ComboBox(self.notebook_10_pane_1, wx.ID_ANY, choices=[_("Salario Minimo"), _("Mayor a Salario Minimo")], style=wx.CB_DROPDOWN)
        self.label_3 = wx.StaticText(self.notebook_10_pane_1, wx.ID_ANY, _("Vigente:"))
        self.cobVigente = wx.ComboBox(self.notebook_10_pane_1, wx.ID_ANY, choices=[_("SI"), _("NO")], style=wx.CB_DROPDOWN)
        self.label_4 = wx.StaticText(self.notebook_10_pane_1, wx.ID_ANY, _("Cargo:"))
        self.cobCargo = wx.ComboBox(self.notebook_10_pane_1, wx.ID_ANY, choices=[_("ADMINISTRACION"), _("ASISTENTE"), _("CAJERO"), _("CHOFER"), _("VIGILANTE"), _("GERENTE VENTAS"), _("ASISTENTE VENTAS"), _("SERVICIO AL CLIENTE"), _("RECURSOS HUMANOS")], style=wx.CB_DROPDOWN)
        self.button_1 = wx.Button(self, wx.ID_ANY, _("Modificar"))
        self.button_2 = wx.Button(self, wx.ID_ANY, _("Limpiar"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.OnPrincipal, self.principal)
        self.Bind(wx.EVT_TEXT, self.OnLetras, self.txtNombre)
        self.Bind(wx.EVT_TEXT, self.OnEstado, self.cobEstado)
        self.Bind(wx.EVT_TEXT, self.OnLetras, self.txtApellidos)
        self.Bind(wx.EVT_TEXT, self.OnMunicipio, self.cobMunicipio)
        self.Bind(wx.EVT_TEXT, self.OnCedula, self.txtCedula)
        self.Bind(wx.EVT_BUTTON, self.OnBuscar, self.bitmap_button_1)
        self.Bind(wx.EVT_BUTTON, self.OnModificar, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.OnLimpiar, self.button_2)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Principal.__set_properties
        self.SetTitle(_("Buscar Postulante"))
        self.SetSize((694, 627))
        self.label_1.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.txtNombre.Enable(False)
        self.cobEstado.Enable(False)
        self.txtApellidos.Enable(False)
        self.cobMunicipio.Enable(False)
        self.bitmap_button_1.SetSize(self.bitmap_button_1.GetBestSize())
        self.cobParroquia.Enable(False)
        self.CobSexo.Enable(False)
        self.CobSexo.SetSelection(-1)
        self.txtDireccion.Enable(False)
        self.cobEducacion.SetMinSize((200, 36))
        self.cobEducacion.Enable(False)
        self.cobEducacion.SetSelection(-1)
        self.txtTitulo.SetMinSize((200, 36))
        self.txtTitulo.Enable(False)
        self.cobIdioma.SetMinSize((200, 36))
        self.cobIdioma.Enable(False)
        self.cobIdioma.SetSelection(-1)
        self.cobSalario.SetMinSize((275, 36))
        self.cobSalario.Enable(False)
        self.cobSalario.SetSelection(-1)
        self.cobVigente.SetMinSize((275, 36))
        self.cobVigente.Enable(False)
        self.cobVigente.SetSelection(-1)
        self.cobCargo.SetMinSize((275, 36))
        self.cobCargo.Enable(False)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Principal.__do_layout
        grid_sizer_3 = wx.FlexGridSizer(5, 1, 0, 0)
        grid_sizer_2 = wx.GridSizer(1, 4, 0, 0)
        grid_sizer_1 = wx.FlexGridSizer(3, 2, 0, 0)
        grid_sizer_5 = wx.FlexGridSizer(3, 2, 0, 0)
        grid_sizer_4 = wx.FlexGridSizer(4, 5, 0, 0)
        grid_sizer_3.Add(self.label_1, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_4.Add(self.label_9, 0, 0, 0)
        grid_sizer_4.Add(self.txtNombre, 0, wx.EXPAND, 0)
        grid_sizer_4.Add((20, 20), 0, 0, 0)
        grid_sizer_4.Add(self.label_13, 0, 0, 0)
        grid_sizer_4.Add(self.cobEstado, 0, wx.EXPAND, 0)
        grid_sizer_4.Add(self.label_10, 0, 0, 0)
        grid_sizer_4.Add(self.txtApellidos, 0, wx.EXPAND, 0)
        grid_sizer_4.Add((20, 20), 0, 0, 0)
        grid_sizer_4.Add(self.label_14, 0, 0, 0)
        grid_sizer_4.Add(self.cobMunicipio, 0, wx.EXPAND, 0)
        grid_sizer_4.Add(self.label_11, 0, 0, 0)
        grid_sizer_4.Add(self.txtCedula, 0, wx.EXPAND, 0)
        grid_sizer_4.Add(self.bitmap_button_1, 0, 0, 0)
        grid_sizer_4.Add(self.label_15, 0, 0, 0)
        grid_sizer_4.Add(self.cobParroquia, 0, wx.EXPAND, 0)
        grid_sizer_4.Add(self.label_12, 0, 0, 0)
        grid_sizer_4.Add(self.CobSexo, 0, wx.EXPAND, 0)
        grid_sizer_4.Add((20, 20), 0, 0, 0)
        grid_sizer_4.Add(self.label_16, 0, 0, 0)
        grid_sizer_4.Add(self.txtDireccion, 0, wx.EXPAND, 0)
        self.notebook_8_pane_1.SetSizer(grid_sizer_4)
        grid_sizer_4.AddGrowableRow(0)
        grid_sizer_4.AddGrowableRow(1)
        grid_sizer_4.AddGrowableRow(2)
        grid_sizer_4.AddGrowableRow(3)
        grid_sizer_4.AddGrowableCol(1)
        grid_sizer_4.AddGrowableCol(4)
        self.notebook_8.AddPage(self.notebook_8_pane_1, _("Datos Personales"))
        grid_sizer_3.Add(self.notebook_8, 1, wx.EXPAND, 0)
        grid_sizer_5.Add(self.label_17, 0, 0, 0)
        grid_sizer_5.Add(self.cobEducacion, 0, 0, 0)
        grid_sizer_5.Add(self.label_18, 0, 0, 0)
        grid_sizer_5.Add(self.txtTitulo, 0, 0, 0)
        grid_sizer_5.Add(self.label_19, 0, 0, 0)
        grid_sizer_5.Add(self.cobIdioma, 0, 0, 0)
        self.notebook_9_pane_1.SetSizer(grid_sizer_5)
        grid_sizer_5.AddGrowableCol(1)
        self.notebook_9.AddPage(self.notebook_9_pane_1, _("Educacion"))
        grid_sizer_3.Add(self.notebook_9, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_2, 0, 0, 0)
        grid_sizer_1.Add(self.cobSalario, 0, 0, 0)
        grid_sizer_1.Add(self.label_3, 0, 0, 0)
        grid_sizer_1.Add(self.cobVigente, 0, 0, 0)
        grid_sizer_1.Add(self.label_4, 0, 0, 0)
        grid_sizer_1.Add(self.cobCargo, 0, 0, 0)
        self.notebook_10_pane_1.SetSizer(grid_sizer_1)
        grid_sizer_1.AddGrowableCol(1)
        self.notebook_10.AddPage(self.notebook_10_pane_1, _("Estatus"))
        grid_sizer_3.Add(self.notebook_10, 1, wx.EXPAND, 0)
        grid_sizer_2.Add((150, 20), 0, 0, 0)
        grid_sizer_2.Add(self.button_1, 0, 0, 0)
        grid_sizer_2.Add((50, 20), 0, 0, 0)
        grid_sizer_2.Add(self.button_2, 0, 0, 0)
        grid_sizer_3.Add(grid_sizer_2, 1, 0, 0)
        self.SetSizer(grid_sizer_3)
        grid_sizer_3.AddGrowableRow(1)
        grid_sizer_3.AddGrowableRow(2)
        grid_sizer_3.AddGrowableRow(3)
        grid_sizer_3.AddGrowableCol(0)
        self.Layout()
        self.Centre()
        # end wxGlade

    def OnPrincipal(self, event):  # wxGlade: Principal.<event_handler>
        dlg = wx.MessageDialog(None, '¿Desea Salir?',
                           'Dialogo de Mensage', wx.OK|wx.CANCEL|
                            wx.ICON_QUESTION)
        #dlg.ShowModal()
        

        if dlg.ShowModal()==wx.ID_OK:
            
            self.Hide()
        dlg.Destroy()
    
    def OnLetras(self, event):  # wxGlade: Principal.<event_handler>
        frm=self
        Campo=frm.txtNombre.GetValue()
        Campo2=frm.txtApellidos.GetValue()
        for i in Campo:
            if chr(33)==i or chr(34)==i or chr(35)==i or chr(36)==i or chr(37)==i or chr(38)==i or chr(39)==i or chr(40)==i or chr(41)==i or chr(42)==i or chr(43)==i or chr(44)==i or chr(45)==i or chr(46)==i or chr(47)==i or chr(48)==i or chr(49)==i or chr(50)==i or chr(51)==i or chr(52)==i or chr(53)==i or chr(54)==i or chr(55)==i or chr(56)==i or chr(57)==i or chr(58)==i or chr(59)==i or chr(60)==i or chr(61)==i or chr(62)==i or chr(63)==i:
                dlg=wx.MessageDialog(self,'Debe Ingresar Solo Letras', 'Atencion', wx.OK)
                dlg.ShowModal()
                dlg.Destroy()
                self.txtNombre.Clear()
            else:
                pass
        for i in Campo2:
            if chr(33)==i or chr(34)==i or chr(35)==i or chr(36)==i or chr(37)==i or chr(38)==i or chr(39)==i or chr(40)==i or chr(41)==i or chr(42)==i or chr(43)==i or chr(44)==i or chr(45)==i or chr(46)==i or chr(47)==i or chr(48)==i or chr(49)==i or chr(50)==i or chr(51)==i or chr(52)==i or chr(53)==i or chr(54)==i or chr(55)==i or chr(56)==i or chr(57)==i or chr(58)==i or chr(59)==i or chr(60)==i or chr(61)==i or chr(62)==i or chr(63)==i:
                dlg=wx.MessageDialog(self,'Debe Ingresar Solo Letras', 'Atencion', wx.OK)
                dlg.ShowModal()
                dlg.Destroy()
                self.txtApellidos.Clear()
            else:
                pass
    
    def OnCedula(self, event):  # wxGlade: Principal.<event_handler>
        frm=self
        Campo=frm.txtCedula.GetValue()
        if len(Campo)> 8 :
            dlg=wx.MessageDialog(self,'La Cedula no debe ser mayor a 8 caracteres', 'Atencion', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
            self.txtCedula.Clear()
        else:
            if Campo.isdigit() :
                pass
            else:
                if len(Campo)==0:
                    pass
                else:
                    dlg=wx.MessageDialog(self,'No puede Tener Letras', 'Atencion', wx.OK)
                    dlg.ShowModal()
                    dlg.Destroy()
                    self.txtCedula.Clear()



    def OnGuardar(self, event):  # wxGlade: Principal.<event_handler>
        pass

    def OnLimpiar(self, event):  # wxGlade: Principal.<event_handler>
        self.txtNombre.Clear()
        self.txtApellidos.Clear()
        self.txtCedula.Clear()
        
        self.cobMunicipio.Clear()
        self.cobParroquia.Clear()
        self.txtDireccion.Clear()

        self.txtTitulo.Clear()
    
    def OnBuscar(self, event):  # wxGlade: Principal.<event_handler>
        #Validamos campos en blanco
        

        if len(self.txtCedula.GetValue())==0:
            wx.MessageBox("No puede tener campos en blanco",
                          "Error")
            self.txtCedula.SetBackgroundColour("red")
            self.txtCedula.SetFocus()
            self.txtCedula.Refresh()

        else:
            f.BuscarPostulantes(self)
    
    def OnModificar(self, event):  # wxGlade: Principal.<event_handler>
        #Validamos campos en blanco
        if len(self.txtNombre.GetValue())==0:
            wx.MessageBox("No puede tener campos en blanco",
                          "Error")
            self.txtNombre.SetBackgroundColour("red")
            self.txtNombre.SetFocus()
            self.txtNombre.Refresh()

        elif len(self.txtApellidos.GetValue())==0:
            wx.MessageBox("No puede tener campos en blanco",
                          "Error")
            self.txtApellidos.SetBackgroundColour("red")
            self.txtApellidos.SetFocus()
            self.txtApellidos.Refresh()

        elif len(self.txtCedula.GetValue())==0:
            wx.MessageBox("No puede tener campos en blanco",
                          "Error")
            self.txtCedula.SetBackgroundColour("red")
            self.txtCedula.SetFocus()
            self.txtCedula.Refresh()

        elif len(self.CobSexo.GetValue())==0:
            wx.MessageBox("No puede tener campos en blanco",
                          "Error")
            self.CobSexo.SetBackgroundColour("red")
            self.CobSexo.SetFocus()
            self.CobSexo.Refresh()

        elif len(self.cobEstado.GetValue())==0:
            wx.MessageBox("No puede tener campos en blanco",
                          "Error")
            self.cobEstado.SetBackgroundColour("red")
            self.cobEstado.SetFocus()
            self.cobEstado.Refresh()

        elif len(self.cobMunicipio.GetValue())==0:
            wx.MessageBox("No puede tener campos en blanco",
                          "Error")
            self.cobMunicipio.SetBackgroundColour("red")
            self.cobMunicipio.SetFocus()
            self.cobMunicipio.Refresh()

        elif len(self.cobParroquia.GetValue())==0:
            wx.MessageBox("No puede tener campos en blanco",
                          "Error")
            self.cobParroquia.SetBackgroundColour("red")
            self.cobParroquia.SetFocus()
            self.cobParroquia.Refresh()

        elif len(self.txtDireccion.GetValue())==0:
            wx.MessageBox("No puede tener campos en blanco",
                          "Error")
            self.txtDireccion.SetBackgroundColour("red")
            self.txtDireccion.SetFocus()
            self.txtDireccion.Refresh()

        elif len(self.cobEducacion.GetValue())==0:
            wx.MessageBox("No puede tener campos en blanco",
                          "Error")
            self.cobEducacion.SetBackgroundColour("red")
            self.cobEducacion.SetFocus()
            self.cobEducacion.Refresh()

        elif len(self.txtTitulo.GetValue())==0:
            wx.MessageBox("No puede tener campos en blanco",
                          "Error")
            self.txtTitulo.SetBackgroundColour("red")
            self.txtTitulo.SetFocus()
            self.txtTitulo.Refresh()

        elif len(self.cobIdioma.GetValue())==0:
            wx.MessageBox("No puede tener campos en blanco",
                          "Error")
            self.cobIdioma.SetBackgroundColour("red")
            self.cobIdioma.SetFocus()
            self.cobIdioma.Refresh()

        elif len(self.cobSalario.GetValue())==0:
            wx.MessageBox("No puede tener campos en blanco",
                          "Error")
            self.cobSalario.SetBackgroundColour("red")
            self.cobSalario.SetFocus()
            self.cobSalario.Refresh()

        elif len(self.cobVigente.GetValue())==0:
            wx.MessageBox("No puede tener campos en blanco",
                          "Error")
            self.cobVigente.SetBackgroundColour("red")
            self.cobVigente.SetFocus()
            self.cobVigente.Refresh()

        elif len(self.cobCargo.GetValue())==0:
            wx.MessageBox("No puede tener campos en blanco",
                          "Error")
            self.cobCargo.SetBackgroundColour("red")
            self.cobCargo.SetFocus()
            self.cobCargo.Refresh()


        else:
            dlg = wx.MessageDialog(None, '¿Desea Modificar?',
                           'Dialogo de Mensage', wx.OK|wx.CANCEL|
                            wx.ICON_QUESTION)
        #dlg.ShowModal()
        

            if dlg.ShowModal()==wx.ID_OK:
            
                f.ModificarPostulante(self)
            dlg.Destroy()
            
    def OnEstado(self, event):  # wxGlade: Principal.<event_handler>
        f.BuscarM(self)
    def OnMunicipio(self, event):  # wxGlade: Principal.<event_handler>
        f.BuscarP(self)
# end of class Principal