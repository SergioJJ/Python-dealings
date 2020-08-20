module fa(cout, sum, a, b, cin);

input a,b,cin;
output cout, sum;
wire AA,BA,BB;

xor XO1(AA, a, b);
xor XO2(sum, AA, cin);

and A1(BA, cin, AA);
and A2(BB, a, b);

or  OR(cout, BA, BB);

endmodule