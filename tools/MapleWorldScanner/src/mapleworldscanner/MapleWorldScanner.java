/*
    This file is part of the HeavenMS MapleStory Server
    Copyleft (L) 2016 - 2018 RonanLana

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation version 3 as published by
    the Free Software Foundation. You may not use, modify or distribute
    this program under any other version of the GNU Affero General Public
    License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/
package mapleworldscanner;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;
import java.sql.Connection;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Iterator;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import org.apache.commons.io.FileUtils;

import mapleworldscanner.MapleWorldMapReader.WorldMapSpot;

/**
 *
 * @author RonanLana
 
 This application's objective is to acquire information from the server's scripts & XML files
 and reliably try to pinpoint them into the game's world map structures (cross-checking method).
 Researched contents are: mobs, NPCs, portals, quests, reactors, map scripts and events.
 
 Estimated parse time: 5 minutes
 
 */
public class MapleWorldScanner {
    
    static PrintWriter printWriter;
    
    static Connection con = null;
    static InputStreamReader fileReader = null;
    static BufferedReader bufferedReader = null;
    
    static String wzPath = "../../../HeavenMS/wz";
    static String scriptPath = "../../../HeavenMS/scripts";
    static String outputPath = "lib/debug";
    static String scannerPath = "lib/scan";
    
    static int initialStringLength = 250;
    
    static Map<Integer, Map<Integer, WorldMapSpot>> worldmapAreas;
    
    static Map<Integer, Integer> returnAreas = new HashMap<>();         // mapwz & event scripts
    static Set<Integer> townAreas = new HashSet<>();
    
    static Map<Integer, Set<Integer>> npcAreas = new HashMap<>();       // mapwz
    static Map<Integer, Set<Integer>> questAreas = new HashMap<>();     // questwz - start/complete npcs
    static Map<Integer, Set<Integer>> reactorAreas = new HashMap<>();   // mapwz
    
    static Map<String, Set<Integer>> mapScriptAreas = new HashMap<>();  // mapwz
    static Map<String, Integer> eventAreas = new HashMap<>();           // self script OR npc starter
    static Map<String, Set<Integer>> portalAreas = new HashMap<>();     // mapwz
    static Map<Integer, Set<Integer>> portalRetAreas = new HashMap<>();
    static Map<Integer, Set<String>> portalScripts = new HashMap<>();
    
    static Map<Integer, Map<Integer, Integer>> mobAreas = new HashMap<>();
    
    static Integer currentMapid;
    static Integer currentQuestid;
    
    static String currentInfo3;
    static String currentInfo2;
    static String currentInfo;
    static Integer currentId;
    static Integer currentTm;
    static Set<Integer> currentPortalRetAreas;
    
    static List<Integer> worldMapids = new ArrayList<>(10000);
    static Set<Integer> questMaps;
    static Map<String, Integer> eventMinMapid = new HashMap<>();
    static Map<String, Integer> eventMaxMapid = new HashMap<>();
    static Map<String, Set<Integer>> eventAssociatedMapids = new HashMap<>();
    static Map<Integer, Integer> linkedMapids = new HashMap<>();
    static Map<Integer, Integer> overworldMapids = new HashMap<>();
    static Map<Integer, Set<Integer>> linkedMapAreas = new HashMap<>(); // don't document this
    
    static List<Pair<String, String>> npcPathExtension = new ArrayList<Pair<String, String>>() {{add(new Pair<>("scripts/npc/", ".js")); add(new Pair<>("wz/Npc.wz/", ".img.xml"));}};
    /*SPECIAL PARSE*/static List<Pair<String, String>> questPathExtension = new ArrayList<Pair<String, String>>() {{add(new Pair<>("scripts/map/quest/", ".js"));}};
    static List<Pair<String, String>> reactorPathExtension = new ArrayList<Pair<String, String>>() {{add(new Pair<>("scripts/reactor/", ".js")); add(new Pair<>("wz/Reactor.wz/", ".img.xml"));}};
    static List<Pair<String, String>> mapScriptPathExtension = new ArrayList<Pair<String, String>>() {{add(new Pair<>("scripts/map/onUserEnter/", ".js")); add(new Pair<>("scripts/map/onFirstUserEnter/", ".js"));}};
    static List<Pair<String, String>> eventPathExtension = new ArrayList<Pair<String, String>>() {{add(new Pair<>("scripts/event/", ".js"));}};
    static List<Pair<String, String>> portalPathExtension = new ArrayList<Pair<String, String>>() {{add(new Pair<>("scripts/portal/", ".js"));}};
    /*SPECIAL PARSE*/static List<Pair<String, String>> zmapPathExtension = new ArrayList<Pair<String, String>>() {{add(new Pair<>("wz/Map.wz/Map/Map", ".img.xml"));}};
    static List<Pair<String, String>> zmobPathExtension = new ArrayList<Pair<String, String>>() {{add(new Pair<>("wz/Mob.wz/", ".img.xml"));}};
    
    static int fileIndex = 0;
    
    static MapWzNodeType mapwzNode = MapWzNodeType.UNDEF;
    static byte status;
    
    static enum MapWzNodeType {
        UNDEF,
        LIFE,
        REACTOR,
        PORTAL,
        INFO
    }
    
    private static String getName(String token) {
        int i, j;
        char[] dest;
        String d;
        
        i = token.lastIndexOf("name");
        i = token.indexOf("\"", i) + 1; //lower bound of the string
        j = token.indexOf("\"", i);     //upper bound

        dest = new char[initialStringLength];
        try {
            token.getChars(i, j, dest, 0);
        } catch (StringIndexOutOfBoundsException e) {
            // do nothing
            return "";
        } catch (Exception e) {
            System.out.println("error in: " + token + "");
            e.printStackTrace();
            try {
                Thread.sleep(100000000);
            } catch (Exception ex) {}
        }
        

        d = new String(dest);
        return(d.trim());
    }
    
    private static String getValue(String token) {
        int i, j;
        char[] dest;
        String d;

        i = token.lastIndexOf("value");
        i = token.indexOf("\"", i) + 1; //lower bound of the string
        j = token.indexOf("\"", i);     //upper bound

        dest = new char[initialStringLength];
        token.getChars(i, j, dest, 0);

        d = new String(dest);
        return(d.trim());
    }
    
    private static void forwardCursor(int st) {
        String line = null;

        try {
            while(status >= st && (line = bufferedReader.readLine()) != null) {
                simpleToken(line);
            }
        }
        catch(Exception e) {
            e.printStackTrace();
        }
    }
    
    private static void simpleToken(String token) {
        if(token.contains("/imgdir")) {
            status -= 1;
        }
        else if(token.contains("imgdir")) {
            status += 1;
        }
    }
    
    private static void translateMapwzToken(String token) {
        if(token.contains("/imgdir")) {
            status -= 1;
            
            if (status == 2) {
                if (mapwzNode == MapWzNodeType.LIFE) {
                    if (currentInfo3.contentEquals("n") && currentId != 0) {  // found npc
                        Set<Integer> areas = npcAreas.get(currentId);
                        if (areas == null) {
                            areas = new HashSet<>();
                            npcAreas.put(currentId, areas);
                        }
                        
                        areas.add(currentMapid);
                    } else if (currentInfo3.contentEquals("m") && currentId != 0) { // found mob
                        increaseMapMobCount(currentId, currentMapid);
                    }
                } else if (mapwzNode == MapWzNodeType.REACTOR) {
                    if (currentId != 0) {  // found reactor
                        Set<Integer> areas = reactorAreas.get(currentId);
                        if (areas == null) {
                            areas = new HashSet<>();
                            reactorAreas.put(currentId, areas);
                        }

                        areas.add(currentMapid);
                    }
                } else if (mapwzNode == MapWzNodeType.PORTAL) {
                    if (!currentInfo3.isEmpty()) {  // found portal
                        Set<Integer> areas = portalAreas.get(currentInfo3);
                        if (areas == null) {
                            areas = new HashSet<>();
                            portalAreas.put(currentInfo3, areas);
                        }
                        
                        areas.add(currentMapid);
                    } else if (currentTm != 999999999) {
                        currentPortalRetAreas.add(currentTm);
                    }
                }
            } else if (status == 1) {
                if (mapwzNode == MapWzNodeType.INFO) {
                    if (!currentInfo.isEmpty()) {  // found mapscript
                        Set<Integer> areas = mapScriptAreas.get(currentInfo);
                        if (areas == null) {
                            areas = new HashSet<>();
                            mapScriptAreas.put(currentInfo, areas);
                        }

                        areas.add(currentMapid);
                    }
                    
                    if (!currentInfo2.isEmpty()) {  // found mapscript
                        Set<Integer> areas = mapScriptAreas.get(currentInfo2);
                        if (areas == null) {
                            areas = new HashSet<>();
                            mapScriptAreas.put(currentInfo2, areas);
                        }

                        areas.add(currentMapid);
                    }
                } else if (mapwzNode == MapWzNodeType.PORTAL) {
                    portalRetAreas.put(currentMapid, currentPortalRetAreas);
                    currentPortalRetAreas = new HashSet<>(5);
                }
                
                mapwzNode = MapWzNodeType.UNDEF;
            }
        }
        else if(token.contains("imgdir")) {
            status += 1;
            
            if (status == 3) {
                if (mapwzNode == MapWzNodeType.LIFE) {
                    currentInfo3 = "";
                    currentId = 0;
                } else if (mapwzNode == MapWzNodeType.REACTOR) {
                    currentId = 0;
                } else if (mapwzNode == MapWzNodeType.PORTAL) {
                    currentInfo3 = "";
                    currentTm = 999999999;
                } else if (mapwzNode == MapWzNodeType.INFO) {
                    currentInfo = "";
                    currentInfo2 = "";
                }
            } else if (status == 2) {
                String d = getName(token);
                
                switch (d) {
                    case "life":
                        mapwzNode = MapWzNodeType.LIFE;
                        break;
                    
                    case "reactor":
                        mapwzNode = MapWzNodeType.REACTOR;
                        break;
                        
                    case "portal":
                        mapwzNode = MapWzNodeType.PORTAL;
                        break;
                        
                    case "info":
                        mapwzNode = MapWzNodeType.INFO;
                        break;
                }
            }
        }
        else {
            if (status == 3) {
                if (mapwzNode == MapWzNodeType.LIFE) {
                    String d = getName(token);
                    
                    switch (d) {
                        case "type":
                            String v = getValue(token);
                            
                            if (v.length() == 1) {
                                currentInfo3 = v;
                            } else {
                                forwardCursor(status);
                            }
                            
                            break;
                            
                        case "id":
                            currentId = Integer.valueOf(getValue(token));
                            break;
                    }
                } else if (mapwzNode == MapWzNodeType.REACTOR) {
                    String d = getName(token);
                    
                    switch (d) {
                        case "id":
                            currentId = Integer.valueOf(getValue(token));
                            break;
                    }
                } else if (mapwzNode == MapWzNodeType.PORTAL) {
                    String d = getName(token);
                    
                    switch (d) {
                        case "tm":
                            currentTm = Integer.parseInt(getValue(token));
                            break;
                        
                        case "script":
                            currentInfo3 = getValue(token);
                            break;
                            
                        case "pn":
                            if (getValue(token).contentEquals("tp")) {  // has Door support, is a town
                                townAreas.add(currentMapid);
                            }
                            
                            break;
                    }
                }
            } else if (status == 2) {
                if (mapwzNode == MapWzNodeType.INFO) {
                    String d = getName(token);
                    
                    switch (d) {
                        case "onUserEnter":
                            currentInfo = getValue(token);
                            break;
                            
                        case "onFirstUserEnter":
                            currentInfo2 = getValue(token);
                            break;
                            
                        case "returnMap":
                            int rmapid = Integer.valueOf(getValue(token));
                            if (rmapid != 999999999) returnAreas.put(currentMapid, rmapid);
                            else returnAreas.put(currentMapid, currentMapid);
                            
                            break;
                    }
                }
            }
        }
    }
    
    private static void increaseMapMobCount(Integer mobid, Integer mapid) {
        Map<Integer, Integer> areas = mobAreas.get(mobid);
        if (areas == null) {
            areas = new HashMap<>(3);
            mobAreas.put(mobid, areas);
        }

        Integer curCount = areas.get(mapid);
        if (curCount != null) {
            areas.put(mapid, curCount + 1);
        } else {
            areas.put(mapid, 1);
        }
    }
    
    private static int getMapIdFromFilename(String fileName) {
        return Integer.parseInt(fileName.substring(0, 9));
    }
    
    private static void parseMapwzFile(File file) {
        // This will reference one line at a time
        String line = null;

        try {
            currentMapid = getMapIdFromFilename(file.getName());
            worldMapids.add(currentMapid);
            
            currentPortalRetAreas = new HashSet<>(5);
            
            mapwzNode = MapWzNodeType.UNDEF;
            status = 0;
            
            fileReader = new InputStreamReader(new FileInputStream(file), "UTF-8");
            bufferedReader = new BufferedReader(fileReader);

            while((line = bufferedReader.readLine()) != null) {
                translateMapwzToken(line);
            }

            bufferedReader.close();
            fileReader.close();
        }
        
        catch(IOException ex) {
            System.out.println("[ACCESS] Error reading file '" + file.getName() + "'");
        }
    }
    
    private static void listFiles(String directoryName, ArrayList<File> files) {
        File directory = new File(directoryName);
        
        // get all the files from a directory
        File[] fList = directory.listFiles();
        for (File file : fList) {
            if (file.isDirectory()) {
                listFilesInternal(file.getAbsolutePath(), files);
            }
        }
    }
    
    private static void listFilesInternal(String directoryName, ArrayList<File> files) {
        File directory = new File(directoryName);
        
        // get all the files from a directory
        File[] fList = directory.listFiles();
        for (File file : fList) {
            if (file.isFile()) {
                files.add(file);
            } else if (file.isDirectory()) {
                listFilesInternal(file.getAbsolutePath(), files);
            }
        }
    }
    
    private static void parseMapwzDirectory() {
        ArrayList<File> files = new ArrayList<>();
        listFiles(wzPath + "/Map.wz/Map", files);
        
        for (File f : files) {
            parseMapwzFile(f);
        }
    }
    
    private static void translateQuestwzToken(String token) {
        if(token.contains("/imgdir")) {
            status -= 1;
        }
        else if(token.contains("imgdir")) {
            status += 1;
            
            if (status == 2) {
                if (!questMaps.isEmpty()) {
                    questAreas.put(currentQuestid, questMaps);
                    questMaps = new HashSet<>();
                }
                
                currentQuestid = Integer.valueOf(getName(token));
            }
        }
        else {
            if (status == 3) {
                if (getName(token).contentEquals("npc")) {
                    int npcid = Integer.valueOf(getValue(token));

                    Set<Integer> npcMaps = npcAreas.get(npcid);
                    if (npcMaps != null) {
                        questMaps.addAll(npcMaps);
                    }
                }
            }
        }
    }
    
    private static void parseQuestwzFile(File file) {
        // This will reference one line at a time
        String line = null;

        try {
            status = 0;
            questMaps = new HashSet<>();
            
            fileReader = new InputStreamReader(new FileInputStream(file), "UTF-8");
            bufferedReader = new BufferedReader(fileReader);
            
            while((line = bufferedReader.readLine()) != null) {
                translateQuestwzToken(line);
            }
            
            if (!questMaps.isEmpty()) {
                questAreas.put(currentQuestid, questMaps);
            }
            
            bufferedReader.close();
            fileReader.close();
        }
        
        catch(IOException ex) {
            System.out.println("[ACCESS] Error reading file '" + file.getName() + "'");
        }
    }
    
    private static int getTargetMapidFromMatchingDataOnFile(String fileContent, String searchStr) {
        int idx = fileContent.indexOf(searchStr);
        if (idx < 0) {
            return -1;
        }
        
        String s = fileContent.substring(idx + searchStr.length());
        idx = Math.min(s.indexOf('\n'), s.indexOf(';'));
        
        while (s.length() > 4) {
            s = s.substring(0, idx);
            try {
                return Integer.valueOf(s);
            } catch (NumberFormatException nfe) {
                idx--;
            }
        }
        
        return -1;
    }
    
    private static List<Integer> fetchMatchingMapids(String fileContent, String searchStr) {
        List<Integer> ret = new ArrayList<>();
        
        String copyContent = fileContent;
        while (true) {
            int idx = copyContent.indexOf(searchStr);
            if (idx < 0) {
                break;
            }

            String s = copyContent.substring(idx + searchStr.length());
            idx = Math.min(s.indexOf('\n'), s.indexOf(';'));

            copyContent = s.substring(idx + 1);
            while (s.length() > 4) {
                s = s.substring(0, idx);
                try {
                    int mapid = Integer.valueOf(s);
                    ret.add(mapid);
                    
                    break;
                } catch (NumberFormatException nfe) {
                    idx--;
                }
            }
        }
        
        return ret;
    }
    
    private static Set<Integer> fetchAssociatedMapids(String fileContent, String[] searchStr) {
        Set<Integer> ret = new HashSet<>();
        for (String search : searchStr) {
            ret.addAll(fetchMatchingMapids(fileContent, search));
        }
        
        return ret;
    }
    
    private static void generateEventAssociatedMapids(String eventName, String fileContent) {
        int minMapId = getTargetMapidFromMatchingDataOnFile(fileContent, "varminMapId=");
        if (minMapId > -1) {
            int maxMapId = getTargetMapidFromMatchingDataOnFile(fileContent, "varmaxMapId=");
            
            if (maxMapId > -1) {
                eventMinMapid.put(eventName, minMapId);
                eventMaxMapid.put(eventName, maxMapId);
            }
        }
        
        Set<Integer> ret = fetchAssociatedMapids(fileContent, new String[]{"getMapInstance(", "getMapFactory().getMap("});
        if (!ret.isEmpty()) {
            Set<Integer> cur = eventAssociatedMapids.get(eventName);
            if (cur == null) {
                eventAssociatedMapids.put(eventName, ret);
            } else {
                cur.addAll(ret);
            }
        }
    }
    
    private static String[] getScriptNameFromMatchingDataOnFile(String fileContent, String searchStr) {
        int idx = fileContent.indexOf(searchStr);
        if (idx < 0) {
            return null;
        }
        
        String s = fileContent.substring(idx + searchStr.length());
        idx = s.indexOf('\"');
        
        String[] ret = new String[2];
        ret[0] = s.substring(0, idx);
        ret[1] = s.substring(idx + 1);
        return ret;
    }
    
    private static Set<String> getScriptNamesFromMatchingDataSearch(File file, String[] strings) {
        String ret[] = null;
        String copyContent = null;
        try {
            String fileContent = getFileContent(file);
            Set<String> scriptNames = new HashSet<>();
            
            for (int i = 0; i < strings.length; i++) {
                copyContent = fileContent;
                
                while (true) {
                    ret = getScriptNameFromMatchingDataOnFile(copyContent, strings[i]);
                    if (ret != null) {
                        scriptNames.add(ret[0]);
                        copyContent = ret[1];
                    } else {
                        break;
                    }
                }
            }
            
            return scriptNames;
        } catch(IOException ioe) {
            System.out.println("[ACCESS] Failed to read file: " + file.getAbsolutePath());
            ioe.printStackTrace();
            return null;
        } catch(RuntimeException re) {
            System.out.print("   [");
            for (String st : ret) {
                System.out.println(st + ", ");
            }
            
            System.out.println("] | '" + copyContent + "'\n---------------------------");
            //re.printStackTrace();
            return null;
        }
    }
    
    private static String getFileContent(File file) throws IOException {
        String fileContent = FileUtils.readFileToString(file, "UTF-8");
        fileContent = fileContent.replace(" ", "");
        
        return fileContent;
    }
    
    private static int getTargetMapidFromMatchingDataSearch(File file, String[] strings) {
        try {
            String fileContent = getFileContent(file);
            
            int ret;
            for (String string : strings) {
                ret = getTargetMapidFromMatchingDataOnFile(fileContent, string);
                if (ret >= 0) {
                    generateEventAssociatedMapids(file.getName(), fileContent);
                    return ret;
                }
            }
            
            return -1;
        } catch(IOException ioe) {
            System.out.println("[ACCESS] Failed to read file: " + file.getAbsolutePath());
            ioe.printStackTrace();
            return -2;
        }
    }
    
    private static void parseEventScripts() {
        Iterator iter = FileUtils.iterateFiles(new File(scriptPath + "/event"), new String[]{"js"}, true);

        String[] searchStr = new String[]{"varexitMap=", "getMapInstance(", "getMapFactory().getMap(", "varbossMapid=", "returnTo=newArray("};
        while(iter.hasNext()) {
            File file = (File) iter.next();
            
            try {
                String fileContent = getFileContent(file);
                String eventName = file.getName();
                
                int mapid = getTargetMapidFromMatchingDataSearch(file, searchStr);
                if (mapid >= 0) {
                    Set<Integer> mapids = fetchAssociatedMapids(fileContent, searchStr);
                    if (!mapids.isEmpty()) {
                        Set<Integer> eventMapids = new HashSet<>();
                        for (Integer mid : mapids) {
                            eventMapids.add(mid);
                        }
                        eventAssociatedMapids.put(eventName, eventMapids);
                    }
                    
                    // puts any related mapid as that event returning area, may be updated
                    Integer rmapid = ((worldmapAreas.containsKey(mapid) || townAreas.contains(returnAreas.get(mapid))) ? mapid : returnAreas.get(mapid));
                    if (rmapid != null) {
                        eventAreas.put(eventName, rmapid);
                    } else {
                        System.out.println("[NOT FOUND] Could not determine return mapid for mapid " + mapid);
                    }
                } else {
                    System.out.println("[NOT FOUND] Could not determine a mapid for event script: " + file.getAbsolutePath());
                }
            } catch(IOException ioe) {
                System.out.println("[ACCESS] Failed to read file: " + file.getAbsolutePath());
                ioe.printStackTrace();
            }
        }
    }
    
    private static String getObjectFromScriptName(String scriptName) {
        int idx = scriptName.indexOf('.');
        return scriptName.substring(0, idx);
    }
    
    private static int getObjectIdFromScriptName(String scriptName) {
        return Integer.parseInt(getObjectFromScriptName(scriptName));
    }
    
    private static String[] getWarpDescriptionFromMatchingDataOnFile(String fileContent, String searchStr) {
        int idx = fileContent.indexOf(searchStr);
        if (idx < 0) {
            return null;
        }
        
        String s = fileContent.substring(idx + searchStr.length());
        
        idx = s.indexOf(')');
        int v = s.indexOf(',');
        if (v < idx && v >= 0) {
            idx = v;
        }
        
        String[] ret = new String[2];
        ret[0] = s.substring(0, idx);
        ret[1] = s.substring(idx + 1);
        return ret;
    }
    
    private static Set<Integer> getWarpDescriptionsFromMatchingDataSearch(File file, String[] strings) {
        String ret[] = null;
        String copyContent = null;
        try {
            String fileContent = getFileContent(file);
            Set<Integer> warpDescriptions = new HashSet<>();
            
            for (int i = 0; i < strings.length; i++) {
                copyContent = fileContent;
                
                while (true) {
                    ret = getWarpDescriptionFromMatchingDataOnFile(copyContent, strings[i]);
                    if (ret != null) {
                        try {
                            warpDescriptions.add(Integer.valueOf(ret[0]));
                        } catch (NumberFormatException nfe) {}  // do nothing
                        
                        copyContent = ret[1];
                    } else {
                        break;
                    }
                }
            }
            
            return warpDescriptions;
        } catch(IOException ioe) {
            System.out.println("[ACCESS] Failed to read file: " + file.getAbsolutePath());
            ioe.printStackTrace();
            return null;
        } catch(RuntimeException re) {
            System.out.print("   {");
            for (String st : ret) {
                System.out.println(st + ", ");
            }
            
            System.out.println("} | '" + copyContent + "'\n---------------------------");
            //re.printStackTrace();
            return null;
        }
    }
    
    private static Set<Integer> getMobidDescriptionsFromMatchingDataSearch(File file, String[] strings) {
        try {
            String fileContent = getFileContent(file);
            Set<Integer> mobDescriptions = new HashSet<>();
            
            for (int i = 0; i < strings.length; i++) {
                Matcher startM = Pattern.compile("\\b" + strings[i]).matcher(fileContent);
                Matcher endM = Pattern.compile("(\\w)*\\b").matcher(fileContent);
                int idx = 0;
                while (startM.find(idx)) {
                    idx = startM.end();
                    if (endM.find(idx)) {
                        String token = fileContent.substring(endM.start(), endM.end());
                        try {
                            mobDescriptions.add(Integer.valueOf(token));
                        } catch (NumberFormatException nfe) {}  // do nothing
                    }
                }
            }
            
            return mobDescriptions;
        } catch(IOException ioe) {
            System.out.println("[ACCESS] Failed to read file: " + file.getAbsolutePath());
            ioe.printStackTrace();
            return null;
        } catch(RuntimeException re) {
            System.out.println("[ERROR] Failed to parse file: " + file.getAbsolutePath());
            re.printStackTrace();
            throw re;
        }
    }
    
    private static Integer getMinimumElement(Set<Integer> set) {
        Integer minElement = Integer.MAX_VALUE;
        for (Integer i : set) {
            if (minElement > i) {
                minElement = i;
            }
        }
        
        return minElement;
    }
    
    private static boolean shouldLinkMaps(Integer currentLinkedMap, Integer newLinkedMap) {
        return newLinkedMap < currentLinkedMap && !worldmapAreas.containsKey(currentLinkedMap);
    }
    
    private static void linkMapIfRelevant(Integer targetMap, Integer newLinkedMap) {
        Integer curLinkedMap = linkedMapids.get(targetMap);
        
        if (curLinkedMap == null || shouldLinkMaps(curLinkedMap, newLinkedMap)) {
            linkedMapids.put(targetMap, newLinkedMap);
        }
    }
    
    private static void parseEventObjectScripts1(String eventObject, Map<Integer, Set<Integer>> objectAreas, int state) {
        Iterator iter = FileUtils.iterateFiles(new File(scriptPath + "/" + eventObject), new String[]{"js"}, true);
        
        if (state == 0) {
            String[] wsearchStr = new String[]{".warp(", ".changeMap("};
            while(iter.hasNext()) {
                File file = (File) iter.next();
                
                Set<Integer> warpMapids = getWarpDescriptionsFromMatchingDataSearch(file, wsearchStr);
                if (!warpMapids.isEmpty()) {
                    try {
                        int oid = getObjectIdFromScriptName(file.getName());
                        Set<Integer> oMapid = objectAreas.get(oid);

                        if (oMapid != null) {
                            oMapid.addAll(warpMapids);
                        } else {
                            objectAreas.put(oid, warpMapids);
                            oMapid = warpMapids;
                        }
                        
                        Integer linkedMapid = getMinimumElement(warpMapids);
                        if (linkedMapid != Integer.MAX_VALUE) {
                            for (Integer i : oMapid) {
                                linkMapIfRelevant(i, linkedMapid);
                            }
                        }
                    } catch (NumberFormatException nfe) {}  // do nothing
                }
            }
        } else if (state == 1) {
            String[] searchStr = new String[]{".getEventManager(\"", "ventName=\""};
            while(iter.hasNext()) {
                File file = (File) iter.next();
                
                Set<String> scriptNames = getScriptNamesFromMatchingDataSearch(file, searchStr);
                if (scriptNames != null && !scriptNames.isEmpty()) {
                    try {
                        int oid = getObjectIdFromScriptName(file.getName());

                        Set<Integer> oMapid = objectAreas.get(oid);
                        if (!oMapid.isEmpty()) {
                            int oMap = getMinimumElement(oMapid);
                            for (String scriptName : scriptNames) {
                                eventAreas.put(scriptName + ".js", oMap);
                            }
                        } else {
                            System.out.println("[ERROR] Could not resolve event " + eventObject + " mapid for '" + file.getName() + "'. " + oMapid);
                        }
                    } catch (NumberFormatException nfe) {}  // do nothing
                }
            }
        } else {
            String[] wsearchStr = new String[]{"mob1=", "mob2=", "bossMobid=", "mobId", ".getMonster\\(", ".getMonsterById\\(", ".killMonster\\("};
            while(iter.hasNext()) {
                File file = (File) iter.next();
                
                Set<Integer> mobids = getMobidDescriptionsFromMatchingDataSearch(file, wsearchStr);
                if (!mobids.isEmpty()) {
                    try {
                        int oid = getObjectIdFromScriptName(file.getName());
                        Set<Integer> omaps = objectAreas.get(oid);
                        if (omaps != null) {
                            for (Integer mobid : mobids) {
                                for (Integer mapid : omaps) {
                                    increaseMapMobCount(mobid, mapid);
                                }
                            }
                        }
                    } catch (NumberFormatException nfe) {}  // do nothing
                }
            }
        }
    }
    
    private static void parseEventObjectScripts2(String eventObject, Map<String, Set<Integer>> objectAreas, int state) {
        Iterator iter = FileUtils.iterateFiles(new File(scriptPath + "/" + eventObject), new String[]{"js"}, true);
        
        if (state == 0) {
            String[] wsearchStr = new String[]{".warp(", ".changeMap("};
            while(iter.hasNext()) {
                File file = (File) iter.next();

                Set<Integer> warpMapids = getWarpDescriptionsFromMatchingDataSearch(file, wsearchStr);
                
                if (!warpMapids.isEmpty()) {
                    String oid = getObjectFromScriptName(file.getName());
                    Set<Integer> oMapid = objectAreas.get(oid);

                    if (oMapid != null) {
                        oMapid.addAll(warpMapids);
                    } else {
                        objectAreas.put(oid, warpMapids);
                        oMapid = warpMapids;
                    }
                    
                    Integer linkedMapid = getMinimumElement(warpMapids);
                    if (linkedMapid != Integer.MAX_VALUE) {
                        for (Integer i : oMapid) {
                            linkMapIfRelevant(i, linkedMapid);
                        }
                    }
                }
            }
        } else if (status == 1) {
            String[] searchStr = new String[]{".getEventManager(\"", "ventName=\""};
            while(iter.hasNext()) {
                File file = (File) iter.next();

                Set<String> scriptNames = getScriptNamesFromMatchingDataSearch(file, searchStr);
                if (scriptNames != null && !scriptNames.isEmpty()) {
                    try {
                        String oid = getObjectFromScriptName(file.getName());
                        Set<Integer> oMapid = objectAreas.get(oid);
                        if (oMapid == null) {
                            oMapid = new HashSet<>(1);
                            oMapid.add(Integer.parseInt(oid));
                        }

                        if (!oMapid.isEmpty()) {
                            int oMap = getMinimumElement(oMapid);

                            for (String scriptName : scriptNames) {
                                eventAreas.put(scriptName + ".js", oMap);
                            }
                        } else {
                            System.out.println("[ERROR] Could not resolve event " + eventObject + " mapid for '" + file.getName() + "'. " + oMapid);
                        }
                    } catch (NumberFormatException nfe) {
                        System.out.println("[ERROR] Could not resolve " + eventObject + " script '" + file.getName() + "'");
                    }
                }
            }
        } else {
            String[] wsearchStr = new String[]{"mob1=", "mob2=", "bossMobid=", "mobId", ".getMonster\\(", ".getMonsterById\\(", ".killMonster\\("};
            while(iter.hasNext()) {
                File file = (File) iter.next();
                
                Set<Integer> mobids = getMobidDescriptionsFromMatchingDataSearch(file, wsearchStr);
                if (!mobids.isEmpty()) {
                    try {
                        String oid = getObjectFromScriptName(file.getName());
                        Set<Integer> omaps = objectAreas.get(oid);
                        if (omaps != null) {
                            for (Integer mobid : mobids) {
                                for (Integer mapid : omaps) {
                                    increaseMapMobCount(mobid, mapid);
                                }
                            }
                        }
                    } catch (NumberFormatException nfe) {}  // do nothing
                }
            }
        }
    }
    
    private static List<String> getEventKeysOrderedByMinMapid() {
        List<Entry<String, Integer>> eventKeys = new ArrayList<>(eventMinMapid.entrySet());
        Collections.sort(eventKeys, new Comparator<Entry<String, Integer>>() {
            @Override
            public int compare(Entry<String, Integer> o1, Entry<String, Integer> o2) {
                return o1.getValue() - o2.getValue();
            }
        });
        
        List<String> ret = new ArrayList<>(eventKeys.size());
        for (Entry<String, Integer> e : eventKeys) {
            ret.add(e.getKey());
        }
        
        return ret;
    }
    
    private static int bsearchWorldMapidIndex(int searchMapid, int cursor) {
        int init, end, mid;
        
        int curMapid = worldMapids.get(cursor);
        int worldLimit = worldMapids.size() - 1;
        
        if (searchMapid < curMapid) {
            init = 0;
            end = cursor;
        } else {
            init = cursor;
            end = worldLimit;
        }
        
        int mapMid;
        while (true) {
            mid = (init + end) / 2;
            
            if (init >= end) {
                mapMid = worldMapids.get(mid);
                if (searchMapid > mapMid) {
                    mid = end + 1;
                } else {
                    mid = end;
                }
                
                if (mid < 0) {
                    mid = 0;
                }
                
                break;
            }
            
            mapMid = worldMapids.get(mid);
            if (searchMapid < mapMid) {
                end = mid - 1;
            } else if (searchMapid > mapMid) {
                init = mid + 1;
            } else {
                break;
            }
        }
        
        return mid;
    }
    
    private static int propagateEventReturnMapids(String event, int cursor) {
        int minMapid = eventMinMapid.get(event), maxMapid = eventMaxMapid.get(event);
        int eventReturnMapid = eventAreas.get(event);
        
        int init = bsearchWorldMapidIndex(minMapid, cursor);
        int idx = init, size = worldMapids.size();
        while (idx < size) {
            int mapid = worldMapids.get(idx);
            if (mapid > maxMapid) {
                break;
            }
            
            returnAreas.put(mapid, eventReturnMapid);
            idx++;
        }
        
        return idx;
    }
    
    private static Integer getBaseReturnMapid(Integer mapId) {
        Integer curId;
        while (true) {
            if (worldmapAreas.containsKey(mapId)) {
                return mapId;
            }
            
            curId = linkedMapids.get(mapId);
            if (curId == null || curId.equals(mapId)) {
                return mapId;
            }
            
            mapId = curId;
        }
    }
    
    private static void propagateLinkedReturnMapids() {
        boolean dirty = true;
        while (dirty) {
            dirty = false;
            
            for (Integer mapId : returnAreas.keySet()) {
                Integer linkedId = getBaseReturnMapid(mapId);
                
                if (!linkedId.equals(mapId)) {
                    Integer curLinkedid = returnAreas.get(mapId);
                    if (!linkedId.equals(curLinkedid)) {
                        dirty = true;
                        returnAreas.put(mapId, linkedId);
                    }
                }
            }
        }
    }
    
    private static void propagateOverworldEventReturnMapids() {
        for (Entry<String, Integer> e : eventAreas.entrySet()) {
            eventAreas.put(e.getKey(), getOverworldMap(e.getValue()));
        }
    }
    
    private static void propagateEventRelatedReturnMapids() {
        for (Entry<String, Set<Integer>> e : eventAssociatedMapids.entrySet()) {
            Integer mainMapid = eventAreas.get(e.getKey());
            
            if (mainMapid != null) {
                for (Integer i : e.getValue()) {
                    returnAreas.put(i, mainMapid);
                }
            } else {
                System.out.println("[ERROR] Could not resolve main mapid for event '" + e.getKey() + "'");
            }
        }
        
        if (!eventMaxMapid.isEmpty()) { // size: [eventMinMapid] == [eventMaxMapid]
            Collections.sort(worldMapids);
            
            int cursor = eventMaxMapid.size();
            List<String> eventKeys = getEventKeysOrderedByMinMapid();
            for (String ek : eventKeys) {
                cursor = propagateEventReturnMapids(ek, cursor);
            }
        }
    }
    
    private static void backpropagateEventAreasReturnMapids() {
        for (Entry<String, Integer> e : eventAreas.entrySet()) {
            Integer linkedId = getBaseReturnMapid(e.getValue());
            
            Integer curRetId = e.getValue();
            if (!worldmapAreas.containsKey(linkedId) || !shouldLinkMaps(curRetId, linkedId)) {
                continue;
            }
            
            String eventName = e.getKey();
            eventAreas.put(e.getKey(), linkedId);
        }
    }
    
    private static void propagateOverworldMapReferrers() {
        generateOverworldMapReferrers(npcAreas);
        generateOverworldMapReferrers(questAreas);
        generateOverworldMapReferrers(reactorAreas);
        generateOverworldMapReferrers(mapScriptAreas);
        generateOverworldMapReferrers(portalAreas);
    }
    
    private static String reportTownMapStatus(int retMapid) {
        return worldmapAreas.containsKey(retMapid) ? "" : " : not overworld";
    }
    
    private static List<Entry<Integer, Integer>> getOrderedMap1(Set<Entry<Integer, Integer>> entrySet) {
        List<Entry<Integer, Integer>> list = new ArrayList<>(entrySet);
        
        Collections.sort(list, new Comparator<Entry<Integer, Integer>>() {
            @Override
            public int compare(Entry<Integer, Integer> p1, Entry<Integer, Integer> p2) {
                return p1.getKey().compareTo(p2.getKey());
            }
        });
        
        return list;
    }
    
    private static List<Entry<String, Set<Integer>>> getOrderedMap2(Set<Entry<String, Set<Integer>>> entrySet) {
        List<Entry<String, Set<Integer>>> list = new ArrayList<>(entrySet);
        
        Collections.sort(list, new Comparator<Entry<String, Set<Integer>>>() {
            @Override
            public int compare(Entry<String, Set<Integer>> p1, Entry<String, Set<Integer>> p2) {
                return p1.getKey().compareTo(p2.getKey());
            }
        });
        
        return list;
    }
    
    private static List<Entry<Integer, Map<Integer, Integer>>> getOrderedMap3(Set<Entry<Integer, Map<Integer, Integer>>> entrySet) {
        List<Entry<Integer, Map<Integer, Integer>>> list = new ArrayList<>(entrySet);
        
        Collections.sort(list, new Comparator<Entry<Integer, Map<Integer, Integer>>>() {
            @Override
            public int compare(Entry<Integer, Map<Integer, Integer>> p1, Entry<Integer, Map<Integer, Integer>> p2) {
                return p1.getKey().compareTo(p2.getKey());
            }
        });
        
        return list;
    }
    
    private static void generateOverworldMapReferrers(Map<?, Set<Integer>> map) {
        for (Set<Integer> v : map.values()) {
            Set<Integer> refMapids = new HashSet<>();
            for (Integer i : v) {
                if (worldmapAreas.containsKey(i)) {
                    refMapids.add(i);
                }
            }
            
            if (!refMapids.isEmpty()) {
                for (Integer i : refMapids) {
                    Set<Integer> mapRefs = linkedMapAreas.get(i);

                    if (mapRefs == null) {
                        mapRefs = new HashSet<>();
                        linkedMapAreas.put(i, mapRefs);
                    }

                    mapRefs.addAll(refMapids);
                }
            }
        }
    }
    
    private static int bfsOverworldMapid(int mapid, Set<Integer> path) {
        Set<Integer> neighborMaps = portalRetAreas.get(mapid);
        if (neighborMaps == null) {
            return -1;
        }
        
        Set<Integer> viewMaps = new HashSet<>(neighborMaps.size());
        for (Integer neighborId : neighborMaps) {
            if (worldmapAreas.containsKey(neighborId)) {
                return neighborId;
            }
            
            if (!path.contains(neighborId)) {
                viewMaps.add(neighborId);
                path.add(neighborId);
            }
        }
        
        for (Integer i : viewMaps) {
            int ret = bfsOverworldMapid(i, path);
            if (ret != -1) {
                return ret;
            }
        }
        return -1;
    }
    
    private static int getOverworldMapInternal(int mapid) {
        if (worldmapAreas.containsKey(mapid)) {
            return mapid;
        }
        
        Set<Integer> path = new HashSet<>();
        Integer retMap = bfsOverworldMapid(mapid, path);
        if (retMap != -1) {
            return retMap;
        }
        
        retMap = returnAreas.get(mapid);
        if (retMap == null || !worldmapAreas.containsKey(retMap)) {
            Set<Integer> referrers = linkedMapAreas.get(mapid);
            
            if (referrers != null && !referrers.isEmpty()) {
                retMap = getMinimumElement(referrers);
            } else {
                retMap = mapid;
            }
        }
        
        return retMap;
    }
    
    private static int getOverworldMap(int mapid) {
        Integer omapId = overworldMapids.get(mapid);
        if (omapId == null) {
            omapId = getOverworldMapInternal(mapid);
            overworldMapids.put(mapid, omapId);
        }
        
        return omapId;
    }
    
    private static String padWithZeroes(int number, int size) {
        return String.format("%0" + size + "d", number);
    }
    
    private static boolean isScriptExtension(Pair<String, String> codePathExtension) {
        return codePathExtension.getRight().endsWith(".js");
    }
    
    private static void printWorldScannerResults(String outputName, List<Pair<String, List<Integer>>> itemPathMapid) {
        try {
            printWriter = new PrintWriter(scannerPath + "/" + fileIndex + "_" + outputName, "UTF-8");
            fileIndex += 1;
            
            for (Pair<String, List<Integer>> p : itemPathMapid) {
                printWriter.print(p.getLeft() + " ");
                for (Integer i : p.getRight()) {
                    printWriter.print(i + " ");
                }
                printWriter.println();
            }
            
            printWriter.close();
        } catch (IOException ioe) {
            ioe.printStackTrace();
        }
    }
    
    private static void reportMappedResults3(String outputName, List<Pair<String, String>> codePathExtension, Map<Integer, Integer> map) {
        try {
            printWriter = new PrintWriter(outputPath + "/" + fileIndex + "_" + outputName, "UTF-8");
            
            List<Pair<String, List<Integer>>> itemPathMapid = new ArrayList<>();
            
            List<Entry<Integer, Integer>> orderedMap = getOrderedMap1(map.entrySet());
            for(Entry<Integer, Integer> e : orderedMap) {
                int retMapid = getOverworldMap(e.getKey());
                printWriter.println(e.getKey() + "\t" + retMapid + reportTownMapStatus(retMapid) + " " + e.getValue() + reportTownMapStatus(e.getValue()));
                
                for (Pair<String, String> pe : codePathExtension) {
                    itemPathMapid.add(new Pair<>(pe.getLeft() + (e.getKey() / 100000000) + "/" + padWithZeroes(e.getKey(), isScriptExtension(pe) ? 1 : 9) + pe.getRight(), Collections.singletonList(retMapid)));
                }
            }

            printWriter.close();
            printWorldScannerResults(outputName, itemPathMapid);
        } catch (IOException ioe) {
            ioe.printStackTrace();
        }
    }
    
    private static void reportMappedResults4(String outputName, List<Pair<String, String>> codePathExtension, Map<Integer, Map<Integer, Integer>> map) {
        try {
            printWriter = new PrintWriter(outputPath + "/" + fileIndex + "_" + outputName, "UTF-8");
            
            List<Pair<String, List<Integer>>> itemPathMapid = new ArrayList<>();
            
            List<Entry<Integer, Map<Integer, Integer>>> orderedMap = getOrderedMap3(map.entrySet());
            for(Entry<Integer, Map<Integer, Integer>> e : orderedMap) {
                int mobid = e.getKey();
                printWriter.print(mobid + "\t");
                
                List<Entry<Integer, Integer>> orderedMap2 = getOrderedMap1(e.getValue().entrySet());
                List<Integer> list = new ArrayList<>(orderedMap2.size());
                for(Entry<Integer, Integer> e2 : orderedMap2) {
                    int retMapid = e2.getKey();
                    printWriter.print(MapleMapNameReader.getMapName(retMapid) + " (" + retMapid + ") " + reportTownMapStatus(retMapid) + " ");
                    list.add(retMapid);
                }
                printWriter.println();
                
                for (Pair<String, String> pe : codePathExtension) {
                    itemPathMapid.add(new Pair<>(pe.getLeft() + padWithZeroes(mobid, isScriptExtension(pe) ? 1 : 7) + pe.getRight(), list));
                }
            }

            printWriter.close();
            printWorldScannerResults(outputName, itemPathMapid);
        } catch (IOException ioe) {
            ioe.printStackTrace();
        }
    }
    
    private static void reportMappedResults1(String outputName, List<Pair<String, String>> codePathExtension, Map<String, Integer> map) {
        Map<String, Set<Integer>> rmap = new HashMap<>(map.size());
        
        for (Entry<String, Integer> e : map.entrySet()) {
            HashSet<Integer> v = new HashSet<>(1);
            v.add(e.getValue());
            
            String eventName = e.getKey();
            rmap.put(eventName.substring(0, eventName.length() - 3), v);
        }
        
        reportMappedResults(outputName, codePathExtension, rmap);
    }
    
    private static void reportMappedResults2(String outputName, List<Pair<String, String>> codePathExtension, Map<Integer, Set<Integer>> map) {
        for (Pair<String, String> pe : codePathExtension) {
            Map<String, Set<Integer>> rmap = new HashMap<>(map.size());
            
            if (!isScriptExtension(pe)) {
                for (Entry<Integer, Set<Integer>> e : map.entrySet()) {
                    rmap.put(padWithZeroes(e.getKey(), 7), e.getValue());
                }
            } else {
                for (Entry<Integer, Set<Integer>> e : map.entrySet()) {
                    rmap.put(padWithZeroes(e.getKey(), 1), e.getValue());
                }
            }
            
            reportMappedResults(outputName, Collections.singletonList(pe), rmap);
        }
    }
    
    private static void reportMappedResults(String outputName, List<Pair<String, String>> codePathExtension, Map<String, Set<Integer>> map) {
        try {
            printWriter = new PrintWriter(outputPath + "/" + fileIndex + "_" + outputName, "UTF-8");
            
            List<Pair<String, List<Integer>>> itemPathMapid = new ArrayList<>();
            
            List<Entry<String, Set<Integer>>> orderedMap = getOrderedMap2(map.entrySet());
            for(Entry<String, Set<Integer>> e : orderedMap) {
                Set<Integer> r = new HashSet<>();
                for (Integer i : e.getValue()) {
                    r.add(i);
                }
                r.remove(null);
                
                if (!r.isEmpty()) {
                    printWriter.print(e.getKey() + "\t");
                    
                    Set<Integer> printMapids = new HashSet<>(r.size());
                    for (Integer i : r) {
                        int retMapid = getOverworldMap(i);
                        printMapids.add(retMapid);
                    }
                    
                    if (!printMapids.isEmpty()) {
                        List<Integer> list = new ArrayList<>(printMapids);
                        Collections.sort(list);
                        for (Integer i : list) {
                            printWriter.print(MapleMapNameReader.getMapName(i) + " (" + i + ") " + reportTownMapStatus(i) + " ");
                        }
                        
                        for (Pair<String, String> pe : codePathExtension) {
                            itemPathMapid.add(new Pair<>(pe.getLeft() + e.getKey() + pe.getRight(), list));
                        }
                    }
                    printWriter.println();
                } else {
                    System.out.println("[MISSING INFO - " + outputName + "] " + e.getKey() + " has no associated area.");
                }
            }

            printWriter.close();
            printWorldScannerResults(outputName, itemPathMapid);
        } catch (IOException ioe) {
            ioe.printStackTrace();
        }
    }
    
    private static void reportScriptMappingResults() {
        reportMappedResults2("npc.txt", npcPathExtension, npcAreas);
        fileIndex = 0;
        
        reportMappedResults2("quest.txt", questPathExtension, questAreas);
        fileIndex = 0;
        
        reportMappedResults2("reactor.txt", reactorPathExtension, reactorAreas);
        fileIndex = 0;
        
        reportMappedResults("mapscript.txt", mapScriptPathExtension, mapScriptAreas);
        fileIndex = 0;
        
        reportMappedResults1("event.txt", eventPathExtension, eventAreas);
        fileIndex = 0;
        
        reportMappedResults("portal.txt", portalPathExtension, portalAreas);
        fileIndex = 0;
        
        reportMappedResults3("zmap.txt", zmapPathExtension, returnAreas);
        fileIndex = 0;
        
        reportMappedResults4("zmobs.txt", zmobPathExtension, mobAreas);
        fileIndex = 0;
    }
    
    private static void parseEventObjectScripts() {
        int state = 0;
        System.out.println("\nFetching maplinks from scripts");
        parseEventObjectScripts2("map/onUserEnter", mapScriptAreas, state);
        parseEventObjectScripts2("map/onFirstUserEnter", mapScriptAreas, state);
        parseEventObjectScripts1("quest", questAreas, state);
        parseEventObjectScripts1("reactor", reactorAreas, state);
        parseEventObjectScripts2("portal", portalAreas, state);
        parseEventObjectScripts1("npc", npcAreas, state);
        
        state = 1;
        System.out.println("\nFetching event references from scripts");
        parseEventObjectScripts2("map/onUserEnter", mapScriptAreas, state);
        parseEventObjectScripts2("map/onFirstUserEnter", mapScriptAreas, state);
        parseEventObjectScripts1("quest", questAreas, state);
        parseEventObjectScripts1("reactor", reactorAreas, state);
        parseEventObjectScripts2("portal", portalAreas, state);
        parseEventObjectScripts1("npc", npcAreas, state);
    }
    
    private static void parseMapObjectScripts() {
        int state = 2;
        parseEventObjectScripts2("map/onUserEnter", mapScriptAreas, state);
        parseEventObjectScripts2("map/onFirstUserEnter", mapScriptAreas, state);
        parseEventObjectScripts1("quest", questAreas, state);
        parseEventObjectScripts1("reactor", reactorAreas, state);
        parseEventObjectScripts2("portal", portalAreas, state);
        parseEventObjectScripts1("npc", npcAreas, state);
    }
    
    private static void generateRemissivePortalAreas() {
        for (Entry<String, Set<Integer>> e : portalAreas.entrySet()) {
            String pname = e.getKey();
            
            for (Integer i : e.getValue()) {
                Set<String> p = portalScripts.get(i);
                if (p == null) {
                    p = new HashSet<>();
                    portalScripts.put(i, p);
                }
                
                p.add(pname);
            }
        }
    }
    
    private static void propagateScriptedReturnPortals() {
        for (Entry<Integer, Set<String>> p : portalScripts.entrySet()) {
            
            Set<Integer> s = portalRetAreas.get(p.getKey());
            if (s == null) {
                s = new HashSet<>();
                portalRetAreas.put(p.getKey(), s);
            }
            
            for (String scriptPortal : p.getValue()) {
                Set<Integer> sp = portalAreas.get(scriptPortal);
                s.addAll(sp);
            }
        }
    }
    
    private static void reportOverworldMappingResults(String outputName, Map<Integer, Integer> map) {
        try {
            printWriter = new PrintWriter(scannerPath + "/" + outputName, "UTF-8");
            
            List<Entry<Integer, Integer>> orderedMap = getOrderedMap1(map.entrySet());
            for(Entry<Integer, Integer> e : orderedMap) {
                printWriter.println(e.getKey() + "\t" + e.getValue() + "\t" + reportTownMapStatus(e.getValue()));
            }

            printWriter.close();
        } catch (IOException ioe) {
            ioe.printStackTrace();
        }
    }
    
    public static void main(String[] args) {
        worldmapAreas = MapleWorldMapReader.parseWorldMapAreas();
        
        System.out.println("Parsing Map.wz");
        parseMapwzDirectory();
        
        System.out.println("Parsing Quest.wz");
        parseQuestwzFile(new File(wzPath + "/Quest.wz/Check.img.xml"));
        MapleMapNameReader.parseMapNames();
        
        System.out.println("\nParsing server scripts");
        parseMapObjectScripts();
        parseEventScripts();
        parseEventObjectScripts();
        
        System.out.println("\nPropagating linked maps update");
        generateRemissivePortalAreas();
        propagateScriptedReturnPortals();
        propagateLinkedReturnMapids();
        
        System.out.println("\nPropagating event maps update");
        propagateOverworldEventReturnMapids();
        propagateEventRelatedReturnMapids();
        
        System.out.println("\nPropagating resulting overworld map links");
        propagateOverworldMapReferrers();
        
        System.out.println("\nBackpropagating event area update");
        backpropagateEventAreasReturnMapids();
        
        System.out.println("\nReporting results");
        reportScriptMappingResults();
        reportOverworldMappingResults("overworld.txt", overworldMapids);
    }
}
