from dataclasses import dataclass
from typing import List

from abc import abstractmethod


[[
[4, 4, 2, 2],
[2, 4, 2, 0],
[0, 2, 2, 2],
[4, 4, 4, 0]]]



@dataclass
class ParkingFloor:
    def __init__(self, floor : int, floorPlan : List[List]) -> None:
        self.floor = floor
        self.floorPlan = floorPlan

        self.row = len(floorPlan)
        self.col = len(floorPlan[0])

        self.reserved = [ [ False ] * self.col for _ in range( self.row ) ] 

    
    def park( self, vechileType ):
        
        for i in range(len(self.floorPlan)):
            for j in range( self.floorPlan[i] ) :
                if j == vechileType and not self.reserved[i][j]:
                    self.reserved[i][j] = True
                    return f"{self.floor} - {i} - {j}" 


        

    
    

class statergies:
    @abstractmethod
    def park( floors, vechileType ):
        pass

class lowestSpotAvailable( statergies ):
    def __init__(self) -> None:
        pass

    def park(floors, vechileType):
        return super().park(floors, vechileType)

class maximunFreeSlots( statergies ):
    def __init__(self) -> None:
        pass

    def park(floors, vechileType):
        return super().park(floors, vechileType)
    
class ParkingManager:
    def __init__(self) -> None:
        self.statergies = [ lowestSpotAvailable, maximunFreeSlots ]

    def park( self, statergy, floors, vechileType ):
        self.statergies[ statergy ].park( floors, vechileType )


class SearchManager:

    def __init__(self) -> None:
        pass

@dataclass
class Solution:

    def __init__(self, parking : List[List[List]] ) -> None:
        self.vechileTypes = [2,4]
        self.floors = [ ParkingFloor( i, floorPlan ) for i,floorPlan in enumerate(parking) ]
        self.parkingManager = ParkingManager()
        self.searchManager  = SearchManager()

    def park( self, vechileType, vechileId, ticketId, statergy ):
        spotId =  self.statergies[ statergy ].park()
        if spotId:
            
    



def run():
    pass

if __name__ == '__main__':
    run()