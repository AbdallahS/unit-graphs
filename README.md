**Unit 2-interval graph checker**  

This python script checks if a given interval graph is a unit 2-interval graph using an encoding in answer set programming.

**Requirements**  

- Clingo
- NetworkX

**Usage**  

To run the code run the following command:

```bash
python3 generatorExauClingo.py graph_file.txt
```

The graph_file.txt must contain a list of graphs in the format described in http://www.jaist.ac.jp/~uehara/graphs/ .  
That is, each interval graph is represented in one line in a simple text format, e.g., 1 1 2 2 3 3 (independent set of three vertices), 1 2 1 3 2 3 (path of length 3), 1 2 3 3 2 1 (complete graph of size 3). 

**Output**  

Returns True if the graph is unit 2-interval, False if it is not but it is K_{1,5}-free and prints out "has a 5 claw, continue" if it contains an induced K_{1,5} (then we know directly that it is not a unit 2-interval graph). 

