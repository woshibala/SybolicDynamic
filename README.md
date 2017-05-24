# Modified Hopcroft algorithm
> We know that every sofic shift has a right-resolving presentation. In order to learn from sofic shift, it’s necessary to have a minimal presentation for every sofic shift. Because sofic shifts are analogous to DFA, it’s intuitive for us to looking for existed algorithms in the automata theory. DFA minimization is such a task that transforming a given deterministic finite automaton (DFA) into an equivalent DFA that a mini- mum number of states [4]. One algorithm for DFA minimization is Hopcroft’s algorithm, which is based on partition refinement, partitioning the DFA states into groups by their behavior.<br/>

> Update: In version 2, we get rid of the non-sink strongly connected component. Now the algorithm can deal with the "irreducible" sofic shift. "even_shift_with_extra" and "even_shift_with_2extra" are the examples, and both of them can be reduced to the two-node even shift. <br/>


Usage:<br/>
~~~~
python mod_hopcroft.py <input file>
~~~~
The input file storage the sofic in such a format:<br/>
~~~~
<start node> <end node> <label>
~~~~
<br/>


So for a four-node even shift the input file would look like:<br/>
~~~~
A B 0
B C 0
C D 0
D A 0
A A 1
C C 1
~~~~
<br/>

The output file uses the same format. For example, the minimized even shift looks like: <br/>
~~~~
AC AC 1
AC BD 0
BD AC 0
~~~~
<br/>

