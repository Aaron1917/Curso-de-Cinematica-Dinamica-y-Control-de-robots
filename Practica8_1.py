import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


def configuracion_grafica(x_lim_inf,x_lim_sup,y_lim_inf,y_lim_sup,z_lim_inf,z_lim_sup,titulo):
    plt.title("Matrices de rotación")
    # Definimos los limites de la gráfica
    grafica.set_xlim(x_lim_inf,x_lim_sup)
    grafica.set_ylim(y_lim_inf,y_lim_sup)
    grafica.set_zlim(z_lim_inf,z_lim_sup)
    
    # Definimos los ejes de la gráfica
    grafica.set_xlabel("X")
    grafica.set_ylabel("Y")
    grafica.set_zlabel("Z")
    grafica.view_init(elev=25, azim=30)


def sistema_coordenadas(x_i, y_i, z_i, x_f, y_f, z_f):
    # Definimos los valores de x, y, z
    x = [x_i, x_f]
    y = [y_i, y_f]
    z = [z_i, z_f]

    # Creamos una grafica en 3D
    grafica.plot3D(x, [y_i, y_i], [z_i, z_i], color="red")
    grafica.plot3D([x_i, x_i], y, [z_i, z_i], color="blue")
    grafica.plot3D([x_i, x_i], [y_i, y_i], z, color="green")

def matriz_rotacion_z(grados):
    rad=grados/180*np.pi
    rotacion=np.array([[np.cos(rad),-np.sin(rad),0],
                      [np.sin(rad),np.cos(rad),0],
                      [0,0,1]])
    return rotacion

def matriz_rotacion_y(grados):
    rad=grados/180*np.pi
    rotacion=np.array([[np.cos(rad),0,np.sin(rad)],
                      [0,1,0],
                      [-np.sin(rad),0,np.cos(rad)]])
    return rotacion

def matriz_rotacion_x(grados):
    rad=grados/180*np.pi
    rotacion=np.array([[1,0,0],
                      [0,np.cos(rad),-np.sin(rad)],
                      [0,np.sin(rad),np.cos(rad)]])
    return rotacion

def matriz_translacion_x(x):
    traslacion=np.array([[1,0,0,-x],
                         [0,1,0,0],
                         [0,0,1,0],
                         [0,0,0,1]])
    return traslacion

def matriz_translacion_y(y):
    traslacion=np.array([[1,0,0,0],
                         [0,1,0,-y],
                         [0,0,1,0],
                         [0,0,0,1]])
    return traslacion

def matriz_translacion_z(z):
    traslacion=np.array([[1,0,0,0],
                         [0,1,0,0],
                         [0,0,1,-z],
                         [0,0,0,1]])
    return traslacion

def sistema_coordenadas_movil(matriz_rotacion):
    # Definimos los componentes de la matriz de rotacion
    mr_11 = matriz_rotacion[0, 0]
    mr_12 = matriz_rotacion[0, 1]
    mr_13 = matriz_rotacion[0, 2]
    mr_21 = matriz_rotacion[1, 0]
    mr_22 = matriz_rotacion[1, 1]
    mr_23 = matriz_rotacion[1, 2]
    mr_31 = matriz_rotacion[2, 0]
    mr_32 = matriz_rotacion[2, 1]
    mr_33 = matriz_rotacion[2, 2]

    grafica.plot3D([0, mr_11], [0, mr_12], [0, mr_13], color="purple")
    grafica.plot3D([0, mr_21], [0, mr_22], [0, mr_23], color="gray")
    grafica.plot3D([0, mr_31], [0, mr_32], [0, mr_33], color="cyan")


def animacion_funcion_3D(grados_x, grados_y, grados_z):
    for i in range(grados_x):
        grafica.cla()
        configuracion_grafica(-10,10,-10,10,-10,10,"Funcion tipo solido")
        # Establecemos las coordenadas del solido
        X = np.arange(-5,5,0.25)
        Y = np.arange(-5,5,0.25)

        X, Y = np.meshgrid(X, Y)
        R = np.sqrt(X*2 + Y*2)
        Z = np.sin(R)
        indice=0
        for datos in zip(X,Y,Z):
            coordenadas_funcion=np.array([datos[0],datos[1],datos[2]])
            rotacion=matriz_rotacion_x(i)
            
            resultado=rotacion@coordenadas_funcion
            X[indice]=resultado[0]
            Y[indice]=resultado[1]
            Z[indice]=resultado[2]
            indice+=1
        # Creamos una figura en 3D
        surface = grafica.plot_surface(X, Y, Z, rstride=1, cstride=1,
                                    cmap=cm.coolwarm, linewidth=0,
                                    antialiased=False)
        plt.draw()
        plt.pause(0.1)
    X_cp=X.copy()
    Y_cp=Y.copy()
    Z_cp=Z.copy()
    
    for j in range(grados_y):
        grafica.cla()
        configuracion_grafica(-10,10,-10,10,-10,10,"Funcion tipo solido")
        # Establecemos las coordenadas del solido
        X = X_cp.copy()
        Y = Y_cp.copy()
        Z = Z_cp.copy()
        indice=0
        for datos in zip(X,Y,Z):
            coordenadas_funcion=np.array([datos[0],datos[1],datos[2]])
            rotacion=matriz_rotacion_y(j)
            
            resultado=rotacion@coordenadas_funcion
            X[indice]=resultado[0]
            Y[indice]=resultado[1]
            Z[indice]=resultado[2]
            indice+=1
        # Creamos una figura en 3D
        surface = grafica.plot_surface(X, Y, Z, rstride=1, cstride=1,
                                    cmap=cm.coolwarm, linewidth=0,
                                    antialiased=False)
        plt.draw()
        plt.pause(0.1) 
    X_cp=X.copy()
    Y_cp=Y.copy()
    Z_cp=Z.copy()
    for k in range(grados_z):
        grafica.cla()
        configuracion_grafica(-10,10,-10,10,-10,10,"Funcion tipo solido")
        # Establecemos las coordenadas del solido
        X = X_cp.copy()
        Y = Y_cp.copy()
        Z = Z_cp.copy()
        indice=0
        for datos in zip(X,Y,Z):
            coordenadas_funcion=np.array([datos[0],datos[1],datos[2]])
            rotacion=matriz_rotacion_z(k)
            
            resultado=rotacion@coordenadas_funcion
            X[indice]=resultado[0]
            Y[indice]=resultado[1]
            Z[indice]=resultado[2]
            indice+=1
        # Creamos una figura en 3D
        surface = grafica.plot_surface(X, Y, Z, rstride=1, cstride=1,
                                    cmap=cm.coolwarm, linewidth=0,
                                    antialiased=False)
        plt.draw()
        plt.pause(0.1)    


def animacion_3d_traslacion(x,y,z):
    for i in range(x):
        i+=1
        grafica.cla()
        configuracion_grafica(-10,10,-10,10,-10,10,"Funcion tipo sólido para traslacion")
        #Dibujando la grafica 
        X=np.arange(-5,5,0.25)
        Y=np.arange(-5,5,0.25)
        
        X,Y=np.meshgrid(X,Y)
        R=np.sqrt(X**2+Y**2)
        Z=np.sin(R)
        W=np.ones(len(Z)) #Contruccion de vector de unos para agregarlos a las coordenadas
        index=0
        for dato in zip(X,Y,Z,W):
            coordenadas_funcion=np.array([dato[0],dato[1],dato[2],dato[3]],dtype=object)
            traslacion_x=matriz_translacion_x(i)
            resultado=traslacion_x@coordenadas_funcion
            
            X[index]=resultado[0]
            Y[index]=resultado[1]
            Z[index]=resultado[2]
            index+=1
        surface=grafica.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=cm.coolwarm,linewidth=0,antialiased=False)
        plt.draw()
        plt.pause(0.01)
    X_cp=X.copy()
    Y_cp=Y.copy()
    Z_cp=Z.copy()

    for j in range(y):
        j+=1
        grafica.cla()
        configuracion_grafica(-10,10,-10,10,-10,10,"Funcion tipo sólido para traslacion")
        #Dibujando la grafica 
        X = X_cp.copy()
        Y = Y_cp.copy()
        Z = Z_cp.copy()
        W=np.ones(len(Z)) #Contruccion de vector de unos para agregarlos a las coordenadas
        index=0
        for dato in zip(X,Y,Z,W):
            coordenadas_funcion=np.array([dato[0],dato[1],dato[2],dato[3]],dtype=object)
            traslacion_y=matriz_translacion_y(j)
            resultado=traslacion_y@coordenadas_funcion
            
            X[index]=resultado[0]
            Y[index]=resultado[1]
            Z[index]=resultado[2]
            index+=1
        surface=grafica.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=cm.coolwarm,linewidth=0,antialiased=False)
        plt.draw()
        plt.pause(0.01)
    
    X_cp=X.copy()
    Y_cp=Y.copy()
    Z_cp=Z.copy()    
    for k in range(z):
        k+=1
        grafica.cla()
        configuracion_grafica(-10,10,-10,10,-10,10,"Funcion tipo sólido para traslacion")
        #Dibujando la grafica 
        X = X_cp.copy()
        Y = Y_cp.copy()
        Z = Z_cp.copy()
        W=np.ones(len(Z)) #Contruccion de vector de unos para agregarlos a las coordenadas
        index=0
        for dato in zip(X,Y,Z,W):
            coordenadas_funcion=np.array([dato[0],dato[1],dato[2],dato[3]],dtype=object)
            traslacion_z=matriz_translacion_z(k)
            resultado=traslacion_z@coordenadas_funcion
            
            X[index]=resultado[0]
            Y[index]=resultado[1]
            Z[index]=resultado[2]
            index+=1
        surface=grafica.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=cm.coolwarm,linewidth=0,antialiased=False)
        plt.draw()
        plt.pause(0.01)
        
    
    
           
# Definimos una gráfica
figura = plt.figure()
grafica = figura.add_subplot(projection='3d')# Configuramos la perspectiva en 3D
#animacion_funcion_3D(90,90,90)
#sistema_coordenadas(0, 0, 0, 1, 1, 1)
animacion_3d_traslacion(10,10,10)
plt.show()