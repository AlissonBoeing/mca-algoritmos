import time
import numpy as np
import sys

class List:
    NUM_OF_ITERATIONS = 5

    def __init__(self):
        self.l_5h = []
        self.l_1t = []
        self.l_5t = []
        self.l_10t = []
        self.create_list()

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

    def print_info(self, n, swaps, comps, duration):
        print()
        print(f"### {n} entries ###".format())
        print("swaps: ", swaps)
        print("comps: ", comps)
        print("duration: ", duration)
    
    def measure_shell_sort(self):
        print("#### shell sort ####")

        _, swaps_5h, comps_5h, duration_ms_5h = self.shell_sort(self.l_5h.copy()) 
        self.print_info(len(self.l_5h),swaps_5h, comps_5h, duration_ms_5h)
            
        _, swaps_1t, comps_1t, duration_ms_1t = self.shell_sort(self.l_1t.copy()) 
        self.print_info(len(self.l_1t),swaps_1t, comps_1t, duration_ms_1t)

        _, swaps_5t, comps_5t, duration_ms_5t = self.shell_sort(self.l_5t.copy()) 
        self.print_info(len(self.l_5t),swaps_5t, comps_5t, duration_ms_5t)
       
        _ , swaps_10t, comps_10t, duration_ms_10t = self.shell_sort(self.l_10t.copy()) 
        self.print_info(len(self.l_10t),swaps_10t, comps_10t, duration_ms_10t)

    def measure_quick_sort(self):
        print("#### quick sort ####")

        duration_list = []
        for i in range(self.NUM_OF_ITERATIONS):
            sl, swaps_5h, comps_5h, duration_ms_5h = self.quick_sort(self.l_5h.copy(), 0, 499) 
            duration_list.append(duration_ms_5h)
        duration_ms_5h = np.mean(duration_list)
        self.print_info(len(self.l_5h), swaps_5h, comps_5h, duration_ms_5h)

        duration_list = []
        for i in range(self.NUM_OF_ITERATIONS):
            sl, swaps_1t, comps_1t, duration_ms_1t = self.quick_sort(self.l_1t.copy(), 0, 999) 
            duration_list.append(duration_ms_1t)
        duration_ms_1t = np.mean(duration_list)
        self.print_info(len(self.l_1t), swaps_1t, comps_1t, duration_ms_1t)

        duration_list = []
        for i in range(self.NUM_OF_ITERATIONS):
            sl, swaps_5t, comps_5t, duration_ms_5t = self.quick_sort(self.l_5t.copy(), 0, 4999) 
            duration_list.append(duration_ms_5t)
        duration_ms_5t = np.mean(duration_list)
        self.print_info(len(self.l_5t), swaps_5t, comps_5t, duration_ms_5t)

        duration_list = []
        for i in range(self.NUM_OF_ITERATIONS):
            sl, swaps_10t, comps_10t, duration_ms_10t = self.quick_sort(self.l_10t.copy(), 0, 9999) 
            duration_list.append(duration_ms_10t)
        duration_ms_10t = np.mean(duration_list)
        self.print_info(len(self.l_10t), swaps_10t, comps_10t, duration_ms_10t)

    def measure_selection_sort(self):
        print("#### selection sort ####")
        
        _, swaps_5h, comps_5h, duration_ms_5h = self.selection_sort(self.l_5h.copy()) 
        self.print_info(len(self.l_5h),swaps_5h, comps_5h, duration_ms_5h)
            
        _, swaps_1t, comps_1t, duration_ms_1t = self.selection_sort(self.l_1t.copy()) 
        self.print_info(len(self.l_1t),swaps_1t, comps_1t, duration_ms_1t)

        _, swaps_5t, comps_5t, duration_ms_5t = self.selection_sort(self.l_5t.copy()) 
        self.print_info(len(self.l_5t),swaps_5t, comps_5t, duration_ms_5t)
       
        _ , swaps_10t, comps_10t, duration_ms_10t = self.selection_sort(self.l_10t.copy()) 
        self.print_info(len(self.l_10t),swaps_10t, comps_10t, duration_ms_10t)

    def measure_insertion_sort(self):
        print("#### insertion sort ####")
        
        _, swaps_5h, comps_5h, duration_ms_5h = self.insertion_sort(self.l_5h.copy()) 
        self.print_info(len(self.l_5h),swaps_5h, comps_5h, duration_ms_5h)
            
        _, swaps_1t, comps_1t, duration_ms_1t = self.insertion_sort(self.l_1t.copy()) 
        self.print_info(len(self.l_1t),swaps_1t, comps_1t, duration_ms_1t)

        _, swaps_5t, comps_5t, duration_ms_5t = self.insertion_sort(self.l_5t.copy()) 
        self.print_info(len(self.l_5t),swaps_5t, comps_5t, duration_ms_5t)
       
        _ , swaps_10t, comps_10t, duration_ms_10t = self.insertion_sort(self.l_10t.copy()) 
        self.print_info(len(self.l_10t),swaps_10t, comps_10t, duration_ms_10t)
   
    def measure_merge_sort(self):
        print("#### merge sort ####")
        
        duration_list = []
        for i in range(self.NUM_OF_ITERATIONS):
            sl, swaps_5h, comps_5h, duration_ms_5h = self.merge_sort(self.l_5h.copy()) 
            duration_list.append(duration_ms_5h)
        duration_ms_5h = np.mean(duration_list)
        self.print_info(len(self.l_5h), swaps_5h, comps_5h, duration_ms_5h)

        duration_list = []
        for i in range(self.NUM_OF_ITERATIONS):
            sl, swaps_1t, comps_1t, duration_ms_1t = self.merge_sort(self.l_1t.copy()) 
            duration_list.append(duration_ms_1t)
        duration_ms_1t = np.mean(duration_list)
        self.print_info(len(self.l_1t), swaps_1t, comps_1t, duration_ms_1t)

        duration_list = []
        for i in range(self.NUM_OF_ITERATIONS):
            sl, swaps_5t, comps_5t, duration_ms_5t = self.merge_sort(self.l_5t.copy()) 
            duration_list.append(duration_ms_5t)
        duration_ms_5t = np.mean(duration_list)
        self.print_info(len(self.l_5t), swaps_5t, comps_5t, duration_ms_5t)

        duration_list = []
        for i in range(self.NUM_OF_ITERATIONS):
            sl, swaps_10t, comps_10t, duration_ms_10t = self.merge_sort(self.l_10t.copy()) 
            duration_list.append(duration_ms_10t)
        duration_ms_10t = np.mean(duration_list)
        self.print_info(len(self.l_10t), swaps_10t, comps_10t, duration_ms_10t)
        
    def selection_sort(self, list):
        comps = 0
        swaps = 0
        duration = 0
        dur_list = []
        inner_list = []
        for ii in range(self.NUM_OF_ITERATIONS):
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
            sys.setrecursionlimit(11000)
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
        comps = 0
        swaps = 0
        duration = 0
        dur_list = []
        inner_list = []
        for i in range(self.NUM_OF_ITERATIONS):
            comps = 0
            swaps = 0
            duration = 0
            inner_list = list.copy()
            n = len(inner_list)
            start_time = time.time()

            for j in range(1, n):
                chave = inner_list[j]
                i = j - 1
                while i >= 0:
                    comps = comps + 1
                    if(inner_list[i] > chave):
                        inner_list[i + 1] = inner_list[i]
                        swaps = swaps + 1
                    else:
                        break    
                    i = i - 1

                inner_list[i + 1] = chave
            
            duration = time.time() - start_time
            dur_list.append(duration)
        list = inner_list
        duration = np.mean(dur_list)

        return list, swaps, comps, duration*1000.0

    def merge_sort(self, list):
        comps = 0
        swaps = 0
        duration = 0

        start_time = time.time()

        def merge(list, left, middle, right):
            nonlocal comps, swaps
            n1 = middle - left + 1
            n2 = right - middle

            L = list[left:left + n1]
            R = list[middle + 1:middle + 1 + n2]

            i = j = 0
            k = left

            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    list[k] = L[i]
                    i += 1
                else:
                    list[k] = R[j]
                    j += 1
                    swaps += 1
                k += 1
                comps += 1

            while i < n1:
                list[k] = L[i]
                i += 1
                k += 1

            while j < n2:
                list[k] = R[j]
                j += 1
                k += 1

        def merge_sort_recursive(list, left, right):
            if left < right:
                middle = (left + right) // 2

                merge_sort_recursive(list, left, middle)
                merge_sort_recursive(list, middle + 1, right)

                merge(list, left, middle, right)

        merge_sort_recursive(list, 0, len(list) - 1)

        duration = time.time() - start_time

        return list, swaps, comps, duration*1000.0

    def shell_sort(self, list):
        comps = 0
        swaps = 0
        duration = 0
        dur_list = []
        inner_list = []
        for i in range(self.NUM_OF_ITERATIONS):
            comps = 0
            swaps = 0
            duration = 0
            inner_list = list.copy()
            n = len(inner_list)
            gap = n >> 1
            start_time = time.time()
            while(gap > 0):
                for i in range(gap, n):
                    temp = inner_list[i]
                    j = i
                    while((j >= gap) and (inner_list[j-gap] > temp)):
                        comps = comps + 1
                        inner_list[j] = inner_list[j-gap]
                        swaps = swaps + 1
                        j = j - gap 
                    inner_list[j] = temp 
                    swaps = swaps + 1
                gap = gap >> 1
            duration = time.time() - start_time
            dur_list.append(duration)
        list = inner_list
        duration = np.mean(dur_list)
        return list, swaps, comps, duration*1000.0
