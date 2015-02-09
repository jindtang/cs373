/*jslint white: true*/
/*global println*/

// -------------
// Variables.js
// -------------

// http://www.w3schools.com/js/js_variables.asp

function assert (b) {
    "use strict";
    if (!b) {
        throw "Assertion Error";}}

var h = 0;

function f () {
    "use strict";
     h = 1;
     assert(h === 1);}

function g () {
    "use strict";
    var h = 2;
    assert(h === 2);}

println("Variables.js");

assert(h === 0);
f();
assert(h === 1);
g();
assert(h === 1);

println("Done.");
