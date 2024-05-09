import math

def gps_to_cartesian(lat, lon, ref_lat, ref_lon):
    earth_radius = 6371000  # meters
    lat_diff = math.radians(lat - ref_lat)
    lon_diff = math.radians(lon - ref_lon)
    x = earth_radius * lon_diff * math.cos(math.radians(ref_lat))
    y = earth_radius * lat_diff
    return x, y

def calculate_bearing_cartesian(pointA, pointB):
    if (type(pointA) != tuple) or (type(pointB) != tuple):
        raise TypeError("Only tuples are supported as arguments")

    deltaX = pointB[0] - pointA[0]
    deltaY = pointB[1] - pointA[1]

    # Calculate the angle using the atan2 function
    angle = math.atan2(deltaY, deltaX)

    # Convert from radians to degrees
    angle_degrees = math.degrees(angle)

    # Normalize the angle to be between 0 and 360 degrees
    compass_bearing = (angle_degrees + 360) % 360

    return compass_bearing

# Points definition
pointA = (0, 0)
pointB = (5, 5)
pointC = (0, 5)
pointD = (2.5, 2.5)

# Calculate bearings
bearing_AB = calculate_bearing_cartesian(pointA, pointB)
bearing_AC = calculate_bearing_cartesian(pointA, pointC)
bearing_AD = calculate_bearing_cartesian(pointA, pointD)

(bearing_AB, bearing_AC, bearing_AD)
