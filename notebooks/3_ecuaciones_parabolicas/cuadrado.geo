// Cuadrado en [0, 1]^2

// Geometría
Point(1) = {0, 0, 0, 1};
Point(2) = {1, 0, 0, 1};
Point(3) = {1, 1, 0, 1};
Point(4) = {0, 1, 0, 1};
Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 1};
Curve Loop(1) = {3, 4, 1, 2};
Plane Surface(1) = {1};

// Grupos físicos
Physical Curve(1) = {3, 2, 1, 4};
Physical Surface(2) = {1};

// Parámetros de malla
npts = 101;
Transfinite Curve {3, 1, 4, 2} = npts Using Progression 1;
Transfinite Surface {1};
