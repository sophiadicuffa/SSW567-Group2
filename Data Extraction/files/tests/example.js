function example_function(input) {
    if(typeof(input) === "string") {
        input = input.split("").reverse().join("");
        return input;
    }
    else return "";
}

console.log(example_function("Hello World"));