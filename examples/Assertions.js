/*jslint plusplus: true, white: true*/
/*global println*/

// -------------
// Assertions.js
// -------------

function assert (b) {
    "use strict";
    if (!b) {
        throw "Assertion Error"; }}

function cycle_length (n) {
    "use strict";
    assert(n > 0);
    var c = 0;
    while (n > 1) {
        if ((n % 2) === 0) {
            n = n / 2;}
        else {
            n = (3 * n) + 1;}
        ++c;}
    assert(c > 0);
    return c;}

println("Assertions.js");

assert(cycle_length( 1) === 1);
assert(cycle_length( 5) === 6);
assert(cycle_length(10) === 7);

println("Done.");

/*
Assertions.js
script error in file Assertions.js : Assertion Error in Assertions.js at line number 11
*/
