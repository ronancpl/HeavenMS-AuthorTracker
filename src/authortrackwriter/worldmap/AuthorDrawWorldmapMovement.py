from random import randint

import csv
import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sys

from authorscanner import AuthorScanRepository
from authortrackwriter import AuthorGraphResultFile

from authortrackwriter import AuthorGraphResultFile
from authortrackwriter import AuthorGraphResultPrinter

result_type = AuthorGraphResultFile.ResultFile.WORLDMAP

worldmap_width = 640
worldmap_height = 470

INIT_RADILIST = []
INIT_COORLIST = []


def read_coord_circle(fl, circle_list):
    # reads circle id
    fl.read(4)
    circle = []

    # reads lat
    str_ = str(fl.read(35))
    circle.append(float(str_))

    # reads lng
    str_ = str(fl.read(35))
    circle.append(float(str_))

    # reads end-of-line (\n)
    fl.read(1)

    circle_list.append(circle)


def init_coord_list(i):
    # returns all circles description, at depth 'i'

    fname = scanner.tools_path + '/coords/csq' + str(i) + '.txt'

    fl = open(fname, "r+t")
    circle_list = []

    # reads 'i' circles at the coordinates file
    for j in range(0, i):
        read_coord_circle(fl, circle_list)

    fl.close()

    return circle_list


def init_radius_coord_list(_meta, fl, st, en):
    i = st

    while True:
        str_ = fl.readline()

        if str_ == '':
            _meta['radCanGrow'] = False     # if run, flag declares there is no more depth
            _meta['radius_cache'] = i       # acts as a cursor, telling the max value of depth cached
            break

        data_ = str_.split(" ")

        if len(data_) < 2:
            _meta['radCanGrow'] = False
            _meta['radius_cache'] = i
            break

        old_i = i
        i = int(data_[0])

        # empty spaces: there is no viable registry for these rows
        for v in range(old_i + 1, i):
            INIT_RADILIST.append(0.0)
            INIT_COORLIST.append([])

        val_ = data_[1]
        INIT_RADILIST.append(float(val_))

        circle_list = init_coord_list(i)
        INIT_COORLIST.append(circle_list)

        if i >= en:
            _meta['radius_cache'] = i
            break


def init_circle_pack_structure():
    fl = open(scanner.tools_path + '/coords/radius.txt', 'r')
    init_radius_coord_list({}, fl, 0, 100)
    fl.close()


def calcGitWorldmapMovement(worldmap_movement):
    spot_mods = {}

    for spot, spot_movement in worldmap_movement.items():
        spot_mods[spot] = countWorldMapSpotChanges(spot_movement)

    return spot_mods


def countWorldMapSpotChanges(spot_movement):
    spot_commits = set()
    spot_files = set()

    for spot_commit, spot_file in spot_movement:
        spot_commits.add(spot_commit)
        spot_files.add(spot_file)

    return len(spot_movement), len(spot_commits), len(spot_files)


def generateWorldmapSpotGraphNodes(spot, spot_movement, kde_worldmap_x, kde_worldmap_y):
    if len(spot_movement) > 0:
        spot_movements, spot_commits, spot_files = countWorldMapSpotChanges(spot_movement)

        spot_node_cpy = math.log(spot_files, 1.4) * math.log(spot_movements, 7.777)  # density
        spot_node_cpy = max(math.ceil(spot_node_cpy), 1)

        spot_node_circles = spot_commits  # reach area

        spot_node_rad = (1 + 0.2 * spot_node_circles) * 25
        spot_node_rad *= INIT_RADILIST[spot_node_circles]

        spot_x, spot_y = spot
        spot_y *= -1    # y-axis inverse

        # print(str(spot_movement) + " : " + str(spot_movements) + ' ' + str(spot_commits) + ' ' + str(spot_files))
        # print(str(spot) + " : copy" + str(spot_node_cpy) + ' cid' + str(spot_node_circles) + ' rad' + str(spot_node_rad))

        flip = randint(0, 2)  # flip circle-packing center coordinates for versatile KDEs
        if flip == 0:
            flip = -1

        for i in range(spot_node_cpy):
            kde_worldmap_x.append(spot_x)
            kde_worldmap_y.append(spot_y)

            for cx, cy in INIT_COORLIST[spot_node_circles]:
                kde_worldmap_x.append(spot_x + cx * spot_node_rad * flip)
                kde_worldmap_y.append(spot_y + cy * spot_node_rad * flip)


def graphGitWorldmapMovement(worldmap_name, worldmap_spot_mods):
    kde_worldmap_x = []
    kde_worldmap_y = []

    for spot, spot_movement in worldmap_spot_mods.items():
        generateWorldmapSpotGraphNodes(spot, spot_movement, kde_worldmap_x, kde_worldmap_y)

    return worldmap_name, kde_worldmap_x, kde_worldmap_y


def updateGitWorldmapItem(worldmap_movement, worldmap_name, worldmap_spot, worldmap_commitstamp_files):
    if worldmap_name not in worldmap_movement:
        worldmap_movement[worldmap_name] = {}

    worldmap_movement[worldmap_name][worldmap_spot] = worldmap_commitstamp_files


def testGitWorldmapMovement(overworld_git_movement):
    file_movements = {}

    for overworld_git_movement_range in overworld_git_movement:

        for worldmap_name_spot, worldmap_commitstamp_files in overworld_git_movement_range.items():
            worldmap_name, worldmap_spot = worldmap_name_spot
            if worldmap_name != 'WorldMap':
                continue

            for commit, filename in worldmap_commitstamp_files:
                if filename not in file_movements:
                    commit_spot_set = set(), set()
                    file_movements[filename] = commit_spot_set
                else:
                    commit_spot_set = file_movements[filename]

                commit_spot_set[0].add(commit)
                commit_spot_set[1].add(worldmap_spot)


def graphGitWorldmaps(overworld_git_movement):
    graph_worldmaps = []

    for overworld_git_movement_range in overworld_git_movement:
        range_graph_worldmaps = []
        graph_worldmaps.append(range_graph_worldmaps)

        git_worldmaps_movement = {}

        for worldmap_name_spot, worldmap_commitstamp_files in overworld_git_movement_range.items():
            worldmap_name, worldmap_spot = worldmap_name_spot

            updateGitWorldmapItem(git_worldmaps_movement, worldmap_name, worldmap_spot, worldmap_commitstamp_files)

        for worldmap_name, worldmap_movement in git_worldmaps_movement.items():
            worldmap_name, kde_worldmap_x, kde_worldmap_y = graphGitWorldmapMovement(worldmap_name, worldmap_movement)
            range_graph_worldmaps.append((worldmap_name, kde_worldmap_x, kde_worldmap_y))

        testGitWorldmapMovement(overworld_git_movement)

    return graph_worldmaps


def drawGraphGitWorldmaps(graph_worldmaps):
    csv.field_size_limit(int(777777777))

    for graph_timesection_idx in range(len(graph_worldmaps)):
        print('Processing worldmap timesection ' + str(graph_timesection_idx))
        graph_timesection = graph_worldmaps[graph_timesection_idx]

        for worldmap_name, kde_worldmap_x, kde_worldmap_y in graph_timesection:
            kde_len = len(kde_worldmap_x)

            if kde_len == 0:
                continue
            elif kde_len <= 3:  # insufficient to make up for a KDE...
                kde_worldmap_x.extend(kde_worldmap_x)
                kde_worldmap_y.extend(kde_worldmap_y)

            kde_worldmap_x[0] = kde_worldmap_x[0] - 0.00777     # avoid LinAlgError
            kde_worldmap_y[0] = kde_worldmap_y[0] + 0.00777

            if worldmap_name != 'WorldMap' and kde_len < 10:
                continue

            # for i in range(len(kde_worldmap_x)):
            #     print(str(kde_worldmap_x[i]) + ', ' + str(kde_worldmap_y[i]))

            graph_ds = [{'px': kde_worldmap_x, 'py': kde_worldmap_y}]

            filename = result_type.value
            fidx = filename.rfind('/')

            filename_st = filename[0:fidx]
            filename_ext = filename[fidx:]

            csv_filename = filename_st + '/' + worldmap_name + filename_ext
            grapher.writeGraphDataset(csv_filename, graph_ds, graph_timesection_idx)

            plot(csv_filename, worldmap_name, graph_timesection_idx)


def plot(csv_filename, worldmap_name, doc_index=-1):
    column_names, graph_content = grapher.readGraphDataset(csv_filename, doc_index)
    kde_worldmap_x = graph_content[0][0]
    kde_worldmap_y = graph_content[0][1]

    worldmap_img = scanner.tools_path + '/worldmaps/' + worldmap_name + '.png'
    plot_img = scanner.plot_path + '/worldmaps/' + worldmap_name + '_jn' + str(doc_index) + '.png'

    map_img = mpimg.imread(worldmap_img)

    # print(worldmap_img + ' num_spots:' + str(len(kde_worldmap_x)) + ' jn:' + str(doc_index))
    fig = plt.figure()
    plt.xticks(rotation=90, fontsize=4, fontweight=25)

    fig.subplots_adjust(bottom=0)
    fig.subplots_adjust(top=1)
    fig.subplots_adjust(right=1)
    fig.subplots_adjust(left=0)

    sns.kdeplot(data=kde_worldmap_x, data2=kde_worldmap_y, cmap="Wistia", n_levels=7, bw=0.12, cut=42, clip=((-worldmap_width / 2, worldmap_width / 2), (-worldmap_height / 2, worldmap_height / 2)), shade=False, shade_lowest=False)
    plt.imshow(map_img, alpha=0.20, zorder=0, extent=[-worldmap_width / 2, worldmap_width / 2, -worldmap_height / 2, worldmap_height / 2])

    grapher.savePlot(fig, plot_img)
    # plt.show()

    plt.close(fig)


def run():
    global scanner
    scanner = AuthorScanRepository.scanner

    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    init_circle_pack_structure()
    overworld_git_movement = result_type.readGraphFile()

    graph_worldmaps = graphGitWorldmaps(overworld_git_movement)
    drawGraphGitWorldmaps(graph_worldmaps)
