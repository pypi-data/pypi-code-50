import osmnx as ox
import geopy.distance


def get_distance_graph(df, dist):


    middle_loc = ((df['gps_latitude'].max() + df['gps_latitude'].min()) / 2,
                  (df['gps_longitude'].max() + df['gps_longitude'].min()) / 2)

    radius = max(geopy.distance.distance((df['gps_latitude'].max(), df['gps_longitude'].mean()),
                                         (df['gps_latitude'].min(), df['gps_longitude'].mean())).m,
                 geopy.distance.distance((df['gps_latitude'].mean(), df['gps_longitude'].max()),
                                         (df['gps_latitude'].mean(), df['gps_longitude'].min())).m)

    try:
        print('extracting graph...')
        return ox.graph_from_point(middle_loc, distance=radius + dist, network_type='drive', simplify=False)

    except:
        print(middle_loc, radius + dist)
        print('Failed to retrieve graph')
        return None


