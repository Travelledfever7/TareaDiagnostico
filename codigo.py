from multiprocessing import Process, Queue
import time
 
def proceso1(name, priority, cola):
    print(f' El nombre del proceso es {name} y su prioridad es {priority}')
    cola.put(f'El proceso {name} ha terminado')
    time.sleep(2)

def main():
    q = Queue()
    for i in range(5):
        
        process = Process(target=proceso1, args=(f"Proceso {i+1}",f"prioridad {i+1}",q,))
        process.start()
        process.join()
        result = q.get()
        print(result)
        if not process.is_alive:
            print(result)
            
    if q.empty:
        print('La cola esta vacia')
    
if __name__ == '__main__': 
    main()
