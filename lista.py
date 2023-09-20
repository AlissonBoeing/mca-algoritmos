import time
class List:
    
    def __init__(self):
        self.l_5h = []
        self.l_1t = []
        self.l_5t = []
        self.l_10t = []

    def print_info(self, n, swaps, comps, duration):
        print()
        print(f"### {n} entries ###".format())
        print("swaps: ", swaps)
        print("comps: ", comps)
        print("duration: ", duration)

    def measure_selection_sort(self):
        print("#### selection sort ####")
        self.create_list()

        _, ss_swaps_5h, ss_comps_5h, ss_duration_ms_5h = self.selection_sort(self.l_5h.copy()) 
        self.print_info(len(self.l_5h),ss_swaps_5h, ss_comps_5h, ss_duration_ms_5h)
            
        _, ss_swaps_1t, ss_comps_1t, ss_duration_ms_1t = self.selection_sort(self.l_1t.copy()) 
        self.print_info(len(self.l_1t),ss_swaps_1t, ss_comps_1t, ss_duration_ms_1t)

        _, ss_swaps_5t, ss_comps_5t, ss_duration_ms_5t = self.selection_sort(self.l_5t.copy()) 
        self.print_info(len(self.l_5t),ss_swaps_5t, ss_comps_5t, ss_duration_ms_5t)
       
        _ , ss_swaps_10t, ss_comps_10t, ss_duration_ms_10t = self.selection_sort(self.l_10t.copy()) 
        self.print_info(len(self.l_10t),ss_swaps_10t, ss_comps_10t, ss_duration_ms_10t)
   
    def create_list(self):
        with open("data/saidaOrdenada.txt", "r") as file:
            index = 0
            for line in file:
                parts = line.strip().split(',')
                if (index < 500):
                    self.l_5h.append(int(parts[0]))
                if(index < 1000):
                    self.l_1t.append(int(parts[0]))
                if(index < 5000):
                    self.l_5t.append(int(parts[0]))
                self.l_10t.append(int(parts[0]))
                index = index+1

    def selection_sort(self, list):
        comps = 0
        swaps = 0
        duration = 0
        start_time = time.time()
        for i in range(len(list)):
            lower_idx = i
            for j in range(i+1, len(list)):
                comps = comps + 1
                if (list[j] < list[lower_idx]):
                    lower_idx = j 
            swaps = swaps + 1
            lower = list[i]
            list[i] = list[lower_idx]
            list[lower_idx] = lower
        duration = time.time() - start_time
        return list, swaps, comps, duration*1000.0

    def quick_sort(self, list):
        
        return list, swaps, comps, duration*1000.0
    
    def insertion_sort(self, list):
        
        return list, swaps, comps, duration*1000.0

    def heap_sort(self, list):
        
        return list, swaps, comps, duration*1000.0

    def shell_sort(self, list):
        
        return list, swaps, comps, duration*1000.0
