# python_samples
My Python sample code that shows some functionalities:

### multiprocessing
You can parallelize tasks using the multiprocessing module. Each Process will run on an available cpu. In this example I created a list of permutations and pass the permutation list as argument with CPU id, and the variable to determine the number of elements to process at each cpu. In each process, a work is done and the main process waits until all processes complete their work. This simple snippet works well if your processes don't need to communicate. In most of my work, this small snippet speeds up the execution time by available number of CPUs (4 in many cases). I recommend using Pipe or Queue if your processes need any kind of communication. 
