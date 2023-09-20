class List:

    def __init__(self):
        self.list = []
        self.changes = 0
        self.comps = 0
        self.duration = 0
    
    def selection_sort(self, list):
        self.list = list
        return self.list, self.changes, self.comps, self.duration

    def quick_sort(self, list):
        self.list = list
        return self.list, self.changes, self.comps, self.duration
    
    def insertion_sort(self, list):
        self.list = list
        return self.list, self.changes, self.comps, self.duration

    def heap_sort(self, list):
        self.list = list
        return self.list, self.changes, self.comps, self.duration

    def shell_sort(self, list):
        self.list = list
        return self.list, self.changes, self.comps, self.duration
