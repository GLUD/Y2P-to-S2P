donde = raw_input("Ingrese la direccion del archivo: ").replace(" ", "")
print "\nLa ruta es:", donde,"\n\n\n"
l=len(donde)
a=".y2p"
if donde[l-4:l]==a:
    f=open(donde, 'rb')	#Se abre el archivo .y2p
    ls=f.readlines()        	#Se lee el archivo
    linea=0
    archi=open('resultado.s2p','w')	#Se crea el archivo .s2p
    #Escritura de lineas fijas
    archi.write('#Archivo .S2P a partir de .Y2P\n')
    archi.write('#Autor: Jonnathan Sebastian Sanchez Sanabria\n')
    archi.write('#Grupo de trabajo GNU/Linux Universidad Distrital (GLUD)\n')
    archi.write('#License: GPLv3\n')
    archi.write('#Year:2017\n')

    archi.write('!Freq.(MHz) S11(Real) S11(Imag) S21(Real) S21(Imag) S12(Real) S12(Imag) S22(Real) S22(Imag)\n')
        #archi.write('Linea 3\n')
        #archi.close()

    for i,j in zip (ls,range(len(ls))):
        if i[0:5]=='! Mhz':
            linea=j
    print "Archivo creado exitosamente:\nNombre del archivo:resultado.s2p\nUbicacion:Esta carpeta"
    #print linea,len(ls)
    compi = []
    for i in range(linea+1,len(ls)):
        datos =  filter(None, (ls[i].replace(" ","\t")).split("\t"))
        clean_data = filter(None, [i.replace("\r\n",'') for i in datos])
        freq=float(clean_data[0])#*1000000
        archi.write(str(freq))
        archi.write(" ")
        Yi = complex(float(clean_data[1]),float(clean_data[2]))
        Yf = complex(float(clean_data[3]),float(clean_data[4]))
        Yr = complex(float(clean_data[5]),float(clean_data[6]))
        Yo = complex(float(clean_data[7]),float(clean_data[8]))
        vares = [Yi,Yf,Yr,Yo]
        compi.append(vares)
        #print "Parametros Y"
        #print Yi,Yr,Yf,Yo
        S11=((1-Yi)*(1+Yo)+(Yr*Yf))/((1-Yi)*(1+Yo)-(Yr*Yf))		#S11
        #archi.write(str(S11))
        s11real=S11.real
        s11imag=S11.imag
        archi.write(str(s11real))
        archi.write(" ")
        archi.write(str(s11imag))
        S12=((-2*Yr)/((1+Yi)*(1+Yo)-(Yr*Yf)))			#S12
        s12real=S12.real
        s12imag=S12.imag
        archi.write(str(s12real))
        archi.write(" ")
        archi.write(str(s12imag))
        archi.write(" ")
        S21=((-2*Yf)/((1+Yi)*(1+Yo)-(Yr*Yf)))			#S21
        s21real=S21.real
        s21imag=S21.imag
        archi.write(str(s21real))
        archi.write(" ")
        archi.write(str(s21imag))
        archi.write(" ")
        S22=(((1+Yi)*(1-Yo)+(Yr*Yf))/((1+Yi)*(1+Yo)-(Yr*Yf)))	#S22
        s22real=S22.real
        s22imag=S22.imag
        archi.write(str(s22real))
        archi.write(" ")
        archi.write(str(s22imag))
        archi.write("\n")
        #print "Parametros S"
        #print S11,S12,S21,S22

else:
    print "La ruta no llega a un archivo .y2p\nError de capa 8"
    #print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n","Archivo creado con exito"
