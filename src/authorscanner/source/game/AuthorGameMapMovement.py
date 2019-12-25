import os
import re
from authorscanner import AuthorScanRepository
from authortrackwriter import AuthorGraphResultFile


result_path_name = AuthorGraphResultFile.ResultFile.WORLDMAP


def appendWorldmapArea(worldmap_spot_mapids, cur_spot):
    worldmap_spot_mapids.append(cur_spot)

    cur_spot = [7777777, 7777777, []]
    return cur_spot


def readWorldmapFile(worldmap_file_path):
    ml_st_p = re.compile('^[ ]{2}<imgdir name="MapList">')
    ml_en_p = re.compile('^[ ]{2}</imgdir>')

    ml_node_st_p = re.compile('^[ ]{4}<imgdir name="')
    ml_node_en_p = re.compile('^[ ]{4}</imgdir>')

    ml_node_item_spot_p = re.compile('^[ ]{6}<vector name="spot" x="([-+]?\d+)" y="([-+]?\d+)"/>')

    ml_node_item_mapno_st_p = re.compile('^[ ]{6}<imgdir name="mapNo">')
    ml_node_item_mapno_en_p = re.compile('^[ ]{6}</imgdir>')

    ml_node_item_mapno_item_p = re.compile('^[ ]{8}<int name="(\d+)" value="(\d+)"/>')

    worldmap_spot_mapids = []
    cur_spot_mapids = appendWorldmapArea(worldmap_spot_mapids, None)
    worldmap_spot_mapids.clear()

    file = open(worldmap_file_path, 'r')
    state = 0
    for line in file.readlines():
        if state == 0:
            ml_m = ml_st_p.match(line)
            if ml_m is not None:
                state += 1

        elif state == 1:
            ml_m = ml_node_st_p.match(line)
            if ml_m is not None:
                state += 1
            else:
                ml_m = ml_en_p.match(line)   # finished reading map points
                if ml_m is not None:
                    state -= 1

        elif state == 2:
            ml_m = ml_node_item_spot_p.match(line)  # reading node data
            if ml_m is not None:
                cur_spot_mapids[0] = int(ml_m.group(1))
                cur_spot_mapids[1] = int(ml_m.group(2))
            else:
                ml_m = ml_node_item_mapno_st_p.match(line)
                if ml_m is not None:
                    state += 1
                else:
                    ml_m = ml_node_en_p.match(line)
                    if ml_m is not None:
                        cur_spot_mapids = appendWorldmapArea(worldmap_spot_mapids, cur_spot_mapids)
                        state -= 1

        elif state == 3:
            ml_m = ml_node_item_mapno_item_p.match(line)
            if ml_m is not None:
                cur_spot_mapids[2].append(int(ml_m.group(2)))
            else:
                ml_m = ml_node_item_mapno_en_p.match(line)
                if ml_m is not None:
                    state -= 1

    file.close()
    return worldmap_spot_mapids


def loadWorldmapSpots():
    worldmap_dir_path = scanner.wz_path + '/Map.wz/WorldMap'

    worldmap_mapids = {}
    for file in os.listdir(worldmap_dir_path):
        worldmap_file_path = worldmap_dir_path + '/' + file
        worldmap_mapids[file[0:file.find('.')]] = readWorldmapFile(worldmap_file_path)

    return worldmap_mapids


def locateWorldmapMapidSpots(worldmap_name_spots):
    worldmap_mapid_spots = {}

    print('wmap')
    for worldmap_name, worldmap_spot_mapids in worldmap_name_spots.items():
        print('  ' + worldmap_name + ' , having ' + str(worldmap_spot_mapids))
    print('´´´´')

    for worldmap_name, worldmap_spot_mapids in worldmap_name_spots.items():
        for worldmap_spot in worldmap_spot_mapids:
            spot = (worldmap_spot[0], worldmap_spot[1])

            for mapid in worldmap_spot[2]:
                if mapid not in worldmap_mapid_spots:
                    worldmap_mapid_area = {}
                    worldmap_mapid_spots[mapid] = worldmap_mapid_area
                else:
                    worldmap_mapid_area = worldmap_mapid_spots[mapid]

                worldmap_mapid_area[worldmap_name] = spot

    return worldmap_mapid_spots


def getFileMapidGitMovement(overworld_tracked_movement):
    graph_mapid_worldmaps = {}

    for mapid, mapid_ts in overworld_tracked_movement.items():
        graph_mapid_worldmap_movement = []
        graph_mapid_worldmaps[mapid] = graph_mapid_worldmap_movement

        for mapid_range in mapid_ts:
            graph_mapid_worldmap_movement_set = set()
            graph_mapid_worldmap_movement.append(graph_mapid_worldmap_movement_set)

            for mapid_item_path, mapid_item_commit_times in mapid_range.items():
                for commit_time in mapid_item_commit_times:
                    graph_mapid_worldmap_movement_set.add((commit_time, mapid_item_path))

    return graph_mapid_worldmaps


def generateTimesectionOverworldGitMovement(mapid_worldmap_spots, overworld_mapid_movement, graph_spots_movement_ts_size):
    graph_spots_movement_ts = []

    for i in range(graph_spots_movement_ts_size):
        graph_spots_movement = {}
        graph_spots_movement_ts.append(graph_spots_movement)

        for mapid, mapid_movement_ts in overworld_mapid_movement.items():
            mapid_movement_stamps = set(mapid_movement_ts[i])

            if mapid in mapid_worldmap_spots:
                for mapid_worldmap_spot_entry in mapid_worldmap_spots[mapid].items():
                    if mapid_worldmap_spot_entry not in graph_spots_movement:
                        graph_spots_movement_item = set()
                        graph_spots_movement[mapid_worldmap_spot_entry] = graph_spots_movement_item
                    else:
                        graph_spots_movement_item = graph_spots_movement[mapid_worldmap_spot_entry]

                    graph_spots_movement_item.update(mapid_movement_stamps)

    return graph_spots_movement_ts


def scanOverworldGitMovement(overworld_tracked_movement):
    overworld_mapid_movement = getFileMapidGitMovement(overworld_tracked_movement)

    worldmap_spots = loadWorldmapSpots()
    worldmap_mapid_spots = locateWorldmapMapidSpots(worldmap_spots)

    return generateTimesectionOverworldGitMovement(worldmap_mapid_spots, overworld_mapid_movement, scanner.tracker_timesection_len)


def run(overworld_tracked_movement):
    global scanner
    scanner = AuthorScanRepository.scanner

    worldmap_movement = scanOverworldGitMovement(overworld_tracked_movement)

    graph_content = worldmap_movement
    scanner.writeGraphFile(result_path_name, graph_content)
