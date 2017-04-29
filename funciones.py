#! /usr/bin/env python
# -*- coding: UTF-8 -*-
#self.db.execute(SQL_STRING, (dork.decode('utf-8'), ))

import sqlite3 as sq3
import wx
import hashlib

import entrada as E
import PrincipalAdmin as PA

import EChofer as EC

import EAdministracion as EA
import EAdministracionM as EAM

import EAsistenteA as EAA
import EAsistenteAM as EAAM

import ECajero as ECA
import ECajeroM as ECAM

import EServicioC as ESC
import EServicioCM as ESCM


import ERecursosH as ERH
import ERecursosHM as ERHM

import ECompraVenta as ECV
import ECompraVentaM as ECVM

import ECompraVenta1 as ECV1
import ECompraVenta1M as ECV1M

import EVigilante as EV
import EVigilanteM as EVM


from datetime import datetime, date, time, timedelta
from time import time
import datetime



#Conexion base de datos
def conexion():
    con=sq3.connect('Sisep.s3db')
    cur = con.cursor()
    return con, cur

def desconectar():
    cur.Close()
    con.Close()
    return


#funciones nuevas.

def Edad(frm):
    self=frm
    dia=int(frm.cobDia.GetValue())
    mes=int(frm.cobMes.GetValue())
    ano=int(frm.cobAno.GetValue())

    d=date.today()
    ano1=d.year-ano
    if d.month <= mes:
        if d.day < dia:
            ano1=ano1-1 
    self.txtEdad.SetValue(str(ano1))

def Ano(frm):
    self=frm
    d=date.today()
    j=int(d.year)+1
    i=int(d.year)-100
    while j>i:
        ano1=j-1 
        self.cobAno.Append(str(ano1))
        j=j-1
        

def Administrativo(frm):

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Seleccionar Postulante"
    Nom="ADMINISTRACION"
    self=frm
    con, cur=conexion()
    cur.execute("Select min(Usuario) from Bitacora")
    rs2=cur.fetchone()
    if rs2:
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Nom,Hora,Op))
        con.commit()
        
                    

#fin funciones nuevas        

def Bitacora(frm):
    Usu=frm.txtUsuario.GetValue()
    En=Usu.upper()
    
    Hora=datetime.datetime.now()
    
    Fecha = datetime.date.today()
    datos=(En,Fecha,Hora)

    con,cur=conexion()


    cur.execute("Insert into Bitacora (Usuario,Fecha,Hora) Values (?,?,?)", (En,Fecha,Hora))
    

    con.commit()
    cur.close()
    con.close()

def Entrada(frm):

    Usu=frm.txtUsuario.GetValue()
    En=Usu.upper()
    Cl=hashlib.md5(frm.txtClave.GetValue())
    Cla=Cl.hexdigest()
    datos=(En,Cla)

    con,cur=conexion()
    self=frm

    cur.execute("Select Estado from Usuarios where Estado= 1 and Nombre=:En",{"En":En})
    rs=cur.fetchone()

    if rs:
        dlg=wx.MessageDialog(self,'Usuario Bloqueado', 'Atencion', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
    else:
        cur.execute("Select * from Usuarios Where Nombre=? and Clave=? and Tipo='ADMINISTRADOR'",datos)
        rs1=cur.fetchone()

        if rs1:

            Ventana=PA.Principal(self)
            Ventana.Show()
            self.Hide()
        else:
            cur.execute("Select * from Usuarios Where Nombre=? and Clave=? and Tipo='SECRETARIA'",datos)
            rs2=cur.fetchone()
            if rs2:

                Ventana=PA.Principal(self)
                Ventana.Show()
                self.Hide()
            
            else:
                dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
                dlg.ShowModal()
                dlg.Destroy()


#<------Usuarios-------->
def Bloquear(frm):
    self=frm
    con,cur=conexion()
    U=frm.txtNombre.GetValue()
    Usu=U.upper()
    dato=Usu
    
    cur.execute("Select Estado from Usuarios where Nombre=:dato",{"dato":dato})
    
    rs=cur.fetchone() 
    N=int(rs[0])
    if N ==1:
        wx.MessageBox('Error, El usuario ya estaba bloqueado', 'Caja de mensaje')
    else:
        cur.execute("Update  Usuarios set Estado= 1 where Nombre=:dato",{"dato":dato})
        wx.MessageBox('Usuario Bloqueado Satisfactoriamente', 'Caja de mensaje')
        con.commit()

        self.txtNombre.Clear()
        self.txtClave.Clear()
        self.cobTipo.Clear()

def Desbloquear(frm):
    self=frm
    con,cur=conexion()
    U=frm.txtNombre.GetValue()
    Usu=U.upper()
    dato=Usu
    cur.execute("Select Estado from Usuarios where Nombre=:dato",{"dato":dato})
    rs=cur.fetchone()
    N=int(rs[0])
    if N ==0:
        wx.MessageBox('Error, El usuario no esta bloqueado', 'Caja de mensaje')
    else:
        cur.execute("Update  Usuarios set Estado= 0 where Nombre=:dato",{"dato":dato})
        wx.MessageBox('Usuario Desbloqueado Satisfactoriamente', 'Caja de mensaje')
        con.commit()

        self.txtNombre.Clear()
        self.txtClave.Clear()
        self.cobTipo.Clear()


def GuardarUsuario(frm):
    No=frm.txtNombre.GetValue()
    Nom=No.upper()
    dato=Nom
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Guardar Usuario"
    Cl=hashlib.md5(frm.txtClave.GetValue())
    Cla=Cl.hexdigest()
    Ti=frm.cobTipo.GetValue()
    Es=0

    datos1=(Nom,Cla,Ti,Es)
    self=frm
    con, cur=conexion()
    # Saber si es menor de 8 caracteres
    if len(Cla)< 8:
        dlg=wx.MessageDialog(self,'La clave debe ser mayor a 8 caracteres', 'Atencion', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        self.txtClave.Clear()
        self.txtClave.SetFocus()
    else:#isdigit solo numeros isalpha solo letras.... comparacion alfanumerica
        if Cla.isdigit()or Cla.isalpha() : #isdigit puros numeros, isalpha puras letras
            dlg=wx.MessageDialog(self,'La Clave Debe Contener Datos Alfanumericos', 'Atencion', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
            self.txtClave.Clear()
            self.txtClave.SetFocus()
        
        else:
            cur.execute("Select Nombre from Usuarios where Nombre=:dato",{"dato":dato})
    
            rs=cur.fetchone() 
            
            if rs:
                wx.MessageBox('Error, El usuario ya esta Registrado ', 'Caja de mensaje')
            else:       
                cur.execute('INSERT INTO Usuarios (Nombre,Clave,Tipo, Estado) VALUES (?,?,?,?)',(datos1))
                wx.MessageBox('Guardado Satisfactoriamente', 'Caja de mensaje')
                con.commit()
            
                cur.execute("Select min(Usuario) from Bitacora")
                rs2=cur.fetchone()
                if rs2:
        
                    N=(str(rs2[0]))
                    cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Nom,Hora,Op))
                    con.commit()
                
                    
                    
                        
                    self.Hide()
                        
                
                self.txtNombre.Clear()
                self.txtClave.Clear()
                #self.cobTipo.Clear()
                self.txtNombre.SetFocus()
            
                cur.close()
                con.close()

def BuscarU(frm):
    con,cur=conexion()
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Buscar Usuario"
    dato1=frm.txtNombre.GetValue()
    dato=dato1.upper()
    cur.execute("Select * from Usuarios where Nombre=:dato",{"dato":dato})
    
    rs=cur.fetchone()
    self=frm
    if rs:
        self.txtNombre.SetValue(str(rs[0]))
        self.txtClave.SetValue(str(rs[1]))
        self.cobTipo.SetValue(str(rs[2]))
        cur.execute("Select min(Usuario) from Bitacora")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,dato1,Hora,Op))
            con.commit()
    else:
        dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

def ModificarUsuario(frm):
    self=frm
    No=frm.txtNombre.GetValue()

    Cla=frm.txtClave.GetValue()
    Ti=frm.cobTipo.GetValue()
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Modificar Usuario"
    con,cur=conexion()

    cur.execute('UPDATE Usuarios Set  Clave=?, Tipo=? WHERE Nombre=?',(Cla,Ti,No))
    wx.MessageBox('Modificado Satisfactoriamente', 'Caja de mensaje')
    con.commit()
    cur.execute("Select min(Usuario) from Bitacora")
    rs2=cur.fetchone()
    if rs2:

        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,No,Hora,Op))
        con.commit()
    self.txtNombre.Clear()
    self.txtClave.Clear()
    self.cobTipo.Clear()
    cur.close()
    con.close()
    return

#No eliminar Usuario a peticion del profesor.
def EliminarUsuario(frm):
    self=frm
    dato=frm.txtNombre.GetValue()
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Eliminar Usuario"
    con,cur=conexion()

    cur.execute("Delete from Usuarios where Nombre=:dato",{"dato":dato})
    wx.MessageBox('Eliminado Satisfactoriamente', 'Caja de mensaje')
    con.commit()
    self.txtNombre.Clear()
    self.txtClave.Clear()
    self.cobTipo.Clear()
    cur.execute("Select min(Usuario) from Bitacora")
    rs2=cur.fetchone()
    if rs2:
        
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,dato,Hora,Op))
        con.commit()  
    cur.close()
    con.close()
    return
        
#<-----Postulante------->

def GuardarPostulante(frm):
    self=frm
    No = frm.txtNombre.GetValue()
    Nom=No.upper()
    Ap= frm.txtApellidos.GetValue()
    Ape= Ap.upper()
    Ce= frm.txtCedula.GetValue()
    Se=frm.CobSexo.GetValue()
    Es=frm.cobEstado.GetValue()
    Est= Es.upper()
    Mu=frm.cobMunicipio.GetValue()
    Mun=Mu.upper()
    Pa=frm.cobParroquia.GetValue()
    Par=Pa.upper()
    Di=frm.txtDireccion.GetValue()
    Dir=Di.upper()
    
    Ed=frm.cobEducacion.GetValue()
    Ti=frm.txtTitulo.GetValue()
    Id=frm.cobIdioma.GetValue()
    AG=frm.txtAnoG.GetValue()
    Me=frm.txtMerito.GetValue()
    Off=frm.cobOffice.GetValue()
    Con=frm.cobContabilidad.GetValue()
    MI="militar"
    PAU="auxilio"

    Educacion=(Ed,Ti,Id,AG,Me,Off,Con,MI,PAU,Ce)

    Sa=frm.cobSalario.GetValue()
    Emp=frm.txtEmpresaT.GetValue()
    AT=frm.cobAtrabajo.GetValue()
    Car=frm.cobCargo.GetValue()
    Experiencia=(Sa,Emp,AT,Car,Ce)

    

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Guardar Postulante"
    
    
    con, cur = conexion()
    dato=frm.txtCedula.GetValue()
    #datos=(Car,Sec)
    cur.execute("Select Variable from registro order by hora desc")
    rs3=cur.fetchone()
    if rs3:
        
        Ca=(str(rs3[0]))

    cur.execute("select Cedula from Postulante where Cedula=:dato",{"dato": dato})
    rs=cur.fetchone()
    if rs:
       wx.MessageBox('Cedula Repetida', 'Caja de mensaje') 
    else:
        
                
        cur.execute('INSERT INTO Postulante (Nombre,Apellido,Cedula,Sexo,Direccion,Fecha) VALUES (?,?,?,?,?,?)',(Nom,Ape,Ce,Se,Dir,Hora))
        cur.execute('INSERT INTO Educacion (NEducacion,Titulo,Idioma,AGraduacion,Merito,Office,Contabilidad,Militar,PAuxilio,Cedula) VALUES (?,?,?,?,?,?,?,?,?,?)',Educacion)
        cur.execute('INSERT INTO Experiencia (Vigente,EmpresaV,ATrabajo,Cargo,Cedula) VALUES (?,?,?,?,?)',Experiencia)
        cur.execute('INSERT INTO Estado (Nombre,Id) VALUES (?,?)',(Est,Ce))
        cur.execute('INSERT INTO Munic (Nombre,Id) VALUES (?,?)',(Mun,Ce))
        cur.execute('INSERT INTO Parroquia (Nombre,Id) VALUES (?,?)',(Par,Ce))
        cur.execute('INSERT INTO Examen (Cargo,Cedula) VALUES (?,?)',(Ca,Ce))
        wx.MessageBox('Guardado Satisfactoriamente', 'Caja de mensaje')       
        con.commit()        


        
        cur.execute("Select min(Usuario) from Bitacora")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Ce,Hora,Op))
            con.commit()

        
            

        if Ca=="ADMINISTRACION":
                Ventana=EA.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="ASISTENTE":
                Ventana=EAA.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="CAJERO":
                Ventana=ECA.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="CHOFER":
                Ventana=EC.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="VIGILANTE":
                Ventana=EV.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="GERENTE VENTAS":
                Ventana=ECV.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="ASISTENTE VENTAS":
                Ventana=ECV1.Principal(self)
                Ventana.Show()
                self.Hide()               
        if Ca=="SERVICIO AL CLIENTE":
                Ventana=ESC.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="RECURSOS HUMANOS":
                Ventana=ERH.Principal(self)
                Ventana.Show()
                self.Hide()
        

    self.txtNombre.Clear()
    self.txtApellidos.Clear()
    self.txtCedula.Clear()
        
    
    self.cobMunicipio.Clear()
    self.cobParroquia.Clear()
    self.txtDireccion.Clear()

    self.txtTitulo.Clear()
   
    self.txtNombre.SetFocus()        
    cur.close()
    con.close()
    return

def BuscarPostulantes(frm):
    con, cur = conexion()
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Buscar Postulante"
    dato= frm.txtCedula.GetValue()
    cur.execute("Select Postulante.Nombre,Postulante.Apellido, Postulante.Sexo,Postulante.Direccion,Postulante.Neducacion, Postulante.Especialidad, Postulante.Idioma, Postulante.Psalarial, Postulante.Vigente,Munic.Nombre,Parroquia.Nombre, Estado.Nombre, Examen.Cargo  from Postulante, Munic, Parroquia, Estado, Examen where Postulante.Cedula=Munic.Id and Munic.Id=Parroquia.Id and Parroquia.Id=Estado.Id and Postulante.Cedula=Examen.Cedula and Postulante.Cedula=:dato",{"dato": dato})
    rs = cur.fetchone()
    self=frm
    if rs:
        
        self.txtNombre.SetValue(str(rs[0]))
        self.txtApellidos.SetValue(str(rs[1]))
        #self.txtCedula.SetValue(int(rs[2]))
        self.CobSexo.SetValue(str(rs[2]))
        self.txtDireccion.SetValue(str(rs[3]))
        self.cobEducacion.SetValue(str(rs[4]))
        self.txtTitulo.SetValue(str(rs[5]))
        self.cobIdioma.SetValue(str(rs[6]))
        self.cobSalario.SetValue(str(rs[7]))
        self.cobVigente.SetValue(str(rs[8]))
        self.cobMunicipio.SetValue(str(rs[9]))
        self.cobParroquia.SetValue(str(rs[10]))
        self.cobEstado.SetValue(str(rs[11]))
        self.cobCargo.SetValue(str(rs[12]))
        self.txtNombre.SetFocus()

        self.txtNombre.Enable(True)
        self.txtApellidos.Enable(True)
        self.CobSexo.Enable(True)
        self.txtDireccion.Enable(True)
        self.cobEducacion.Enable(True)
        self.txtTitulo.Enable(True)
        self.cobIdioma.Enable(True)
        self.cobSalario.Enable(True)
        self.cobVigente.Enable(True)
        self.cobMunicipio.Enable(True)
        self.cobParroquia.Enable(True)
        self.cobEstado.Enable(True)
        self.cobCargo.Enable(True)

        
    else:
        dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

def ModificarPostulante(frm):
    
    self=frm
    No = frm.txtNombre.GetValue()
    Nom=No.upper()
    Ap= frm.txtApellidos.GetValue()
    Ape= Ap.upper()
    Ce= frm.txtCedula.GetValue()
    Se=frm.CobSexo.GetValue()
    Es=frm.cobEstado.GetValue()
    Est= Es.upper()
    Mu=frm.cobMunicipio.GetValue()
    Mun=Mu.upper()
    Pa=frm.cobParroquia.GetValue()
    Par=Pa.upper()
    Di=frm.txtDireccion.GetValue()
    Dir=Di.upper()
    
    Ed=frm.cobEducacion.GetValue()
    Es=frm.txtTitulo.GetValue()
    Id=frm.cobIdioma.GetValue()

    Sa=frm.cobSalario.GetValue()
    Vi=frm.cobVigente.GetValue()
    Ca=frm.cobCargo.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Modificar Postulante"
    
   
    
    con, cur = conexion()
    

    cur.execute('UPDATE Postulante Set Nombre=?, Apellido=?, Sexo=?, Direccion=?, Neducacion=?, Especialidad=?,Idioma=?, Psalarial=?,Vigente=?,Fecha=? WHERE Cedula=?',(Nom,Ape,Se,Dir,Ed,Es,Id,Sa,Vi,Hora,Ce))
    cur.execute('UPDATE Estado Set Nombre=? WHERE Id=?',(Est,Ce))
    cur.execute('UPDATE Munic Set Nombre=? WHERE Id=?',(Mun,Ce))
    cur.execute('UPDATE Parroquia Set Nombre=? WHERE Id=?',(Par,Ce))
    cur.execute('UPDATE Examen Set Cargo=? WHERE Id=?',(Ca,Ce))
    

    wx.MessageBox('Modificado Satisfactoriamente', 'Caja de mensaje')
    con.commit()

    cur.execute("Select min(Usuario) from Bitacora")
    rs2=cur.fetchone()
    if rs2:
        
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Ce,Hora,Op))
        con.commit()
    
    cur.close()
    con.close()
    return




# Examenes
#Cargar datos
def CargarDatos(frm):
    con, cur = conexion()   

    cur.execute("select max(variable),fecha,hora from registro where Operacion='Buscar Examen' order by fecha asc" )
    rs = cur.fetchone()
    self=frm
    if rs:
        dato=(str(rs[0]))
        cur.execute("Select * from Examen where Cedula=:dato",{"dato": dato})
        rs1 = cur.fetchone()
        if rs1:
            #Empieza en 1 xq 0 es el ID
            self.cobExperiencia.SetValue(str(rs1[1]))
            self.cobGTrabajo.SetValue(str(rs1[2]))
            self.cobTFuera.SetValue(str(rs1[3]))
            self.cobLicencia.SetValue(str(rs1[4]))
            self.cobTransporte.SetValue(str(rs1[5]))
            self.cobMecanica.SetValue(str(rs1[6]))
            self.cobHoras.SetValue(str(rs1[7]))
            self.cobNormas.SetValue(str(rs1[8]))
            self.cobNormasS.SetValue(str(rs1[9]))
            self.cobAccidente.SetValue(str(rs1[10]))      

        
    else:
        dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

#Buscar Examenes
def BuscarExamen(frm):

    con, cur = conexion()
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Buscar Examen"
    Ce= frm.txtCedula.GetValue()

    cur.execute("Select min(Usuario) from Bitacora")
    rs2=cur.fetchone()
    if rs2:
        
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Ce,Hora,Op))
        con.commit()

    cur.execute("Select Cargo from Examen where Cedula=:Ce",{"Ce": Ce})
    rs = cur.fetchone()
    self=frm
    if rs:
        Campo=(str(rs[0]))

        if Campo=="ADMINISTRACION": 
            Ventana=EAM.Principal(self)
            Ventana.Show()            
            self.Hide()
        if Campo=="ASISTENTE": 
            Ventana=EAAM.Principal(self)
            Ventana.Show()            
            self.Hide()
        if Campo=="CAJERO": 
            Ventana=ECAM.Principal(self)
            Ventana.Show()            
            self.Hide()
        if Campo=="CHOFER": 
            Ventana=ECM.Principal(self)
            Ventana.Show()            
            self.Hide()
        if Campo=="VIGILANTE": 
            Ventana=EVM.Principal(self)
            Ventana.Show()            
            self.Hide()
        if Campo=="GERENTE VENTAS": 
            Ventana=ECVM.Principal(self)
            Ventana.Show()            
            self.Hide()
        if Campo=="ASISTENTE VENTAS": 
            Ventana=ECV1M.Principal(self)
            Ventana.Show()            
            self.Hide()
        if Campo=="SERVICIO AL CLIENTE": 
            Ventana=ESCM.Principal(self)
            Ventana.Show()            
            self.Hide()
        if Campo=="RECURSOS HUMANOS": 
            Ventana=ERHM.Principal(self)
            Ventana.Show()

                
       
            
            self.Hide() 

        
    else:
        dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
#Chofer

def GuardarChofer(frm):
    self=frm
    puntaje=0
    #Años de Experiencia=P1
    AE=frm.cobExperiencia.GetValue()
    #Se integra facilmente a grupos de trabajo=P2
    GT=frm.cobGTrabajo.GetValue()
    #Tendria incoveniente en trabajar fuera de la ciudad=P3
    TF=frm.cobTFuera.GetValue()
    #Que tipo de licencia posee=P4
    LI=frm.cobLicencia.GetValue()
    #Que tipo de Transporte ha manejado=P5
    TA=frm.cobTransporte.GetValue()
    #Posee conocimientos en mecanica basica=P6
    ME=frm.cobMecanica.GetValue()
    #Esta dispuesto a trabajas horas extras=P7
    HE=frm.cobHoras.GetValue()
    #Acepta las normas de la empresa=P8
    NE=frm.cobNormas.GetValue()
    #Acepta las normas de sus superores=P9
    NS=frm.cobNormasS.GetValue()
    #Ha tenido accidentes de transito=P10
    AC=frm.cobAccidente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Postulante Chofer"
    
    dato="CHOFER"
    con, cur = conexion()
    
    cur.execute("Select max(id) from Examen")
    rs2=cur.fetchone()
    if rs2:
        Id=(str(rs2[0])) 
                
        

        cur.execute("select * from Respuestas where Cargo=:dato",{"dato": dato})
        rs3=cur.fetchone()
        if rs3:
            lista1=[AE,GT,TF,LI,TA,ME,HE,NE,NS,AC]
            lista2=[str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4]),str(rs3[5]),str(rs3[6]),str(rs3[7]),str(rs3[8]),str(rs3[9]),str(rs3[10]),]
            puntaje=0
            pu=str(0)

            for i in lista1:
                if i in lista2:
                    puntaje=puntaje+10
        

            pp=str(puntaje)
            cur.execute('UPDATE Examen Set  P1=?,P2=?,P3=?,P4=?,P5=?,P6=?,P7=?,P8=?,P9=?,P10=?,Puntuacion=? WHERE Id=?',(AE,GT,TF,LI,TA,ME,HE,NE,NS,AC,pp,Id))
            
            
            dlg=wx.MessageDialog(self,'Datos Guardados\n'+
            'Su puntuacion fue de: '+pp+'%\n'+
            'Su Numero de Registro es:'+Id
            , 'Atencion', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
                    
                    
                 
        

        
        cur.execute("Select min(Usuario) from Bitacora")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Id,Hora,Op))
            con.commit()

          
    cur.close()
    con.close()


#Administacion

def GuardarAdministrador(frm):
    self=frm
    puntaje=0
    #Años de Experiencia=P1
    AE=frm.cobExperiencia.GetValue()
    #Se integra facilmente a grupos de trabajo=P2
    GT=frm.cobGTrabajo.GetValue()
    #Tendria incoveniente en trabajar fuera de la ciudad=P3
    TF=frm.cobTFuera.GetValue()
    #Que tipo de licencia posee=P4
    LI=frm.cobLicencia.GetValue()
    #Que tipo de Transporte ha manejado=P5
    TA=frm.cobTransporte.GetValue()
    #Posee conocimientos en mecanica basica=P6
    ME=frm.cobMecanica.GetValue()
    #Esta dispuesto a trabajas horas extras=P7
    HE=frm.cobHoras.GetValue()
    #Acepta las normas de la empresa=P8
    NE=frm.cobNormas.GetValue()
    #Acepta las normas de sus superores=P9
    NS=frm.cobNormasS.GetValue()
    #Ha tenido accidentes de transito=P10
    AC=frm.cobAccidente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Postulante Administracion"
    
    dato="ADMINISTRACION"
    con, cur = conexion()
    
    cur.execute("Select max(id) from Examen")
    rs2=cur.fetchone()
    if rs2:
        Id=(str(rs2[0])) 
                
        

        cur.execute("select * from Respuestas where Cargo=:dato",{"dato": dato})
        rs3=cur.fetchone()
        if rs3:
            lista1=[AE,GT,TF,LI,TA,ME,HE,NE,NS,AC]
            lista2=[str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4]),str(rs3[5]),str(rs3[6]),str(rs3[7]),str(rs3[8]),str(rs3[9]),str(rs3[10]),]
            puntaje=0
            pu=str(0)

            for i in lista1:
                if i in lista2:
                    puntaje=puntaje+10
        

            pp=str(puntaje)
            cur.execute('UPDATE Examen Set  P1=?,P2=?,P3=?,P4=?,P5=?,P6=?,P7=?,P8=?,P9=?,P10=?,Puntuacion=? WHERE Id=?',(AE,GT,TF,LI,TA,ME,HE,NE,NS,AC,pp,Id))
            
            cur.execute("select * from Examen where cargo="ADMINISTRACION" order by puntuacion desc")
            rs4=[r[0] for r in cur.fetchall()]
            
            dlg=wx.MessageDialog(self,'Datos Guardados\n'+
            'Su puntuacion fue de: '+pp+'%\n'+
            'Su Numero de Registro es:'+Id
            , 'Atencion', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
                    
                    
                 
        

        
        cur.execute("Select min(Usuario) from Bitacora")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Id,Hora,Op))
            con.commit()

          
    cur.close()
    con.close()

#Asistente Administrativo

def GuardarAsistenteA(frm):
    self=frm
    puntaje=0
    #Años de Experiencia=P1
    AE=frm.cobExperiencia.GetValue()
    #Se integra facilmente a grupos de trabajo=P2
    GT=frm.cobGTrabajo.GetValue()
    #Tendria incoveniente en trabajar fuera de la ciudad=P3
    TF=frm.cobTFuera.GetValue()
    #Que tipo de licencia posee=P4
    LI=frm.cobLicencia.GetValue()
    #Que tipo de Transporte ha manejado=P5
    TA=frm.cobTransporte.GetValue()
    #Posee conocimientos en mecanica basica=P6
    ME=frm.cobMecanica.GetValue()
    #Esta dispuesto a trabajas horas extras=P7
    HE=frm.cobHoras.GetValue()
    #Acepta las normas de la empresa=P8
    NE=frm.cobNormas.GetValue()
    #Acepta las normas de sus superores=P9
    NS=frm.cobNormasS.GetValue()
    #Ha tenido accidentes de transito=P10
    AC=frm.cobAccidente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Postulante Asistente Administrativo"
    
    dato="ASISTENTE"
    con, cur = conexion()
    
    cur.execute("Select max(id) from Examen")
    rs2=cur.fetchone()
    if rs2:
        Id=(str(rs2[0])) 
                
        

        cur.execute("select * from Respuestas where Cargo=:dato",{"dato": dato})
        rs3=cur.fetchone()
        if rs3:
            lista1=[AE,GT,TF,LI,TA,ME,HE,NE,NS,AC]
            lista2=[str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4]),str(rs3[5]),str(rs3[6]),str(rs3[7]),str(rs3[8]),str(rs3[9]),str(rs3[10]),]
            puntaje=0
            pu=str(0)

            for i in lista1:
                if i in lista2:
                    puntaje=puntaje+10
        

            pp=str(puntaje)
            cur.execute('UPDATE Examen Set  P1=?,P2=?,P3=?,P4=?,P5=?,P6=?,P7=?,P8=?,P9=?,P10=?,Puntuacion=? WHERE Id=?',(AE,GT,TF,LI,TA,ME,HE,NE,NS,AC,pp,Id))
            
            
            dlg=wx.MessageDialog(self,'Datos Guardados\n'+
            'Su puntuacion fue de: '+pp+'%\n'+
            'Su Numero de Registro es:'+Id
            , 'Atencion', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
                    
                    
                 
        

        
        cur.execute("Select min(Usuario) from Bitacora")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Id,Hora,Op))
            con.commit()

          
    cur.close()
    con.close()

#Cajero

def GuardarCajero(frm):
    self=frm
    puntaje=0
    #¿Por qué quiere trabajar con nosotros?
    AE=frm.cobExperiencia.GetValue()
    #¿tiene experiencia en esta área de trabajo?
    GT=frm.cobGTrabajo.GetValue()
    #¿Ha vivido algún conflicto en su último trabajo?
    TF=frm.cobTFuera.GetValue()
    #¿Por qué dejo su último trabajo?
    LI=frm.cobLicencia.GetValue()
    #Que tipo de Transporte ha manejado=P5
    TA=frm.cobTransporte.GetValue()
    #Posee conocimientos en mecanica basica=P6
    ME=frm.cobMecanica.GetValue()
    #Esta dispuesto a trabajas horas extras=P7
    HE=frm.cobHoras.GetValue()
    #Acepta las normas de la empresa=P8
    NE=frm.cobNormas.GetValue()
    #Acepta las normas de sus superores=P9
    NS=frm.cobNormasS.GetValue()
    #Ha tenido accidentes de transito=P10
    AC=frm.cobAccidente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Postulante Cajero"
    
    dato="CAJERO"
    con, cur = conexion()
    
    cur.execute("Select max(id) from Examen")
    rs2=cur.fetchone()
    if rs2:
        Id=(str(rs2[0])) 
                
        

        cur.execute("select * from Respuestas where Cargo=:dato",{"dato": dato})
        rs3=cur.fetchone()
        if rs3:
            lista1=[AE,GT,TF,LI,TA,ME,HE,NE,NS,AC]
            lista2=[str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4]),str(rs3[5]),str(rs3[6]),str(rs3[7]),str(rs3[8]),str(rs3[9]),str(rs3[10]),]
            puntaje=0
            pu=str(0)

            for i in lista1:
                if i in lista2:
                    puntaje=puntaje+10
        

            pp=str(puntaje)
            cur.execute('UPDATE Examen Set  P1=?,P2=?,P3=?,P4=?,P5=?,P6=?,P7=?,P8=?,P9=?,P10=?,Puntuacion=? WHERE Id=?',(AE,GT,TF,LI,TA,ME,HE,NE,NS,AC,pp,Id))
            
            dlg=wx.MessageDialog(self,'Datos Guardados\n'+
            'Su puntuacion fue de: '+pp+'%\n'+
            'Su Numero de Registro es:'+Id
            , 'Atencion', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
                    
                    
                 
        

        
        cur.execute("Select min(Usuario) from Bitacora")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Id,Hora,Op))
            con.commit()

          
    cur.close()
    con.close()


#Servicio al Cliente

def GuardarServicioC(frm):
    self=frm
    puntaje=0
    #Años de Experiencia=P1
    AE=frm.cobExperiencia.GetValue()
    #Se integra facilmente a grupos de trabajo=P2
    GT=frm.cobGTrabajo.GetValue()
    #Tendria incoveniente en trabajar fuera de la ciudad=P3
    TF=frm.cobTFuera.GetValue()
    #Que tipo de licencia posee=P4
    LI=frm.cobLicencia.GetValue()
    #Que tipo de Transporte ha manejado=P5
    TA=frm.cobTransporte.GetValue()
    #Posee conocimientos en mecanica basica=P6
    ME=frm.cobMecanica.GetValue()
    #Esta dispuesto a trabajas horas extras=P7
    HE=frm.cobHoras.GetValue()
    #Acepta las normas de la empresa=P8
    NE=frm.cobNormas.GetValue()
    #Acepta las normas de sus superores=P9
    NS=frm.cobNormasS.GetValue()
    #Ha tenido accidentes de transito=P10
    AC=frm.cobAccidente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Postulante Servicio al Cliente"
    
    dato="SERVICIO AL CLIENTE"
    con, cur = conexion()
    
    cur.execute("Select max(id) from Examen")
    rs2=cur.fetchone()
    if rs2:
        Id=(str(rs2[0])) 
                
        

        cur.execute("select * from Respuestas where Cargo=:dato",{"dato": dato})
        rs3=cur.fetchone()
        if rs3:
            lista1=[AE,GT,TF,LI,TA,ME,HE,NE,NS,AC]
            lista2=[str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4]),str(rs3[5]),str(rs3[6]),str(rs3[7]),str(rs3[8]),str(rs3[9]),str(rs3[10]),]
            puntaje=0
            pu=str(0)

            for i in lista1:
                if i in lista2:
                    puntaje=puntaje+10
        

            pp=str(puntaje)
            cur.execute('UPDATE Examen Set  P1=?,P2=?,P3=?,P4=?,P5=?,P6=?,P7=?,P8=?,P9=?,P10=?,Puntuacion=? WHERE Id=?',(AE,GT,TF,LI,TA,ME,HE,NE,NS,AC,pp,Id))
            
            
            dlg=wx.MessageDialog(self,'Datos Guardados\n'+
            'Su puntuacion fue de: '+pp+'%\n'+
            'Su Numero de Registro es:'+Id
            , 'Atencion', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
                    
                 
        

        
        cur.execute("Select min(Usuario) from Bitacora")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Id,Hora,Op))
            con.commit()

          
    cur.close()
    con.close()


#Vigilante

def GuardarVigilante(frm):
    self=frm
    puntaje=0
    #Años de Experiencia=P1
    AE=frm.cobExperiencia.GetValue()
    #Se integra facilmente a grupos de trabajo=P2
    GT=frm.cobGTrabajo.GetValue()
    #Tendria incoveniente en trabajar fuera de la ciudad=P3
    TF=frm.cobTFuera.GetValue()
    #Que tipo de licencia posee=P4
    LI=frm.cobLicencia.GetValue()
    #Que tipo de Transporte ha manejado=P5
    TA=frm.cobTransporte.GetValue()
    #Posee conocimientos en mecanica basica=P6
    ME=frm.cobMecanica.GetValue()
    #Esta dispuesto a trabajas horas extras=P7
    HE=frm.cobHoras.GetValue()
    #Acepta las normas de la empresa=P8
    NE=frm.cobNormas.GetValue()
    #Acepta las normas de sus superores=P9
    NS=frm.cobNormasS.GetValue()
    #Ha tenido accidentes de transito=P10
    AC=frm.cobAccidente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Postulante Vigilante"
    
    dato="VIGILANTE"
    con, cur = conexion()
    
    cur.execute("Select max(id) from Examen")
    rs2=cur.fetchone()
    if rs2:
        Id=(str(rs2[0])) 
                
        

        cur.execute("select * from Respuestas where Cargo=:dato",{"dato": dato})
        rs3=cur.fetchone()
        if rs3:
            lista1=[AE,GT,TF,LI,TA,ME,HE,NE,NS,AC]
            lista2=[str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4]),str(rs3[5]),str(rs3[6]),str(rs3[7]),str(rs3[8]),str(rs3[9]),str(rs3[10]),]
            puntaje=0
            pu=str(0)

            for i in lista1:
                if i in lista2:
                    puntaje=puntaje+10
        

            pp=str(puntaje)
            cur.execute('UPDATE Examen Set  P1=?,P2=?,P3=?,P4=?,P5=?,P6=?,P7=?,P8=?,P9=?,P10=?,Puntuacion=? WHERE Id=?',(AE,GT,TF,LI,TA,ME,HE,NE,NS,AC,pp,Id))
            
            
            dlg=wx.MessageDialog(self,'Datos Guardados\n'+
            'Su puntuacion fue de: '+pp+'%\n'+
            'Su Numero de Registro es:'+Id
            , 'Atencion', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
                    
                 
        

        
        cur.execute("Select min(Usuario) from Bitacora")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Id,Hora,Op))
            con.commit()

          
    cur.close()
    con.close()

#Recursos Humanos

def GuardarRecursosH(frm):
    self=frm
    puntaje=0
    #¿Por qué quiere trabajar con nosotros?
    AE=frm.cobExperiencia.GetValue()
    #¿tiene experiencia en esta área de trabajo?
    GT=frm.cobGTrabajo.GetValue()
    #¿Ha vivido algún conflicto en su último trabajo?
    TF=frm.cobTFuera.GetValue()
    #¿Por qué dejo su último trabajo?
    LI=frm.cobLicencia.GetValue()
    #Que tipo de Transporte ha manejado=P5
    TA=frm.cobTransporte.GetValue()
    #Posee conocimientos en mecanica basica=P6
    ME=frm.cobMecanica.GetValue()
    #Esta dispuesto a trabajas horas extras=P7
    HE=frm.cobHoras.GetValue()
    #Acepta las normas de la empresa=P8
    NE=frm.cobNormas.GetValue()
    #Acepta las normas de sus superores=P9
    NS=frm.cobNormasS.GetValue()
    #Ha tenido accidentes de transito=P10
    AC=frm.cobAccidente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Postulante Recursos Humanos"
    
    dato="RECURSOS HUMANOS"
    con, cur = conexion()
    
    cur.execute("Select max(id) from Examen")
    rs2=cur.fetchone()
    if rs2:
        Id=(str(rs2[0])) 
                
        

        cur.execute("select * from Respuestas where Cargo=:dato",{"dato": dato})
        rs3=cur.fetchone()
        if rs3:
            lista1=[AE,GT,TF,LI,TA,ME,HE,NE,NS,AC]
            lista2=[str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4]),str(rs3[5]),str(rs3[6]),str(rs3[7]),str(rs3[8]),str(rs3[9]),str(rs3[10]),]
            puntaje=0
            pu=str(0)

            for i in lista1:
                if i in lista2:
                    puntaje=puntaje+10
        

            pp=str(puntaje)
            cur.execute('UPDATE Examen Set  P1=?,P2=?,P3=?,P4=?,P5=?,P6=?,P7=?,P8=?,P9=?,P10=?,Puntuacion=? WHERE Id=?',(AE,GT,TF,LI,TA,ME,HE,NE,NS,AC,pp,Id))
            
            dlg=wx.MessageDialog(self,'Datos Guardados\n'+
            'Su puntuacion fue de: '+pp+'%\n'+
            'Su Numero de Registro es:'+Id
            , 'Atencion', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
                    
                    
                 
        

        
        cur.execute("Select min(Usuario) from Bitacora")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Id,Hora,Op))
            con.commit()

          
    cur.close()
    con.close()

#Gerente Ventas

def GuardarGVentas(frm):
    self=frm
    puntaje=0
    #Años de Experiencia=P1
    AE=frm.cobExperiencia.GetValue()
    #Se integra facilmente a grupos de trabajo=P2
    GT=frm.cobGTrabajo.GetValue()
    #Tendria incoveniente en trabajar fuera de la ciudad=P3
    TF=frm.cobTFuera.GetValue()
    #Que tipo de licencia posee=P4
    LI=frm.cobLicencia.GetValue()
    #Que tipo de Transporte ha manejado=P5
    TA=frm.cobTransporte.GetValue()
    #Posee conocimientos en mecanica basica=P6
    ME=frm.cobMecanica.GetValue()
    #Esta dispuesto a trabajas horas extras=P7
    HE=frm.cobHoras.GetValue()
    #Acepta las normas de la empresa=P8
    NE=frm.cobNormas.GetValue()
    #Acepta las normas de sus superores=P9
    NS=frm.cobNormasS.GetValue()
    #Ha tenido accidentes de transito=P10
    AC=frm.cobAccidente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Postulante Compra y Venta"
    
    dato="GERENTE VENTAS"
    con, cur = conexion()
    
    cur.execute("Select max(id) from Examen")
    rs2=cur.fetchone()
    if rs2:
        Id=(str(rs2[0])) 
                
        

        cur.execute("select * from Respuestas where Cargo=:dato",{"dato": dato})
        rs3=cur.fetchone()
        if rs3:
            lista1=[AE,GT,TF,LI,TA,ME,HE,NE,NS,AC]
            lista2=[str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4]),str(rs3[5]),str(rs3[6]),str(rs3[7]),str(rs3[8]),str(rs3[9]),str(rs3[10]),]
            puntaje=0
            pu=str(0)

            for i in lista1:
                if i in lista2:
                    puntaje=puntaje+10
        

            pp=str(puntaje)
            cur.execute('UPDATE Examen Set  P1=?,P2=?,P3=?,P4=?,P5=?,P6=?,P7=?,P8=?,P9=?,P10=?,Puntuacion=? WHERE Id=?',(AE,GT,TF,LI,TA,ME,HE,NE,NS,AC,pp,Id))
            
            
            dlg=wx.MessageDialog(self,'Datos Guardados\n'+
            'Su puntuacion fue de: '+pp+'%\n'+
            'Su Numero de Registro es:'+Id
            , 'Atencion', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
                    
                    
                 
        

        
        cur.execute("Select min(Usuario) from Bitacora")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Id,Hora,Op))
            con.commit()

          
    cur.close()
    con.close()

#Asistente Ventas

def GuardarAVentas(frm):
    self=frm
    puntaje=0
    #Años de Experiencia=P1
    AE=frm.cobExperiencia.GetValue()
    #Se integra facilmente a grupos de trabajo=P2
    GT=frm.cobGTrabajo.GetValue()
    #Tendria incoveniente en trabajar fuera de la ciudad=P3
    TF=frm.cobTFuera.GetValue()
    #Que tipo de licencia posee=P4
    LI=frm.cobLicencia.GetValue()
    #Que tipo de Transporte ha manejado=P5
    TA=frm.cobTransporte.GetValue()
    #Posee conocimientos en mecanica basica=P6
    ME=frm.cobMecanica.GetValue()
    #Esta dispuesto a trabajas horas extras=P7
    HE=frm.cobHoras.GetValue()
    #Acepta las normas de la empresa=P8
    NE=frm.cobNormas.GetValue()
    #Acepta las normas de sus superores=P9
    NS=frm.cobNormasS.GetValue()
    #Ha tenido accidentes de transito=P10
    AC=frm.cobAccidente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Postulante Compra y Venta"
    
    dato="ASISTENTE VENTAS"
    con, cur = conexion()
    
    cur.execute("Select max(id) from Examen")
    rs2=cur.fetchone()
    if rs2:
        Id=(str(rs2[0])) 
                
        

        cur.execute("select * from Respuestas where Cargo=:dato",{"dato": dato})
        rs3=cur.fetchone()
        if rs3:
            lista1=[AE,GT,TF,LI,TA,ME,HE,NE,NS,AC]
            lista2=[str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4]),str(rs3[5]),str(rs3[6]),str(rs3[7]),str(rs3[8]),str(rs3[9]),str(rs3[10]),]
            puntaje=0
            pu=str(0)

            for i in lista1:
                if i in lista2:
                    puntaje=puntaje+10
        

            pp=str(puntaje)
            cur.execute('UPDATE Examen Set  P1=?,P2=?,P3=?,P4=?,P5=?,P6=?,P7=?,P8=?,P9=?,P10=?,Puntuacion=? WHERE Id=?',(AE,GT,TF,LI,TA,ME,HE,NE,NS,AC,pp,Id))
            
            
            dlg=wx.MessageDialog(self,'Datos Guardados\n'+
            'Su puntuacion fue de: '+pp+'%\n'+
            'Su Numero de Registro es:'+Id
            , 'Atencion', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
                    
                    
                 
        

        
        cur.execute("Select min(Usuario) from Bitacora")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Id,Hora,Op))
            con.commit()

          
    cur.close()
    con.close()






#Direcciones
def BuscarM(frm):
    
    dato=frm.cobEstado.GetValue()
    
   
    
    self=frm

    
    i=0
    
    Merida=["Alberto Adriani","Andres Bello","Antonio Pinto Salinas","Aricagua","Arzobispo Chacon","Campo Elias","Caracciolo Parra Olmedo","Cardenal Quintero","Guaraque","Julio Cesar","Justo Briceno","Libertador","Miranda","Obispo Ramos de Lora","Padre Noguera","Pueblo Llano","Rangel","Rivas Davila","Santos Marquina","Sucre","Tovar","Tulio Febres Cordero","Zea"]
    Sucre=["Bermudez","Sucre","Benitez","Cruz Salmeron Acosta","Bolivar","Arismendi","Ribero","Valdez","Montes","Mejia","Marino","Libertador","Andres Mata","Andres Eloy Blanco","Cajigal"]
    if dato=="Merida":
        self.cobMunicipio.Clear()
        while i <len(Merida):
            self.cobMunicipio.Append(Merida[i])
            i=i+1
    elif dato=="Sucre":
        self.cobMunicipio.Clear()
        while i <len(Sucre):
            self.cobMunicipio.Append(Sucre[i])
            i=i+1

def BuscarP(frm):
    
    dato=frm.cobMunicipio.GetValue()

    self=frm
    i=0
    #Listas de las Parroquias (problemas con el unicode)
    Bermudez=["Santa Catalina","Santa Rosa","Santa Teresa", "Bolivar", "Macarapana"]
    Sucre=["San Juan","Altagracia","Ayacucho","Gran Mariscal","Raul Leoni","Valentin Valiente"]
    Benitez=["El Pilar","El Rincon","General Francisco Antonio Vazquez","Guaraunos","Tunapuicito","Union"]
    Cruz_Salmeron_Acosta=["Cruz Salmeron Acosta", "Chacopata","Manicuare"]
    Bolivar=["Mariguitar"]
    Arismendi=["Antonio Jose de Sucre","El Morro de Puerto Santo","Puerto Santo","Rio Caribe","San Juan de las Galdonas"]
    Ribero=["Catuaro","Rendon","Santa Cruz","Santa Maria","Villa Frontado"]
    Valdez=["Bideau","Cristobal Colon","Guiria","Punta de Piedras"]
    Montes=["Arenas","Aricagua","Cocollar","Cumanacoa","San Fernando","San Lorenzo"]
    Mejia=["Mejia"]
    Marino=["Irapa","Campo Claro","Maraval","San Antonio de Irapa","Soro"]
    Libertador=["Tunapuy","Campo Elias"]
    Andres_Mata=["San Jose de Aerocuar","Tavera Acosta"]
    Andres_Eloy_Blanco=["Marino","Romulo Gallegos"]
    Cajigal=["Libertad","ElPaujil","Yaguaraparo"]
    
    if dato=="Bermudez":
        self.cobParroquia.Clear()
        while i<len(Bermudez):
            self.cobParroquia.Append(Bermudez[i])
            i=i+1
    if dato=="Sucre":
        self.cobParroquia.Clear()
        while i<len(Sucre):
            self.cobParroquia.Append(Sucre[i])
            i=i+1
    if dato=="Benitez":
        self.cobParroquia.Clear()
        while i<len(Benitez):
            self.cobParroquia.Append(Benitez[i])
            i=i+1
    if dato=="Cruz Salmeron Acosta":
        self.cobParroquia.Clear()
        while i<len(Cruz_Salmeron_Acosta):
            self.cobParroquia.Append(Cruz_Salmeron_Acosta[i])
            i=i+1
    if dato=="Bolivar":
        self.cobParroquia.Clear()
        while i<len(Bolivar):
            self.cobParroquia.Append(Bolivar[i])
            i=i+1
    if dato=="Arismendi":
        self.cobParroquia.Clear()
        while i<len(Arismendi):
            self.cobParroquia.Append(Arismendi[i])
            i=i+1
    if dato=="Ribero":
        self.cobParroquia.Clear()
        while i<len(Ribero):
            self.cobParroquia.Append(Ribero[i])
            i=i+1
    if dato=="Valdez":
        self.cobParroquia.Clear()
        while i<len(Valdez):
            self.cobParroquia.Append(Valdez[i])
            i=i+1
    if dato=="Montes":
        self.cobParroquia.Clear()
        while i<len(Montes):
            self.cobParroquia.Append(Montes[i])
            i=i+1
    if dato=="Mejia":
        self.cobParroquia.Clear()
        while i<len(Mejia):
            self.cobParroquia.Append(Mejia[i])
            i=i+1
    if dato=="Marino":
        self.cobParroquia.Clear()
        while i<len(Marino):
            self.cobParroquia.Append(Marino[i])
            i=i+1
    if dato=="Libertador":
        self.cobParroquia.Clear()
        while i<len(Libertador):
            self.cobParroquia.Append(Libertador[i])
            i=i+1
    if dato=="Andres Mata":
        self.cobParroquia.Clear()
        while i<len(Andres_Mata):
            self.cobParroquia.Append(Andres_Mata[i])
            i=i+1
    if dato=="Andres Eloy Blanco":
        self.cobParroquia.Clear()
        while i<len(Andres_Eloy_Blanco):
            self.cobParroquia.Append(Andres_Eloy_Blanco[i])
            i=i+1
    if dato=="Andres Mata":
        self.cobParroquia.Clear()
        while i<len(Andres_Mata):
            self.cobParroquia.Append(Andres_Mata[i])
            i=i+1



def ano():
    self.cobAno.Clear()
    i=0
    ano=time.strftime("%Y")
    ano1=int(ano)-101

    while ano1 < int(ano):
        ano1=ano1+1
        print ano1
