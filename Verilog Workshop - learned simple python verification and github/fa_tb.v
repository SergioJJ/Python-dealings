module fa_tb();

reg a,b,cin;
wire cout, sum;

fa FA1 (cout, sum, a, b, cin);

initial
begin
a = 1'b0; b = 1'b0; cin = 1'b0;
#1
a = 1'b0; b = 1'b1; cin = 1'b0;
#1
a = 1'b1; b = 1'b0; cin = 1'b0;
#1
a = 1'b1; b = 1'b1; cin = 1'b0;
#1
a = 1'b0; b = 1'b0; cin = 1'b1;
#1
a = 1'b0; b = 1'b1; cin = 1'b1;
#1
a = 1'b1; b = 1'b0; cin = 1'b1;
#1
a = 1'b1; b = 1'b1; cin = 1'b1;

end

initial $monitor("CIN = %b, %b + %b = %b%b",cin,a,b, cout,sum);

endmodule