module RCA16b_tb();


wire COUT, CIN;
integer read_file, write_file, value_r;
reg carry_in, clk;
reg [15:0] arrayA;
reg [15:0] arrayB;

wire [15:0] SOUT;   // output excluding the carryout bit, 
wire [16:0] SUM;    // this is used for Python verification module to simplify output

RCA16b DUT (COUT, CIN, SOUT, arrayA, arrayB);

assign CIN = carry_in;
assign SUM [16] = COUT;    // 17th bit possible from adding 2 16 bit values
assign SUM [15:0] = SOUT;  // the "meat" of adding two 16 bit values

initial 
begin
    clk = 1;
    carry_in = 0;
    arrayA = 0;
    arrayB = 0;
    read_file = $fopen("in_vec.txt", "r");  //reads in the input file generated from python script
    write_file = $fopen("out_vec.txt","w");  // writes to output file that will be analyzed by python script
end

always # 1 clk = ~clk;  // clk for simulation stepping

initial 
begin @ (posedge clk);
    while (!$feof(read_file))
    begin @ (posedge clk);
    value_r = $fscanf(read_file, "%h %h\n",arrayA,arrayB);   // reads in input file on every pos clk edge, sorts into A,  B input column
    end
    @ (posedge clk);
    $fclose(read_file);
    $fclose(write_file); // closes out both files,
    #1 $finish;
end

/* // this block used for manual verification, no python
initial
begin
arrayA = 4'h0; arrayB = 4'h0; carry_in = 1'b0;
#1
arrayA = 4'h0; arrayB = 4'h0; carry_in = 1'b1;
#1
arrayA = 4'h1; arrayB = 4'h0; carry_in = 1'b1;
#1
arrayA = 4'h1; arrayB = 4'h3; carry_in = 1'b0;
#1
arrayA = 4'h5; arrayB = 4'h3; carry_in = 1'b0;
#1
arrayA = 4'h7; arrayB = 4'h8; carry_in = 1'b1;
#1
arrayA = 4'h8; arrayB = 4'h8; carry_in = 1'b0;
#1
arrayA = 4'hf; arrayB = 4'hf; carry_in = 1'b1;
end
*/
always @ (negedge clk)
begin
    $fwrite(write_file,"%0d %0d %0d\n", arrayA, arrayB, SUM);
end
//initial $monitor("Array A %d + Array B %d = %d %b",arrayA,arrayB, SUM, SUM);

endmodule