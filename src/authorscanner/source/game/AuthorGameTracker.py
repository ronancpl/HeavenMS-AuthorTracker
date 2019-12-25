import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
from authorscanner import AuthorScanRepository
import math
import os.path


def getFileCommitChangesTimesectionTimeset(file_change_delta):
    changes_data = []

    for commit_time in file_change_delta['modification_commit_times']:
        file_commit_data = {'commit_time': commit_time}
        changes_data.append(file_commit_data)

    file_changes_db = scanner.generateTimeSectionDatabase(changes_data, ['commit_time'], days=20)

    file_changes_timeset = []
    for file_changes_range in file_changes_db:
        changes_times = set()

        for file_changes_item in file_changes_range:
            changes_times.add(file_changes_item['commit_time'])

        file_changes_timeset.append(changes_times)

    return file_changes_timeset


def trackRepositoryCommitFileChanges():
    file_change_times = {}
    for file_change_delta in scanner.deltas.values():
        file_changes_ts_set = getFileCommitChangesTimesectionTimeset(file_change_delta)
        file_change_times[file_change_delta['path']] = file_changes_ts_set

    return file_change_times


def trackRepositoryCommitQuests():
    quests = {}

    for commit_sha, commit_quests in scanner.commit_quests.items():
        commit_timestamp = scanner.commits[commit_sha]['commit']['author']['date']

        for questid in commit_quests:
            if questid not in quests:
                quest_times = []
                quests[questid] = quest_times
            else:
                quest_times = quests[questid]

            quest_times.append({'commit_time': commit_timestamp})

    quest_tracked_times = {}
    for quest, quest_times in quests.items():
        quest_times_db = scanner.generateTimeSectionDatabase(quest_times, ['commit_time'], days=20)

        quest_times_ts = []
        quest_tracked_times[quest] = quest_times_ts

        for quest_times_range in quest_times_db:
            quest_times_timeset = set()

            for quest_times_item in quest_times_range:
                quest_times_timeset.add(quest_times_item['commit_time'])

            quest_times_ts.append(quest_times_timeset)

    return quest_tracked_times


def loadPathOverworldReferencesFile(overworld_ref_file):
    path_refs = {}

    file = open(overworld_ref_file, 'r')
    for line in file.readlines():
        idx = line.rfind(':')
        if idx > -1:
            line = line[:idx]

        tokens = line.split()
        path = tokens[0]

        mapids = []
        if len(tokens) > 1:
            for mapid in tokens[1:]:
                mapids.append(int(mapid))

        path_refs[path] = mapids

    file.close()
    return path_refs


def loadNpcOverworldReferences(overworld_ref_dir_path):
    npc_mapids = {}

    for path, mapids in loadPathOverworldReferencesFile(overworld_ref_dir_path + '1_npc.txt').items():
        npcid = int(path[10:17])
        npc_mapids[npcid] = set(mapids)

    for path, mapids in loadPathOverworldReferencesFile(overworld_ref_dir_path + '0_npc.txt').items():
        path = path[12:]
        npcid = int(path[:path.find('.')])

        if npcid in npc_mapids:
            npc_mapids[npcid].update(set(mapids))
        else:
            npc_mapids[npcid] = set(mapids)

    return npc_mapids


def loadQuestOverworldReferences(overworld_ref_dir_path):
    quest_npcids = []
    npcids = None

    file = open(scanner.wz_path + '/Quest.wz/Check.img.xml', 'r')
    for qline in file.readlines():
        if qline.startswith('  <imgdir name="'):
            qline = qline[16:]

            qid = int(qline[:qline.find('"')])
            npcids = []
            quest_npcids.append((qid, npcids))
        elif qline.startswith('      <int name="npc" value="'):
            qline = qline[29:]

            npcid = int(qline[:qline.find('"')])
            npcids.append(npcid)

    file.close()

    npc_mapids = loadNpcOverworldReferences(overworld_ref_dir_path)

    quest_mapids = {}
    for quest, npcids in quest_npcids:
        mapids = set()

        for npcid in npcids:
            if npcid in npc_mapids:
                mapids.update(npc_mapids[npcid])

        quest_mapids[quest] = mapids

    for quest, mapids in quest_mapids.items():
        quest_mapids[quest] = sorted(list(mapids))

    return quest_mapids


def loadPathOverworldReferences(overworld_ref_dir_path):
    path_refs = {}

    for file in os.listdir(overworld_ref_dir_path):
        path_refs.update(loadPathOverworldReferencesFile(overworld_ref_dir_path + file))

    quest_refs = loadQuestOverworldReferences(overworld_ref_dir_path)

    return path_refs, quest_refs


def updateMapidTimesectionCommits(overworld_tracked_changes, mapid, ts_item_key, ts_item_commitstamps, ts_limit):
    if mapid in overworld_tracked_changes:
        tracked_changes = overworld_tracked_changes[mapid]
    else:
        tracked_changes = [ {} for i in range(ts_limit) ]
        overworld_tracked_changes[mapid] = tracked_changes

    for i in range(ts_limit):
        tracked_changes[i][ts_item_key] = ts_item_commitstamps[i]


def trackRepositoryMapidMovement(overworld_ref_dir_path, tracked_file_movement, tracked_quest_movement):
    path_mapids, quest_mapids = loadPathOverworldReferences(overworld_ref_dir_path)

    overworld_tracked_changes = {}

    for path, ts_commitstamps in tracked_file_movement.items():
        if path in path_mapids:
            for mapid in path_mapids[path]:
                updateMapidTimesectionCommits(overworld_tracked_changes, mapid, path, ts_commitstamps, scanner.tracker_timesection_len)

    for quest, ts_commitstamps in tracked_quest_movement.items():
        if quest in quest_mapids:
            for mapid in quest_mapids[quest]:
                path = 'q' + str(quest)
                updateMapidTimesectionCommits(overworld_tracked_changes, mapid, path, ts_commitstamps, scanner.tracker_timesection_len)

    return overworld_tracked_changes


def trackRepositoryOverworldMovement():
    tracked_file_movement = trackRepositoryCommitFileChanges()
    tracked_quest_movement = trackRepositoryCommitQuests()

    overworld_tracked_movement = trackRepositoryMapidMovement('../../tools/MapleWorldScanner/lib/scan/', tracked_file_movement, tracked_quest_movement)
    return tracked_file_movement, overworld_tracked_movement


def run():
    global scanner
    scanner = AuthorScanRepository.scanner

    return trackRepositoryOverworldMovement()


if __name__ == '__main__':
    run()
