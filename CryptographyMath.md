# Resources for Understanding and Computing Cryptography Mathematics
When cryptography comes up in discussion what are your true, honest feelings?
I think for many of us it's something like "my eyes cross looking at that.. but I WISH I COULD DO IT"

I felt that for a long time, but as it turns out, understanding the math behind cryptography is probably
more in reach than you think. The math behind it mostly algebra, some of it's a little spicy, 
but taking baby steps will get you there. This readme will attempt to serve as a reference that will guide you
towards understanding the basics behind cryptography all the way to libraries you can use to do really useful
things with it in software you build.

Let's start with the math. It's unclear to most of us what cryptography actually is and what you need to
study to use it. Outlined below are the fields that underly it. I'm missing some of them currently, but this will
be filled out with time. Being honest, it will probably take 6 months to Grok this all, but those 6 months will
pass anyways!

They key subjects you'll find useful in this study are:

### Abstract Algebra 
This is basically doing regular regular algebra on objects beyond just all real numbers. It can get 
deep, but for cryptography you really only need a few key slices of it to understand it.

The details you'll need to know in order of learning:
* Finite/Modular arithmetic (doing addition/substraction/multiplication/division on integers with remainders)
* Understanding of what "groups" and "fields" are (easier than it sounds, I promise)
* Understanding the "generators", "characteristics", "order", and "cofactors" of finite groups
* Subgroups, Subfields, and Prime Fields
* Understanding a special class of field called "Galois" fields
* Homomorphisms (a slightly more general word for "functions") between groups which preserve their structure
* Isogenys - a special type of morphism between groups (surjective)

### Algebraic Geometry 
This field studies geometry through algebra. Normally for small circles, triangles, elipses, parabolas, etc.
you can visualize them a graphing app and determine the properties of them through that. But when you start dealing 
with large numbers or complicated shapes, it becomes difficult to study visually. Alegbraic geometry allows us
to find useful properties of geometric objects by studying the alebgra that defines them.

In this field the things that are of key study are include
* Projective spaces (for cryptography this amounts to defining curves in new, useful ways)
* Relations: The generalization of functoins between two sets (such as ==, >=, is included)
* Binary Relations, Equivalence Relations, Injective & Surjective Functions
* Equivalence classes: Sets of elements that can be considered equivalent under certain relations (like the equal sign or multiplication!)
* Kernels: (A little intricate, but more or less the solution to functions when you set them to zero!)


## Math resources

### Beginner
* Practical cryptography for developers: https://cryptobook.nakov.com/
* Visualization of an Eliptic Curve in higher dimension (also called an "algebraic variety"): https://www.math3d.org/c16cy5nFq
* Math notation reference: https://mathvault.ca/hub/higher-math/math-symbols/

### Not Beginner
(Don't be afraid to tread here)
* Binary Relations: https://en.wikipedia.org/wiki/Binary_relation
* Equivalence Relations: https://www.math.cmu.edu/~mradclif/teaching/127S19/Notes/EquivalenceRelations.pdf
* Equivalence Classes: https://math24.net/equivalence-classes-partitions.html
* Equivalence Class Notation: https://math.stackexchange.com/questions/369635/what-is-the-standard-notation-for-a-set-of-equivalence-classes
* What is a projective space: https://www.youtube.com/watch?v=ZzJd1n_tUuU
* Eliptic Curve Point Addition in Projective CoordinateS: https://www.nayuki.io/page/elliptic-curve-point-addition-in-projective-coordinates
* Standard Projective Addition Formulas: https://en.wikibooks.org/wiki/Cryptography/Prime_Curve/Standard_Projective_Coordinates
* Understanding what the "point at infinity" is: https://crypto.stackexchange.com/questions/70507/in-elliptic-curve-what-does-the-point-at-infinity-look-like

### Super Sayan
(Don't be afraid to tread here either)
* Birational GeometrY: https://en.wikipedia.org/wiki/Birational_geometry


### Applied Information
* Why isn't RSA used to encrypt large files?: https://infosecwriteups.com/why-rsa-is-not-used-to-encrypt-large-files-d3172d83febd
