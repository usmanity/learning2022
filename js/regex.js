// creates a new regex object
var re = new RegExp("^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,4}$");
const email = "usman6@gmail.com";
// validates an email address using the regex object
var isValid = re.test(email);
console.log(isValid);

var gptReg = new RegExp("[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}");
isValid = gptReg.test(email);
console.log(isValid);

console.log(gptReg.test("m@m.co"));
console.log(re.test("m@m.co"));
