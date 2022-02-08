OPENQASM 2.0;
include "qelib1.inc";

gate oracle a, b, c, d {
  x b;
  cu3(0, pi/4, 0) a, d;
  cx a, b;
  cu3(0, -pi/4, 0) b, d;
  cx a, b;
  cu3(0, pi/4, 0) b, d;
  cx b, c;
  cu3(0, -pi/4, 0) c, d;
  cx a, c;
  cu3(0, pi/4, 0) c, d;
  cx b, c;
  cu3(0, -pi/4, 0) c, d;
  cx a, c;
  cu3(0, pi/4, 0) c, d;
  x b;
}

gate cccz a, b, c, d {
    cu3(0, pi/4, 0) a, d;
    cx a, b;
    cu3(0, -pi/4, 0) b, d;
    cx a, b;
    cu3(0, pi/4, 0) b, d;
    cx b, c;
    cu3(0, -pi/4, 0) c, d;
    cx a, c;
    cu3(0, pi/4, 0) c, d;
    cx b, c;
    cu3(0, -pi/4, 0) c, d;
    cx a, c;
    cu3(0, pi/4, 0) c, d;
}

gate ism a, b, c, d {
    h a;
    h b;
    h c;
    h d;
    x a;
    x b;
    x c;
    x d;
    cccz a, b, c, d;
    x a;
    x b;
    x c;
    x d;
    h a;
    h b;
    h c;
    h d;
}

qreg q[4];

h q;

oracle q[0], q[1], q[2], q[3];
ism q[0], q[1], q[2], q[3];

oracle q[0], q[1], q[2], q[3];
ism q[0], q[1], q[2], q[3];

oracle q[0], q[1], q[2], q[3];
ism q[0], q[1], q[2], q[3];