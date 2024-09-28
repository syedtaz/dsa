use std::io;

fn main() -> () {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer);
    let contents: Vec<&str> = buffer.split(' ').collect();
    let n: u32 = contents[0].parse().unwrap();
    let m: u32 = contents[1].parse().unwrap();
    let a: u32 = contents[2].parse().unwrap();
    println!("{:?}", n.div_ceil(a) * m.div_ceil(a));
}
