#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib as mpl;
import matplotlib.pyplot as plt;
from mpl_toolkits.mplot3d import Axes3D;
import numpy as np;

fig = plt.figure();
ax = fig.add_subplot(111, projection = "3d");

x = np.arange(-10, 10, 1).reshape((20, 1));
y = (np.zeros(20) + 1).reshape((1, 20));
sx = np.dot(x, y);

y = y.reshape((20, 1));
x = x.reshape((1, 20));
sy = np.dot(y, x);

sx = sx.reshape(400);
sy = sy.reshape(400);
sz = sx ** 2 + sy ** 2;

r = 100;
thet = np.random.rand(200) * np.pi * 2;
fai = np.random.rand(200) * np.pi;

x = 0 + r * np.sin(thet) * np.cos(fai);
y = 0 + r * np.sin(thet) * np.sin(fai);
z = 0 + r * np.cos(thet);

ax.scatter(x, y, z, c = 'b', marker = 'o');

ax.set_xlabel("X Label");
ax.set_ylabel("Y Label");
ax.set_zlabel("Z Label");

plt.show();
