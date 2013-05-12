import random, math

def main():
    """Estimates the value of pi by generating random points in the unit square
    and calculating the ratio of those points that lie within the unit circle."""
    print("Enter number of trials desired.")
    num_trials = int(input())
    result = run_trials(num_trials)
    print("Estimated value of pi with ", num_trials, " trials: ", result)

def run_trials(num_trials):
    """Runs a set number of trials and estimates the value of pi."""
    in_circle = 0
    for _ in range(num_trials):
        # Generates random floats in [0,1) and scales them to [-1,1)
        point_x = -1 + (2 * random.random()) 
        point_y = -1 + (2 * random.random())
        point = (point_x, point_y)
        hit = distance(point) <= 1
        in_circle += int(hit) # 1 iff point is in circle
    return (4*in_circle)/num_trials
    
    
def distance(point):
    """Computes the distance of the point, a tuple of length 2, from the origin."""
    return math.sqrt(point[0]**2 + point[1]**2)

main()
