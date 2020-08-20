module RCA4b_tb();


wire COUT,S0,S1,S2,S3,A0,A1,A2,A3,B0,B1,B2,B3,CIN;
reg carry_in;
reg [3:0] arrayA;
reg [3:0] arrayB;

wire [3:0] SOUT;

RCA4b DUT (COUT,S0,S1,S2,S3,A0,A1,A2,A3,B0,B1,B2,B3,CIN);

assign CIN = carry_in;

assign SOUT[0] = S0;
assign SOUT[1] = S1;
assign SOUT[2] = S2;
assign SOUT[3] = S3;

assign A0 = arrayA[0];
assign A1 = arrayA[1];
assign A2 = arrayA[2];
assign A3 = arrayA[3];

assign B0 = arrayB[0];
assign B1 = arrayB[1];
assign B2 = arrayB[2];
assign B3 = arrayB[3];

`ifdef T1
initial
begin
$display("CIN,   ARRAY_A,  ARRAY_B,  SUM,  COUT");
arrayA = 4'h0; arrayB = 4'h0; carry_in = 1'b0;
#1
arrayA = 4'h5; arrayB = 4'h5; carry_in = 1'b0;

end

`endif

// iverilog -Wall -DT1 -o test 4bRCA_tb.v  4bRCA.v fa.v

initial
begin
$display("CIN,   ARRAY_A,  ARRAY_B,  SUM,  COUT");
arrayA = 4'h0; arrayB = 4'h0; carry_in = 1'b0;
#1
arrayA = 4'h0; arrayB = 4'h1; carry_in = 1'b0;
#1
arrayA = 4'h1; arrayB = 4'h3; carry_in = 1'b0;
#1
arrayA = 4'h1; arrayB = 4'h3; carry_in = 1'b1;
#1
arrayA = 4'h5; arrayB = 4'h3; carry_in = 1'b0;
#1
arrayA = 4'h7; arrayB = 4'h8; carry_in = 1'b0;
#1
arrayA = 4'h8; arrayB = 4'h8; carry_in = 1'b0;
end

initial 
begin
//#5 $monitoron; // controls when the monitor actually shows what's happening
$monitor("%b,      %d,       %d,       %d,    %b",CIN,arrayA,arrayB, SOUT,COUT);
//#10 $monitoroff;

end


endmodule