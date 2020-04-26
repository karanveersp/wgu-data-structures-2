from simulation import simulation, random_scheduler
import sys

def load_data(filename):
    with open(filename, "rt") as infile:
        num_processors = int(infile.readline().replace("\n", ""))
        processes = list(map(lambda line: int(line.replace("\n", "")), infile.readlines()))
    return num_processors, processes

def shortest_process_first_scheduler(processes, processors):
    return processes.index(min(processes)), processors.index(min(processors))

def first_come_first_served_scheduler(processes, processors):
    return 0, processors.index(min(processors))

if __name__ == "__main__":

    num_processors, processes = load_data(sys.argv[1])
                
    print("SIM 1: random scheduler")            
    processes_copy = [ x for x in processes ]
    final_time, total_wait_time, max_wait_time = simulation(num_processors, processes_copy, random_scheduler)
    print('%20s: %d' % ('Final Time', final_time))
    print('%20s: %d' % ('Total Wait Time', total_wait_time))
    print('%20s: %d' % ('Max Wait time', max_wait_time))
    print('%20s: %0.2f' % ('Average Wait Time', total_wait_time / num_processors))

    print()
    print("SIM 2: first-come-first-served scheduler")            
    processes_copy = [ x for x in processes ]
    final_time, total_wait_time, max_wait_time = simulation(num_processors, processes_copy, first_come_first_served_scheduler)
    print('%20s: %d' % ('Final Time', final_time))
    print('%20s: %d' % ('Total Wait Time', total_wait_time))
    print('%20s: %d' % ('Max Wait time', max_wait_time))
    print('%20s: %0.2f' % ('Average Wait Time', total_wait_time / num_processors))

    print()
    print("SIM 3: shortest-process-first scheduler")            
    processes_copy = [ x for x in processes ]
    final_time, total_wait_time, max_wait_time = simulation(num_processors, processes_copy, shortest_process_first_scheduler)
    print('%20s: %d' % ('Final Time', final_time))
    print('%20s: %d' % ('Total Wait Time', total_wait_time))
    print('%20s: %d' % ('Max Wait time', max_wait_time))
    print('%20s: %0.2f' % ('Average Wait Time', total_wait_time / num_processors))