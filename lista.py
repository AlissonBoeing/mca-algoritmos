import time
import numpy as np
class List:
    
    def __init__(self):
        self.l_5h = []
        self.l_1t = []
        self.l_5t = []
        self.l_10t = []
        self.create_list()

    def print_info(self, n, swaps, comps, duration):
        print()
        print(f"### {n} entries ###".format())
        print("swaps: ", swaps)
        print("comps: ", comps)
        print("duration: ", duration)

    def measure_quick_sort(self):
        print("#### quick sort ####")

        duration_list = []
        for i in range(5):
            sl, ss_swaps_5h, ss_comps_5h, ss_duration_ms_5h = self.quick_sort(self.l_5h.copy(), 0, 499) 
            duration_list.append(ss_duration_ms_5h)
        ss_duration_ms_5h = np.mean(duration_list)
        self.print_info(len(self.l_5h), ss_swaps_5h, ss_comps_5h, ss_duration_ms_5h)

        duration_list = []
        for i in range(5):
            sl, ss_swaps_1t, ss_comps_1t, ss_duration_ms_1t = self.quick_sort(self.l_1t.copy(), 0, 999) 
            duration_list.append(ss_duration_ms_1t)
        ss_duration_ms_1t = np.mean(duration_list)
        self.print_info(len(self.l_1t), ss_swaps_1t, ss_comps_1t, ss_duration_ms_1t)

        duration_list = []
        for i in range(5):
            sl, ss_swaps_5t, ss_comps_5t, ss_duration_ms_5t = self.quick_sort(self.l_5t.copy(), 0, 4999) 
            duration_list.append(ss_duration_ms_5t)
        ss_duration_ms_5t = np.mean(duration_list)
        self.print_info(len(self.l_5t), ss_swaps_5t, ss_comps_5t, ss_duration_ms_5t)

        duration_list = []
        for i in range(5):
            sl, ss_swaps_10t, ss_comps_10t, ss_duration_ms_10t = self.quick_sort(self.l_10t.copy(), 0, 9999) 
            duration_list.append(ss_duration_ms_10t)
        ss_duration_ms_10t = np.mean(duration_list)
        self.print_info(len(self.l_10t), ss_swaps_10t, ss_comps_10t, ss_duration_ms_10t)


    def measure_selection_sort(self):
        print("#### selection sort ####")
        
        _, ss_swaps_5h, ss_comps_5h, ss_duration_ms_5h = self.selection_sort(self.l_5h.copy()) 
        self.print_info(len(self.l_5h),ss_swaps_5h, ss_comps_5h, ss_duration_ms_5h)
            
        _, ss_swaps_1t, ss_comps_1t, ss_duration_ms_1t = self.selection_sort(self.l_1t.copy()) 
        self.print_info(len(self.l_1t),ss_swaps_1t, ss_comps_1t, ss_duration_ms_1t)

        _, ss_swaps_5t, ss_comps_5t, ss_duration_ms_5t = self.selection_sort(self.l_5t.copy()) 
        self.print_info(len(self.l_5t),ss_swaps_5t, ss_comps_5t, ss_duration_ms_5t)
       
        _ , ss_swaps_10t, ss_comps_10t, ss_duration_ms_10t = self.selection_sort(self.l_10t.copy()) 
        self.print_info(len(self.l_10t),ss_swaps_10t, ss_comps_10t, ss_duration_ms_10t)
   
    def create_list(self):
        with open("data/saidaAleatoria.txt", "r") as file:
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
        dur_list = []
        inner_list = []
        for ii in range(5):
            inner_list = list.copy()
            comps = 0
            swaps = 0
            duration = 0
            start_time = time.time()
            for i in range(len(inner_list)):
                lower_idx = i
                for j in range(i+1, len(inner_list)):
                    comps = comps + 1
                    if (inner_list[j] < inner_list[lower_idx]):
                        lower_idx = j 
                swaps = swaps + 1
                lower = inner_list[i]
                inner_list[i] = inner_list[lower_idx]
                inner_list[lower_idx] = lower
            duration = time.time() - start_time
            dur_list.append(duration)
        duration = np.mean(dur_list)
        list = inner_list
        return list, swaps, comps, duration*1000

    def quick_sort(self, list, left, right):
            comps = 0
            swaps = 0
            duration = 0
            start_time = time.time()
            def partition(list, left, right):
                nonlocal comps, swaps
                pivot = list[right]
                i = left - 1
                
                for j in range(left, right):
                    comps = comps + 1
                    if (list[j] < pivot):
                        i = i + 1
                        list[i], list[j] = list[j], list[i]
                        swaps = swaps + 1
                comps = comps + 1
                if (pivot < list[i + 1]):
                    list[i+1], list[right] = list[right], list[i+1]
                    swaps = swaps + 1
                return i + 1

            if (left < right):
                part = partition(list, left, right)
                self.quick_sort(list, left, part - 1)
                self.quick_sort(list, part + 1, right)
            duration = time.time() - start_time
            return list, swaps, comps, duration*1000

    
    def insertion_sort(self, list):
        
        return list, swaps, comps, duration*1000.0

    def heap_sort(self, list):
        
        return list, swaps, comps, duration*1000.0

    def shell_sort(self, list):
        
        return list, swaps, comps, duration*1000.0
