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

        self.freeSpots = self.row * self.col
    
    def park( self, vechileType ):
        
        for i in range(len(self.floorPlan)):
            for j in range( self.floorPlan[i] ) :
                if j == vechileType and not self.reserved[i][j]:
                    self.reserved[i][j] = True
                    self.freeSpots -=1
                    return f"{self.floor} - {i} - {j}" 


    def remove( self, positions ):
        i,j = map( int, map( lambda x:x.strip(), positions.split('-') ) )
        self.reserved[ i ][ j ] = False
        self.freeSpots += 1


class statergies:
    @abstractmethod
    def park( floors, vechileType ):
        pass

class lowestSpotAvailable( statergies ):
    def park(floors, vechileType):
        
        for floor in range( len( floors ) ):
            spotId = floors[ floor ].park( vechileType )
            if spotId:
                return spotId

class maximunFreeSlots( statergies ):

    def park(floors, vechileType):
        
        floorWithMaxAvailableSlots = -1
        maxAvailableSlots = -1

        for floor in range( len( floors ) ):
            if floors[ floor ].freeSpots > maxAvailableSlots:
                maxAvailableSlots = floors[ floor ].freeSpots
                floorWithMaxAvailableSlots = floor

        floors[ floorWithMaxAvailableSlots ].park( vechileType )
    
class ParkingManager:
    def __init__(self) -> None:
        self.statergies = [ lowestSpotAvailable, maximunFreeSlots ]

    def park( self, statergy, floors, vechileType ):
        self.statergies[ statergy ].park( floors, vechileType )


class SearchManager:

    def __init__(self) -> None:
        self.cache = {}

    def storeVechileDetails( self, spotId, vechileId, ticketId  ):
        self.cache[ vechileId ] = spotId
        self.cache[ ticketId ]  = spotId

    def findVechile( self, vechileOrTicketId ):
        return self.cache.get( vechileOrTicketId, '' )
    
    def removeVechileDetails( self,  vechileId, ticketId  ):
        del self.cache[ vechileId ]
        del self.cache[ ticketId ]

@dataclass
class Solution:

    def __init__(self, parking : List[List[List]] ) -> None:
        self.vechileTypes = [2,4]
        self.floors = [ ParkingFloor( i, floorPlan ) for i,floorPlan in enumerate(parking) ]
        self.parkingManager = ParkingManager()
        self.searchManager  = SearchManager()

    def park( self, vechileType, vechileId, ticketId, statergy ):
        spotId =  self.parkingManager.park( statergy, self.floors, vechileType )
        if spotId:
            self.searchManager.storeVechileDetails( spotId, vechileId, ticketId )
            return spotId
        
    def remove( self,  vechileId, ticketId  ):
        spotId = self.searchManager.findVechile( vechileId, ticketId )
        if spotId:
            floor, positions = spotId.split('-')
            self.floors[ floor ].remove( positions )
        return 

def run():
    pass

if __name__ == '__main__':
    run()