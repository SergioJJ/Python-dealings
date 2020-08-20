module ha_tb();

reg a,b;
wire cout, sum;

ha HA1 (cout, sum, a, b);

initial
begin
a = 1'b0; b = 1'b0;
#1
a = 1'b0; b = 1'b1;
#1
a = 1'b1; b = 1'b0;
#1
a = 1'b1; b = 1'b1;

end

initial $monitor("%b + %b = %b%b",a,b, cout, sum);

endmodule