console.log("In the controller");

a = new Poll(32, new Date(), "Question?");
console.log(a);
var json = JSON.stringify(a);
b = new Poll();
b.fromJSONObject((new Function( "return" + json)()));
console.log(b);
console.log(a == b);