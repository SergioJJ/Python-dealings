module RCA4b(COUT,S0,S1,S2,S3,A0,A1,A2,A3,B0,B1,B2,B3,CIN);

input A0,A1,A2,A3,B0,B1,B2,B3,CIN;
output S0,S1,S2,S3,COUT;

wire C1,C2,C3;

fa FA0 (C1,   S0, A0, B0, CIN);
fa FA1 (C2,   S1, A1, B1, C1);
fa FA2 (C3,   S2, A2, B2, C2);
fa FA3 (COUT, S3, A3, B3, C3);



endmodule