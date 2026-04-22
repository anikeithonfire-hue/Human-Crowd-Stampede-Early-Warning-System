import numpy as np
 
# calculates a danger score for each cell in the grid
# and for the overall venue
#
# danger scoring logic
# --------------------
# density alone isnt enough, rate of change matters too
# a zone at 5/sqm thats increasing fast is more dangerous
# than a zone at 5.5/sqm thats stable
#
# danger score per cell = (density_score * 0.7) + (rate_score * 0.3)
# both normalised to 0-100
#
# overall danger = weighted avg with highest cells getting more weight
 
# density thresholds for scoring
DENSITY_SAFE      = 2.0    # below this = score 0
DENSITY_WARNING   = 4.0    # moderate concern
DENSITY_DANGER    = 6.0    # serious danger
DENSITY_CRITICAL  = 7.5    # stampede imminent
 
 
def density_to_score(d):
    # converts density value to 0-100 score
    # piecewise linear mapping
    if d <= DENSITY_SAFE:
        return 0.0
    elif d <= DENSITY_WARNING:
        return 25.0 * (d - DENSITY_SAFE) / (DENSITY_WARNING - DENSITY_SAFE)
    elif d <= DENSITY_DANGER:
        return 25.0 + 50.0 * (d - DENSITY_WARNING) / (DENSITY_DANGER - DENSITY_WARNING)
    elif d <= DENSITY_CRITICAL:
        return 75.0 + 20.0 * (d - DENSITY_DANGER) / (DENSITY_CRITICAL - DENSITY_DANGER)
    else:
        return min(100.0, 95.0 + 5.0 * (d - DENSITY_CRITICAL))
 