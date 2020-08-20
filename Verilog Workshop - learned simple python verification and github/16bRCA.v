module RCA16b(COUT, CIN, arrayS, arrayA, arrayB);


input CIN; 
input [15:0] arrayA;
input [15:0] arrayB;
output COUT; 
output [15:0] arrayS;

wire C1,C2,C3;

RCA4b RCA1 (C1,arrayS [0], arrayS [1], arrayS [2], arrayS [3],arrayA [0],arrayA [1],arrayA [2],arrayA [3],arrayB [0],arrayB [1],arrayB [2],arrayB [3],CIN);
RCA4b RCA2 (C2,arrayS [4], arrayS [5], arrayS [6], arrayS [7],arrayA [4],arrayA [5],arrayA [6],arrayA [7],arrayB [4],arrayB [5],arrayB [6],arrayB [7],C1);
RCA4b RCA3 (C3,arrayS [8], arrayS [9], arrayS [10], arrayS [11],arrayA [8],arrayA [9],arrayA [10],arrayA [11],arrayB [8],arrayB [9],arrayB [10],arrayB [11],C2);
RCA4b RCA4 (COUT,arrayS [12], arrayS [13], arrayS [14], arrayS [15],arrayA [12],arrayA [13],arrayA [14],arrayA [15],arrayB [12],arrayB [13],arrayB [14],arrayB [15],C3);



endmodule