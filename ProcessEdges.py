import arcpy
edges_table = r'C:\Users\jame9353\Documents\ArcGIS\Projects\Defense and Intel Forum\GraphAnalysis.gdb\edges_table'
edges = r'C:\Users\jame9353\Documents\ArcGIS\Projects\Defense and Intel Forum\GraphAnalysis.gdb\edges'
fields = ['OBJECTID', 'SHAPE@', 'carrier', 'distance', 'travel_time', 'segment', 'betweenness', 'shape_1']
cursor = arcpy.da.InsertCursor(edges, fields)
for row in arcpy.da.SearchCursor('edges_table', "*"):
    object_id = row[0]
    carrier = row[2]
    distance = row[3]
    travel_time = row[4]
    segment = row[5]
    betweenness = row[6]
    flight_shape = row[7]
    origin_long = row[7].split("]")[0].split("[")[2].split(',')[0]
    origin_lat = row[7].split("]")[0].split("[")[2].split(',')[1]
    destination_long = row[7].split("]")[1].split("[")[1].split(',')[0]
    destination_lat = row[7].split("]")[1].split("[")[1].split(',')[1]
    feature = [[origin_long, origin_lat], [destination_long, destination_lat]]
    features = "there were once points here..."
    line = arcpy.Polyline(arcpy.Array([arcpy.Point(*coords) for coords in feature]))
    iRow = [object_id, line, carrier, distance, travel_time, segment, betweenness, features]
    cursor.insertRow(iRow)

del cursor