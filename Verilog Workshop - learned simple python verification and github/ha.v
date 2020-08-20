module ha(cout, sum, a, b);

input a,b;
output cout, sum;

xor XO1(sum, a, b);
and A1(cout, a, b);


endmodule