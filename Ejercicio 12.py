#Ejercicio 12
dia=int(input("Por favor, ingrese el dÃ­a de su nacimiento "))
mes=str(input("Por favor, ingrese su mes de nacimiento "))

if (dia>=21) and (dia<=31) and (mes=="marzo") or (mes=="Marzo") or (mes=="MARZO"):
    print("Usted es de Aries")
if (dia>=1) and (dia<=20) and (mes=="abril") or (mes=="Abril") or (mes=="ABRIL"):
    print("Usted es de Aries")
    
if (dia>=21) and (dia<=30) and (mes=="abril") or (mes=="Abril") or (mes=="ABRIL"):
    print("Usted es de Tauro")
if (dia>=1) and (dia<=20) and (mes=="mayo") or (mes=="Mayo") or (mes=="MAYO"):
    print("Usted es de Tauro")
    
if (dia>=21) and (dia<=31) and (mes=="mayo") or (mes=="Mayo") or (mes=="MAYO"):
    print("Usted es de Géminis")
if (dia>=1) and (dia<=21) and (mes=="junio") or (mes=="Junio") or (mes=="JUNIO"):
    print("Usted es de Géminis")
    
if (dia>=22) and (dia<=30) and (mes=="junio") or (mes=="Junio") or (mes=="JUNIO"):
    print("Usted es de Cáncer")
if (dia>=1) and (dia<=21) and (mes=="julio") or (mes=="Julio") or (mes=="JULIO"):
    print("Usted es de Cáncer")
    
if (dia>=22) and (dia<=31) and (mes=="julio") or (mes=="Julio") or (mes=="JULIO"):
    print("Usted es de Leo")
if (dia>=1) and (dia<=23) and (mes=="agosto") or (mes=="Agosto") or (mes=="AGOSTO"):
    print("Usted es de Leo")
    
if (dia>=24) and (dia<=31) and (mes=="agosto") or (mes=="Agosto") or (mes=="AGOSTO"):
    print("Usted es de Virgo")
if (dia>=1) and (dia<=23) and (mes=="setiembre") or (mes=="Setiembre") or (mes=="SETIEMBRE"):
    print("Usted es de Virgo")
    
if (dia>=24) and (dia<=30) and (mes=="setiembre") or (mes=="Setiembre") or (mes=="SETIEMBRE"):
    print("Usted es de Libra")
if (dia>=1) and (dia<=22) and (mes=="octubre") or (mes=="Octubre") or (mes=="OCTUBRE"):
    print("Usted es de Libra")
        
if (dia>=23) and (dia<=31) and (mes=="octubre") or (mes=="Octubre") or (mes=="OCTUBRE"):
    print("Usted es de Escorpio")
if (dia>=1) and (dia<=22) and (mes=="noviembre") or (mes=="Noviembre") or (mes=="NOVIEMBRE"):
   print("Usted es de Escorpio")
   
if (dia>=23) and (dia<=30) and (mes=="noviembre") or (mes=="Noviembre") or (mes=="NOVIEMBRE"):
    print("Usted es de Sagitario")
if (dia>=1) and (dia<=21) and (mes=="diciembre") or (mes=="Diciembre") or (mes=="DICIEMBRE"):
    print("Usted es de Sagitario")
    
if (dia>=22) and (dia<=31) and (mes=="diciembre") or (mes=="Diciembre") or (mes=="DICIEMBRE"):
    print("Usted es de Capricornio")
if (dia>=1) and (dia<=20) and (mes=="enero") or (mes=="Enero") or (mes=="ENERO"):
    print("Usted es de Capricornio")
    
if (dia>=21) and (dia<=31) and (mes=="enero") or (mes=="Enero") or (mes=="ENERO"):
    print("Usted es de Acuario")
if (dia>=1) and (dia<=19) and (mes=="febrero") or (mes=="Febrero") or (mes=="FEBRERO"):
    print("Usted es de Acuario")
        
if (dia>=20) and (dia<=29) and (mes=="febrero") or (mes=="Febrero") or (mes=="FEBRERO"):
    print("Usted es de Pisis")
if (dia>=1) and (dia<=20) and (mes=="marzo") or (mes=="Marzo") or (mes=="MARZO"):
    print("Usted es de Pisis")


if (dia<1) and (dia>31):
    print("El nÃºmero ingresado no corresponde a un dÃ­a del mes")
