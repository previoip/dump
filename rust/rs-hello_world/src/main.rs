fn get_type_name<T>(_: &T) -> String {
    String::from(format!("{:?}", std::any::type_name::<T>()))
}

fn hello_world() -> String {
    "Hello World".to_string()
}


fn function_over() -> u32 {
    fn function_over() -> u32 {
        fn function_over() -> u32 {
            fn function_over() -> u32 {
                fn function_over() -> u32 {
                    17
                }
                function_over() - 9
            }
            function_over() * 8
        }
        function_over() + 5
    }
    function_over() 
}

fn main() {
    let mut s: String = hello_world();
    println!("{}", &s);
    s = get_type_name(&s);
    println!("typeof {}", &s);
    println!("magic number! {}",  function_over())
}
