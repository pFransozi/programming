use std::{io};

fn main() {

    println!("Hello, world! Basics on Rust from Rust Essential Training eLearning LinkedIn.");
    // var_scope_basic_example();  
    // formatting_basic_example();
    // math_basic_operators();
    // input_basic_example();
    // bitwise_basic_example();
    compound_data_types();


}

fn compound_data_types()
{
    let mut letters = ['A', 'B', 'C'];
    let first_letter = letters[0];

    println!("The first letter is {}", first_letter);
    println!("The second letter is {}", letters[1]);

    letters[0] = 'Z';
    println!("The new first letter is {}", letters[0]);

    let numbers: [i32; 5];
    numbers = [0; 5];
    let index:usize = numbers.len();
    println!("The array len is {}", index);
    println!("The fourth number is {}", numbers[index -1 ]);

    println!("===============================================================");

    let parking_lot = [[1,2,3], [4,5,6]];

    let get_a_car = parking_lot[0][2];

    let garage: [[[i32; 100]; 10]; 5];
    let garage1 = [[[0; 100]; 10]; 5];


    let stuff: (u8, f32, char) = (10, 3.14, 'x');
    let first_item = stuff.0;
    println!("The value of the first item is {}", first_item);

    let (a, b, c) = stuff;
    println!("A is {}", a);
    println!("B is {}", b);
    println!("C is {}", c);

}

fn var_scope_basic_example()
{
    //this var lives in the var_scope_basic_example function();
    let outer_var = 112;

    println!("Outer var in the main function = {}", outer_var);
    
    //this is a small block, scope, inside the var_scope_basic_example function()
    {
        println!("Outer var inside a restrict scope {}", outer_var);

        //this var only exists inside the scope.
        let inner_var = 213;
        let outer_var = 100;
        println!("Inner var inside a restrict scope  = {}", inner_var);
        //it is possible access outer var.
        println!("Outer var inside a restrict scope before changed from 112 to 100 = {}", outer_var);
    }//end block

    println!("Outer var has been changed inside a restrict scope, and now out of the restrict scope, the value return");
    println!("Outer var in the main function = {}", outer_var);

    //but the it is not possible access inside the restrict scope.
    //println!("inner var out of the block = {}", inner_var);
}

fn bitwise_basic_example()
{

    let mut bin = 0b1010_1111u8; // a byte
    let dec_to_bin = 3;
    println!("Value is {}", bin);
    println!("Binary value is {:08b}", bin);
    println!("Value 10000000 to binary is {:b}", dec_to_bin);

    println!("Binary value is {:08b}", bin);
    bin = !bin;
    println!("Binary value is {:08b}, applied not operator.", bin);

    println!("Not operator: ");
    println!("not 1 = {:0b}", !0b1);
    println!("not 0 = {:0b}", !0b0);

    println!("");
    let a = true;
    let b = false;

    println!("A = {}, B = {}", a, b);
    println!("Not a is {}", !a);
    println!("A and b is {}", a & b);
    println!("A or b is {}", a | b);
    println!("A xor b is {}", a ^ b);

    let mut c = (a ^ b) | (a & b); //evaluate just the first, if it is sufficient.
    println!("C is  {}", c);

    c = (a ^ b) || panic!(); //evaluate just the first, if it is sufficient.
    println!("C is  {}", c);

}

fn formatting_basic_example()
{
    println!("==================================================================");
    println!("Using println format.");
    println!("{} days", 32);
    println!("{} days, {} months, {} years", 32, 13, 5000000);

    println!("Using format function, then println.");
    let message1 = format!("{}", 32);
    let message2 = format!("{} days, {} months, {} years", 32, 13, 5000000);

    println!("{message1}");
    println!("{message2}");

    println!("==================================================================");

    let a = 3.45;
    let b = 9.567789;
    let c = a / b;
    println!("Decimal value is {}", c);
    println!("Decimal value is {:.3}, with three numbers after dot.", c);
    println!("Decimal value is {:8.3}, with three numbers after dot and eight format position before.", c);
    println!("Decimal value is {:08.3}, with three numbers after dot and eight format position before.", c);
    println!("a / b = {:08.3},\na = {},\nb = {}", c, a, b);

    println!("==================================================================");

    print!("Using print fx ");
    print!("without ln");

    println!("");
    println!("Using positional param: 0 = {0}, 1 = {1}, 2 = {2}", a, b, c);
    println!("Using positional param: 2 = {2}, 0 = {0}, 1 = {1}", a, b, c);

    println!("==================================================================");

    println!("Base 10 repr:             {}", 65536);
    println!("Base 2 (binary) repr:   {:b}", 65536);
    println!("Base 8 (octal) repr:    {:o}", 65536);
    println!("Base 16 (hexadec) repr: {:x}", 65536);
    println!("Base 16 (hexadec) repr: {:X}", 65536);

    println!("==================================================================");

    println!("{0}, this is {1}. {1}, this is {0}", "Alice", "Bob");
    println!("{subject} {verb} {object}"
                , object="the lazy dog"
                , verb="jumps over"
                , subject="the quick brown fox");

    println!("{number:>5}", number=1);
    println!("{number:0>5}", number=1);
    println!("{number:0>width$}", number=1, width=6);

    println!("My name is {0}, {1} {0}", "Bond", "James");

    let message3 = format!("{:?}", (3, 4));
    let message4 = format!("{:#?}", (300, 400));

    println!("{message3}");
    println!("{message4}");

    println!("==================================================================");

    let hello_x = "Hello x    !";
    let hello_x1 = "Hello x----!";
    let hello_x2 = "Hello   x  !";
    let hello_x3 = "Hello     x!";

    let fm_hello_x = format!("Hello {:<5}!", "x");
    let fm_hello_x1 = format!("Hello {:-<5}!", "x");
    let fm_hello_x2 = format!("Hello {:^5}!", "x"); 
    let fm_hello_x3 = format!("Hello {:>5}!", "x");
    assert_eq!(fm_hello_x, hello_x );
    assert_eq!(fm_hello_x1, hello_x1);
    assert_eq!(fm_hello_x2, hello_x2);
    assert_eq!(fm_hello_x3, hello_x3 );

    println!("{fm_hello_x}");
    println!("{fm_hello_x1}");
    println!("{fm_hello_x2}");
    println!("{fm_hello_x3}");

    println!("==================================================================");

    let msg = "Hello +5!";
    let msg1 = "0x1b!";
    let msg2 = "Hello 00005!";
    let msg3 = "Hello -0005!";
    let msg4 = "0x0000001b!";

    let fmt_msg = format!("Hello {:+}!", 5);
    let fmt_msg1 = format!("{:#x}!", 27);
    let fmt_msg2 = format!("Hello {:05}!", 5);
    let fmt_msg3 = format!("Hello {:05}!", -5);
    let fmt_msg4 = format!("{:#010x}!", 27);

    assert_eq!(fmt_msg, msg);
    assert_eq!(fmt_msg1, msg1);
    assert_eq!(fmt_msg2, msg2);
    assert_eq!(fmt_msg3, msg3);
    assert_eq!(fmt_msg4, msg4);

    println!("{fmt_msg}");
    println!("{fmt_msg1}");
    println!("{fmt_msg2}");
    println!("{fmt_msg3}");
    println!("{fmt_msg4}");

    println!("==================================================================");

    println!("Hello {0} is {1:.5}", "x", 0.01);
    println!("Hello {1} is {2:.0$}", 5, "x", 0.01);
    println!("Hello {0} is {2:.1$}", "x", 5, 0.01);
    println!("Hello {} is {:.*}", "x", 5, 0.01);
    println!("Hello {1} is {2:.*}",  5, "x", 0.01);
    println!("Hello {} is {2:.*}",   "x", 5, 0.01);
    println!("Hello {} is {number:.prec$}", "x", prec = 5, number = 0.01);

    println!("==================================================================");


}

fn input_basic_example()
{
    println!("Guess the number!");
    println!("Input your guess: ");

    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line.");
    
    println!("You guessed: {guess}");
}

fn math_basic_operators()
{
    println!("Math operators");

    let mut a = 7;
    let mut b = 9;

    println!("a = {}, b = {}", a, b);
    println!("a + b = {}", a + b);
    println!("a - b = {}", a - b);
    println!("a / b = {}", a / b); 
    println!("a and b are integer numbers, so divide operator return integer part.");
    println!("a % b = {}", a % b);
    println!("a * b = {}", a * b);

    println!("");
    println!("Math operator 1");
    println!("");

    a = 5;
    let c = 0.78;
    println!("a = {}, c = {}", a, c);
    println!("a + b = {}", a as f64 + c);
    println!("a - b = {}", a as f64 - c);
    println!("a / b = {}", a as f64 / c); 
    println!("a and b are integer numbers, so divide operator return integer part.");
    println!("a % b = {}", a as f64 % c);
    println!("a * b = {}", a as f64 * c);

    let x = 8.25;
    let y = 9.68;

    println!("x = {} and y = {}", x, y);
    println!("x / y = {}", x / y);
    println!("x / y (both as integers) = {}", x as i32 / y as i32);
    println!("x % y = {}", x % y);
}