function ascii_to_string(ascii_codes) {
    let result = "";
    for (let i = 0; i < ascii_codes.length; i++) {
        result += String.fromCharCode(ascii_codes[i]);
    }
    return result;
}

// Example usage
let ascii_codes = [12,34,56,78];//Use the output of encoding.py
let result = ascii_to_string(ascii_codes);
console.log(result);
