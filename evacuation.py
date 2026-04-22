import numpy as np
 
# figures out which direction people should move to escape
# from a dangerous zone
#
# logic is simple but works -
# look at all 4 neighbours of the hotspot cell
# recommend moving toward the one with lowest danger score
# if all neighbours are also dangerous, recommend the edges
# (edges = exits in a real venue)
 
DIRECTIONS = {
    "north": (-1,  0),
    "south": ( 1,  0),
    "east" : ( 0,  1),
    "west" : ( 0, -1),
}
 
 
class EvacuationAdvisor:
 
    def __init__(self, grid_size=10):
        self.grid_size         = grid_size
        self.recommended_zones = []   # list of safe zone coordinates
        self.direction_msg     = "All zones normal"
 
    # -------------------------------------------------
    def recommend(self, danger_grid, hotspot):
        d    = np.array(danger_grid)
        r, c = hotspot
 
        if d[r, c] < 25:
            self.direction_msg     = "All zones normal"
            self.recommended_zones = []
            return
 
        # check all 4 neighbours
        options = {}
        for name, (dr, dc) in DIRECTIONS.items():
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.grid_size and 0 <= nc < self.grid_size:
                options[name] = d[nr, nc]
 
        if not options:
            self.direction_msg = "Hotspot at corner, move to nearest exit"
            return
 