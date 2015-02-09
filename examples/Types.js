/*jslint white: true*/
/*global println*/

// --------
// Types.js
// --------

// http://www.w3schools.com/js/js_datatypes.asp

function assert (b) {
    "use strict";
    if (!b) {
        throw "Assertion Error";}}

function is_array (a) {
    "use strict";
    return a.constructor.toString().indexOf("Array") >= 0;}

function is_object (x) {
    "use strict";
    return x.constructor.toString().indexOf("Object") >= 0;}

println("Types.js");

var b = false;
b = true;
assert((typeof b) === "boolean");

var n = 2.34;
assert((typeof n) === "number");

var s = "abc";
assert((typeof s) === "string");

var a = [2, 3, 4];
assert((typeof a) === "object");
assert(is_array(a));
assert(a     instanceof Array);
assert(a     instanceof Object);
assert(Array instanceof Object);
assert(Object.getPrototypeOf(a)               === Array.prototype);
assert(Object.getPrototypeOf(Array.prototype) === Object.prototype);

var x = {n : 2.34, s : "abc", u : {v : [2, 3, 4]}};
assert((typeof x) === "object");
assert(is_object(x));
assert(x instanceof Object);
assert(Object.getPrototypeOf(x) === Object.prototype);

function inc (v) {
    "use strict";
    return v + 1;}
assert((typeof inc) === "function");
assert(inc      instanceof Function);
assert(inc      instanceof Object);
assert(Function instanceof Object);

assert(Object instanceof Object);
assert(Object.getPrototypeOf(Object.prototype) === null);

println("Done.");
