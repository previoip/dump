fn get_type_name<T>(_: &T) -> String {
    String::from(format!("{:?}", std::any::type_name::<T>()))
}

fn hello_world() -> String {
    "Hello World".to_string()
}

fn main() {
    let s: String = hello_world();
    println!("{}", &s);
    let t = get_type_name(&s);
    println!("typeof \"{}\" -> {}", &s, &t);
}
