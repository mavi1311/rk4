En esta parte explicaremos paso a paso como revolver un ejemplo de un problema dinamico de valor inicial utilizando el método RK4 en python

Teniendo como operador O una matriz 2x2 como la siguiente:

$$ \left( \begin{array}{ll} 0 & 1 \\ 1 & 0 \end{array} \right) $$

Cuyo código en python sería el siguiente:

``` py
Oper = np.array([[0, 1], [1, 0]])

print(Oper)
```

Podemos notar que dicho operador no es diagonal, por lo cual se espera que conforme avance el tiempo el operador modifica el estado y(t).


Seguidamente se define un estado inicial , dicho estado puede representar cantidades físicas de un sistema. COnsideramos como estado inicial una matriz 2x2 nada por:

$$ \left( \begin{array}{ll} 0 & 0 \\ 0 & 1 \end{array} \right) $$

Ahora implementamos la función f(y,t) en Python:

``` py
def dyn_generator(oper, state):
    return (-1.0j)*(np.dot(oper,state)-np.dot(state,oper))
```


También implementamos la función que realiza la operación dinámica en python con el método RK4:

``` py
def rk4(func, oper, state, h):
    k_1 = h * func(oper , state)
    k_2 = h * func(oper , state + (k_1)/(2))
    k_3 = h * func(oper , state + (k_2)/(2))
    k_4 = h * func(oper , state + k_3)
    return state + 1/(6) * (k_1 + 2 * k_2 + 2* k_3 + k_4)
```

Teniendo estas dos funciones ahora podemos evaluar la dinámica temporal de una grilla temporal unidimensional. Utilizando la función np.linspace creamos un arreglo de valores temporales:

``` py
times = np.linspace(0.0,10.0,50)
print(times)
```

Este código anterior nos da una lista de valores desde 0 a 10 con una separación de 0,5 entre cada valor.

Ahora necesitamos definirle un valor a h:

``` py
h = times[1] - times [0]
```

Creamos una rutina para realizar la evolución temporal. PAra ellos primero creamos una copia del operador que representa el valor inicial:

``` py
yCopy = yInit.copy()
```

Y luego llamamos la rutina rk4(), calculando el estado del sistema y(t) a través del tiempo y vamos a guardar la entrada (0,0) y (0,1) de la matriz y(t). Para esto vamos a inicializar dos arreglos que van a contener los valores con valores iniciales cero, utilizando el mismo tamaño del arreglo que contiene la variable independiente temporal:

``` py
stateQuant00 = np.zeros(times.size)
stateQuant11 = np.zeros(times.size)
```

Realizamos la rutina principal que realiza la evolución temporal:

Primero guardamos los valores de las entradas de yInit (0,0) y (1,1) en los arreglos que definimos:

``` py
stateQuant00[tt] = yCopy[0,0].real
stateQuant11[tt] = yCopy[1,1].real
```
    
Luego invocamos rk4 operando sobre yInit y devolvemos el resultado a una nueva variable yN

``` py
yN = rk4(dyn_generator,oOper,yCopy, h)
```
    
Después asignamos yN a yInit:

``` py
yCopy = yN
```

De esta manera, en la siguente iteracción, el operador de esta iteracción se convierte en el inicial de la siguiente iteración.

Podemos graficar estos resultados utilizando matplotlib:

``` py
plt.plot(times,stateQuant00)
```

![Gráfica de los resultados](/Descargas/grafica_tarea_2.png)
