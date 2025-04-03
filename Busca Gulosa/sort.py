import numpy as np

class Sort:
    def __init__(self, size):
        self.size = size
        self.cities = np.empty(self.size, dtype=object)
        self.last_position = -1
        
    def list(self):
        if self.last_position == -1:
            print("Tá Vazio.")
        else:
            for index in range(self.last_position + 1):
                print(f"{index} -> {self.cities[index].label}")
                print(f"\t Heuristica: {self.cities[index].target_distance}")                
                
    def insert(self, value):
        if self.last_position == (self.size - 1):
            print("Cabo o espaço.")
            return
        
        position = 0
        for position in range(self.last_position + 1):
            if self.cities[position].target_distance > value.target_distance:
                break
            
            if position == self.last_position:
                position += 1
        
        last_position = self.last_position
        while last_position >= position:
            next_positon = last_position + 1
            self.cities[next_positon] = self.cities[last_position]
            last_position -= 1
            
        self.cities[position] = value
        self.last_position += 1
