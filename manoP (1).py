import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
xDedos = []
yDedos = []

xIzquierda = []
yIzquierda = []

xDerecha = []
yDerecha = []


#INICIO MANO CARLOS BARON
#IZQUIERDA
xIzquierda.append(1.5);
xIzquierda.append(2.5);
xIzquierda.append(3.5);
xIzquierda.append(4.5);
xIzquierda.append(5.5);
xIzquierda.append(6.5);
xIzquierda.append(7.5);
xIzquierda.append(8.5);
xIzquierda.append(9.5);
xIzquierda.append(10.5);
xIzquierda.append(11.5);
yIzquierda.append(37);
yIzquierda.append(34);
yIzquierda.append(32.3);
yIzquierda.append(30.8);
yIzquierda.append(29.6);
yIzquierda.append(28.3);
yIzquierda.append(26);
yIzquierda.append(21.5);
yIzquierda.append(16.9);
yIzquierda.append(15);
yIzquierda.append(13.4);
#DEDOS
xDedos.append(1.5);
xDedos.append(2.2);
xDedos.append(2.9);
xDedos.append(3.6);
xDedos.append(4.3);
xDedos.append(5);
xDedos.append(5.7);
xDedos.append(6.4);
xDedos.append(7.1);
xDedos.append(7.8);
xDedos.append(8.5);
xDedos.append(9.2);
xDedos.append(9.9);
xDedos.append(10.6);
xDedos.append(11.3);
xDedos.append(12);
xDedos.append(12.7);
xDedos.append(13.4);
xDedos.append(14.1);
xDedos.append(14.8);
xDedos.append(15.5);
xDedos.append(16.2);
xDedos.append(16.9);
xDedos.append(17.6);
xDedos.append(18.3);
xDedos.append(19);
xDedos.append(19.7);
xDedos.append(20.4);
xDedos.append(21.1);
xDedos.append(21.8);
xDedos.append(23);
xDedos.append(23.7);
xDedos.append(24.4);
xDedos.append(25.1);
xDedos.append(25.8);
xDedos.append(26.7);
xDedos.append(27.4);
xDedos.append(28.1);
xDedos.append(28.8);
xDedos.append(29.5);
xDedos.append(30.2);
xDedos.append(30.9);
xDedos.append(31.6);
xDedos.append(32.3);
xDedos.append(33);
xDedos.append(33.7);
xDedos.append(34.4);
xDedos.append(35.1);
xDedos.append(36);
yDedos.append(37);
yDedos.append(37.8);
yDedos.append(38);
yDedos.append(37.7);
yDedos.append(37.2);
yDedos.append(36.3);
yDedos.append(34.6);
yDedos.append(33.5);
yDedos.append(32.9);
yDedos.append(32.2);
yDedos.append(31);
yDedos.append(30.6);
yDedos.append(34.3);
yDedos.append(44);
yDedos.append(45);
yDedos.append(44.6);
yDedos.append(43.8);
yDedos.append(37);
yDedos.append(33.4);
yDedos.append(41);
yDedos.append(45.8);
yDedos.append(46.7);
yDedos.append(47);
yDedos.append(46.3);
yDedos.append(40.6);
yDedos.append(33);
yDedos.append(33.6);
yDedos.append(35.5);
yDedos.append(39);
yDedos.append(42);
yDedos.append(44.7);
yDedos.append(44.8);
yDedos.append(44);
yDedos.append(27.3);
yDedos.append(25.7);
yDedos.append(25.3);
yDedos.append(25.6);
yDedos.append(26);
yDedos.append(26.7);
yDedos.append(27.4);
yDedos.append(28.3);
yDedos.append(29.1);
yDedos.append(29.9);
yDedos.append(30.4);
yDedos.append(31);
yDedos.append(31.4);
yDedos.append(31.3);
yDedos.append(31);
yDedos.append(30);
#DERECHA
xDerecha.append(22.5);
xDerecha.append(23.5);
xDerecha.append(24.5);
xDerecha.append(25.5);
xDerecha.append(26.5);
xDerecha.append(27.5);
xDerecha.append(28.5);
xDerecha.append(29.5);
xDerecha.append(30.5);
xDerecha.append(31.5);
xDerecha.append(32.5);
xDerecha.append(33.5);
xDerecha.append(34.5);
xDerecha.append(35.5);
xDerecha.append(36);
yDerecha.append(12.8);
yDerecha.append(13.5);
yDerecha.append(14.6);
yDerecha.append(16.6);
yDerecha.append(18.1);
yDerecha.append(20);
yDerecha.append(21);
yDerecha.append(22.2);
yDerecha.append(23.3);
yDerecha.append(24.4);
yDerecha.append(25);
yDerecha.append(26.1);
yDerecha.append(27.9);
yDerecha.append(29);
yDerecha.append(30);
#FIN MANO CARLOS BARON



"""
#INICIO MANO SANTIAGO RODRIGUEZ
xDedos.append(2);
xDedos.append(3);
xDedos.append(4.5);
xDedos.append(6);
xDedos.append(7);
xDedos.append(8.3);
xDedos.append(9);
xDedos.append(10);
xDedos.append(11);
xDedos.append(12.3);
xDedos.append(13.6);
xDedos.append(14.3);
xDedos.append(14.8);
xDedos.append(15.8);
xDedos.append(16.1);
xDedos.append(16.9);
xDedos.append(17.4);
xDedos.append(18.3);
xDedos.append(19);
xDedos.append(19.3);
xDedos.append(20);
xDedos.append(21);
xDedos.append(22.5);
xDedos.append(23.3);
xDedos.append(23.5);
xDedos.append(24);
xDedos.append(24.8);
xDedos.append(25.3);
xDedos.append(26);
xDedos.append(26.5);
xDedos.append(27.2);
xDedos.append(28);
xDedos.append(28.5);
xDedos.append(28.8);
xDedos.append(29.4);
xDedos.append(30.6);
xDedos.append(31.5);
xDedos.append(32.5);
xDedos.append(33.1);
xDedos.append(34.5);
xDedos.append(35.2);
xDedos.append(35.7);
yDedos.append(26);
yDedos.append(26.7);
yDedos.append(27);
yDedos.append(26.8);
yDedos.append(26);
yDedos.append(24.4);
yDedos.append(23);
yDedos.append(21);
yDedos.append(19.5);
yDedos.append(19);
yDedos.append(33);
yDedos.append(42.7);
yDedos.append(43.3)
yDedos.append(43.4);
yDedos.append(42.9);
yDedos.append(38);
yDedos.append(32);
yDedos.append(28);
yDedos.append(34);
yDedos.append(40.4);
yDedos.append(44.8);
yDedos.append(45.5);
yDedos.append(45.6);
yDedos.append(44.8);
yDedos.append(36);
yDedos.append(29);
yDedos.append(34.6);
yDedos.append(39.8);
yDedos.append(43);
yDedos.append(43.8);
yDedos.append(43.7);
yDedos.append(43.5);
yDedos.append(36);
yDedos.append(29);
yDedos.append(25.7);
yDedos.append(29);
yDedos.append(31.5);
yDedos.append(34.5);
yDedos.append(36.2);
yDedos.append(36.4);
yDedos.append(36);
yDedos.append(35);
xIzquierda.append(2);
xIzquierda.append(3);
xIzquierda.append(4);
xIzquierda.append(5);
xIzquierda.append(6);
xIzquierda.append(7);
xIzquierda.append(8);
xIzquierda.append(9);
xIzquierda.append(10);
xIzquierda.append(11);
xIzquierda.append(12);
yIzquierda.append(26);
yIzquierda.append(24);
yIzquierda.append(22);
yIzquierda.append(20);
yIzquierda.append(18.5);
yIzquierda.append(17);
yIzquierda.append(15);
yIzquierda.append(13);
yIzquierda.append(11);
yIzquierda.append(9.5);
yIzquierda.append(8);
yDerecha.append(8);
yDerecha.append(10.3);
yDerecha.append(12);
yDerecha.append(16);
yDerecha.append(22.5);
yDerecha.append(27);
yDerecha.append(30.5);
yDerecha.append(35);
xDerecha.append(30.5);
xDerecha.append(31);
xDerecha.append(31.5);
xDerecha.append(32);
xDerecha.append(33);
xDerecha.append(34);
xDerecha.append(35);
xDerecha.append(35.7);
#FIN MANO SANTIAGO RODRIGUEZ
"""
"""
#INICIO MANO CARLOS CAMACHO
#IZQUIERDA
xIzquierda.append(2);
xIzquierda.append(2.7);
xIzquierda.append(3.7);
xIzquierda.append(4.7);
xIzquierda.append(5.7);
xIzquierda.append(6.7);
xIzquierda.append(7.7);
xIzquierda.append(8.7);
xIzquierda.append(9.7);
xIzquierda.append(10.7);
xIzquierda.append(11.7);
yIzquierda.append(38.2);
yIzquierda.append(36);
yIzquierda.append(34.7);
yIzquierda.append(33);
yIzquierda.append(30.7);
yIzquierda.append(29.8);
yIzquierda.append(27);
yIzquierda.append(24.5);
yIzquierda.append(17.6);
yIzquierda.append(16.5);
yIzquierda.append(14);
#DEDOS
xDedos.append(2);
xDedos.append(2.5);
xDedos.append(3.4);
xDedos.append(3.9);
xDedos.append(4.6);
xDedos.append(5);
xDedos.append(6.2);
xDedos.append(6.9);
xDedos.append(7.4);
xDedos.append(8);
xDedos.append(8.8);
xDedos.append(9.4);
xDedos.append(10);
xDedos.append(10.9);
xDedos.append(11.8);
xDedos.append(12.5);
xDedos.append(13);
xDedos.append(13.8);
xDedos.append(14.8);
xDedos.append(15.4);
xDedos.append(15.9);
xDedos.append(16.5);
xDedos.append(16.9);
xDedos.append(17.8);
xDedos.append(18.9);
xDedos.append(19.7);
xDedos.append(19.8);
xDedos.append(21.5);
xDedos.append(22.9);
xDedos.append(23.3);
xDedos.append(24.5);
xDedos.append(25.5);
xDedos.append(26);
xDedos.append(27.3);
xDedos.append(27.8);
xDedos.append(28.7);
xDedos.append(29);
xDedos.append(29.5);
xDedos.append(30);
xDedos.append(30.9);
xDedos.append(31.6);
xDedos.append(32.7);
xDedos.append(33);
xDedos.append(33.8);
xDedos.append(35.4);
xDedos.append(36);
yDedos.append(38.2);
yDedos.append(38.8);
yDedos.append(39);
yDedos.append(38.1);
yDedos.append(37.5);
yDedos.append(36.8);
yDedos.append(34.5);
yDedos.append(33.2);
yDedos.append(32.9);
yDedos.append(31.8);
yDedos.append(31);
yDedos.append(30.8);
yDedos.append(34.6);
yDedos.append(45);
yDedos.append(46);
yDedos.append(45.6);
yDedos.append(44.8);
yDedos.append(36.8);
yDedos.append(34);
yDedos.append(40);
yDedos.append(45.6);
yDedos.append(46.9);
yDedos.append(47);
yDedos.append(46.5);
yDedos.append(40.5);
yDedos.append(34);
yDedos.append(34.6);
yDedos.append(42.3);
yDedos.append(45.7);
yDedos.append(45.8);
yDedos.append(45);
yDedos.append(26.8);
yDedos.append(25.5);
yDedos.append(24.9);
yDedos.append(24.6);
yDedos.append(26.3);
yDedos.append(26.8);
yDedos.append(27.7);
yDedos.append(28);
yDedos.append(29.4);
yDedos.append(30);
yDedos.append(30.6);
yDedos.append(32);
yDedos.append(32.4);
yDedos.append(32.6);
yDedos.append(32);
#DERECHA
xDerecha.append(22.7);
xDerecha.append(23.7);
xDerecha.append(24.7);
xDerecha.append(25.7);
xDerecha.append(26.7);
xDerecha.append(27.7);
xDerecha.append(28.7);
xDerecha.append(29.7);
xDerecha.append(30.7);
xDerecha.append(31.7);
xDerecha.append(32.7);
xDerecha.append(33.7);
xDerecha.append(34.7);
xDerecha.append(35.7);
xDerecha.append(36);
yDerecha.append(13);
yDerecha.append(13.7);
yDerecha.append(14.8);
yDerecha.append(16.5);
yDerecha.append(18.2);
yDerecha.append(22);
yDerecha.append(23);
yDerecha.append(23.2);
yDerecha.append(24.3);
yDerecha.append(25.4);
yDerecha.append(26);
yDerecha.append(26.5);
yDerecha.append(27.8);
yDerecha.append(30);
yDerecha.append(32);
#FIN MANO CARLOS CAMACHO
"""


x = np.array(xDedos)
y = np.array(yDedos)


xi = np.array(xIzquierda)
yi = np.array(yIzquierda)

xd = np.array(xDerecha)
yd = np.array(yDerecha)



splDedos = interpolate.splrep(x, y)
xnew = np.linspace(min(x), max(x), 500)
ynew = interpolate.splev(xnew, splDedos)

splIzq = interpolate.splrep(xi, yi)
xinew = np.linspace(min(xi), max(xi), 500)
yinew = interpolate.splev(xinew, splIzq)

splDer = interpolate.splrep(xd, yd)
xdnew = np.linspace(min(xd), max(xd), 500)
ydnew = interpolate.splev(xdnew, splDer)


plt.plot(xinew, yinew, xnew, ynew, xdnew, ydnew, x, y, 'o', xi, yi, 'x', xd, yd, 'x')


plt.show()


