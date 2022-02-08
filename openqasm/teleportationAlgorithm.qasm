OPENQASM 2.0;
include "qelib1.inc";

gate message a {
  u3(pi/3, 0, 3) a;
}

qreg q[4];
creg cZ[1];
creg cX[1];

message q[0];
barrier q;

h q[1];
cx q[1], q[2];
cx q[0], q[1];
h q[0];

barrier q;
measure q[0] -> cZ[0];
measure q[1] -> cX[0];
barrier q;

if (cX == 1) x q[2];
if (cZ == 1) z q[2];

message q[3];