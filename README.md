Pi-Estimator
============

Performs numerical estimation of pi. The estimation is performed by generating a set of points at random in the unit square and then determining the ratio of those points that lie within the unit circle.  

The logic of the estimation is that the ratio of the area of a circle inscribed within a square to the area of that square is pi/4. Thus, the value displayed to the user is 4*(n/N), where N is the number of trials and n is the number of points within the unit circle.  

To run, execute  

    python3 pi_estimate.py

and enter the number of trials desired.
