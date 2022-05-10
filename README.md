# pyrunplan
# Create run plan based on Roche plan (0-15-20-15-0-35-15)
#
# inputs:
## start miles: start miles for the plan. Default to 20 miles. Take average of last 4-6 weeks of running.
## double runs after: mileage threshold when we start double run days
## double run day: which day to do double runs, assumes 1 double run day a week.
## number of weeks to plan. Default 52.
## number of build weeks. Default 3
## number of recovery weeks. Default 1
## build increase. Default 10%
## recovery decrease. Default 85%
## max time
## min time
## friday run threshold
## Show week DATE (08/05 for instance)
## Show week number (18 week plan should show weeks 1..18)

# [
#     [0, 36, 48, 36, 0, 84, 36],
#     [0, 40, 53, 40, 0, 92, 40],
#     [0, 44, 58, 44, 0, 102, 44],d
#     [0, 37, 49, 37, 0, 86, 37],
#     [0, 41, 54, 41, 0, 95, 41]
# ]