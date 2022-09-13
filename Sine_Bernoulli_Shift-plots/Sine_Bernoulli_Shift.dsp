// Bernoulli Shift

import("stdfaust.lib");
// sine
sine(ph) = sin(ph * 2 * ma.PI);
// x = a number between 0 and 1. f = frequency of the motion
Bernoulli(x) = sine(x : \(n,y).((y*2)+n)~_ : \(z).(z-int(z)));
random(seed) = abs( (int(seed+1) * 1103515245)/2147483647.0 );
voices = 3;
process =   par( i, voices, Bernoulli(random(i) * .0001) );