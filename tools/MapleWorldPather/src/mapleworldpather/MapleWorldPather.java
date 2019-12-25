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
package mapleworldpather;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;
import java.util.Stack;
import org.apache.commons.io.FileUtils;

/**
 *
 * @author Ronan
 */
public class MapleWorldPather {
    
    static PrintWriter printWriter;
    
    static InputStreamReader fileReader = null;
    static BufferedReader bufferedReader = null;
    
    static String basePath = "../../../HeavenMS";
    static String portalScriptPath = "../../../HeavenMS/scripts/portal";
    static String libPath = "lib";
    
    static int initialLength = 200;
    static int initialStringLength = 50;
    
    static byte status = 0;
    
    static int currentMapid;
    static Set<Integer> mapLinks;
    static Set<String> mapScripts;
    
    static String portalScript;
    static int portalMapid;
    
    static Map<Integer, Set<Integer>> worldmapLinks = new HashMap<>();
    static Map<Integer, Set<Integer>> worldmapNeighbors = new HashMap<>();
    
    private static String getName(String token) {
        int i, j;
        char[] dest;
        String d;

        i = token.lastIndexOf("name");
        i = token.indexOf("\"", i) + 1; //lower bound of the string
        j = token.indexOf("\"", i);     //upper bound

        dest = new char[initialStringLength];
        token.getChars(i, j, dest, 0);

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
    
    private static void translateToken(String token) {
        String d;
        
        if(token.contains("/imgdir")) {
            status -= 1;
            
            if (status == 2) {
                if (portalScript.isEmpty()) {
                    if (portalMapid > -1 && portalMapid < 999999999) {
                        mapLinks.add(portalMapid);
                    }
                } else {
                    mapScripts.add(portalScript);
                }
            }
        }
        else if(token.contains("imgdir")) {
            status += 1;
            
            if(status == 2) {
                if (!getName(token).contentEquals("portal")) {
                    forwardCursor(status);
                }
            } else if (status == 3) {
                portalScript = "";
                portalMapid = 999999999;
            }
        }
        else {
            if (status == 3) {
                if (getName(token).contentEquals("tm")) {
                    portalMapid = Integer.valueOf(getValue(token));
                } else if (getName(token).contentEquals("script")) {
                    portalScript = getValue(token);
                }
            }
        }
    }

    private static void readWzMapidData(File f) throws IOException {
        String line;
        
        mapLinks = new HashSet<>();
        mapScripts = new HashSet<>();
        
        fileReader = new InputStreamReader(new FileInputStream(f), "UTF-8");
        bufferedReader = new BufferedReader(fileReader);

        while((line = bufferedReader.readLine()) != null) {
            translateToken(line);
        }

        bufferedReader.close();
        fileReader.close();
    }
    
    private static void parseMapleWorldScriptLinks() {
        for (String script : mapScripts) {
            parseLinkedMapidFromScript(script);
        }
    }
    
    private static String getFileContent(File file) throws IOException {
        String fileContent = FileUtils.readFileToString(file, "UTF-8");
        fileContent = fileContent.replace(" ", "");
        
        return fileContent;
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
    
    private static void parseLinkedMapidFromScript(String eventObject) {
        String[] wsearchStr = new String[]{".warp(", ".changeMap("};
        File file = new File(portalScriptPath + "/" + eventObject + ".js");
        if (!file.exists()) {
            return;
        }

        Set<Integer> warpMapids = getWarpDescriptionsFromMatchingDataSearch(file, wsearchStr);
        if (!warpMapids.isEmpty()) {
            warpMapids.remove(100000000);
            mapLinks.addAll(warpMapids);
        }
    }
    
    private static void fetchMapleWorldMapNeighbors(File f) {
        mapLinks = new HashSet<>();
        mapScripts = new HashSet<>();
        
        currentMapid = Integer.valueOf(f.getName().substring(0, f.getName().indexOf('.')));
        try {
            readWzMapidData(f);
            parseMapleWorldScriptLinks();
        } catch (IOException ioe) {
            ioe.printStackTrace();
        }
        
        worldmapLinks.put(currentMapid, mapLinks);
    }
    
    private static void generateMapleWorldPath() {
        File dir = new File(basePath + "/wz/Map.wz/Map");
        
        for (File d : dir.listFiles()) {
            if (d.isDirectory()) {
                for (File f : d.listFiles()) {
                    fetchMapleWorldMapNeighbors(f);
                }
            }
        }
    }
    
    private static Set<Integer> visited;
    private static Stack<Integer> neighbors;
    private static Stack<Integer> nextNeighbors;
    private static int distance;
    
    private static Set<Integer> visitNode(int mapid) {
        visited.add(mapid);
        
        Set<Integer> links = worldmapLinks.get(mapid);
        return links != null ? links : new HashSet<Integer>();
        
    }
    
    private static void traverseMapleWorldCurrentVicinity() {
        neighbors = nextNeighbors;
        nextNeighbors = new Stack<>();
        
        while (!neighbors.isEmpty()) {
            Integer mapid = neighbors.pop();
            if (visited.contains(mapid)) continue;
            
            Set<Integer> newNeighbors = visitNode(mapid);
            nextNeighbors.addAll(newNeighbors);
        }
        
        distance += 1;
    }
    
    private static Set<Integer> runMapleWorldMapidVicinity(int mapid) {
        visited = new HashSet<>();
        neighbors = new Stack<>();
        nextNeighbors = new Stack<>();
        
        nextNeighbors.add(mapid);
        
        distance = -1;
        while (distance < 5) {
            traverseMapleWorldCurrentVicinity();
        }
        
        return visited;
    }
    
    private static void runMapleWorldVicinityScanner() {
        for (Integer mapid : worldmapLinks.keySet()) {
            Set<Integer> neighbors = runMapleWorldMapidVicinity(mapid);
            worldmapNeighbors.put(mapid, neighbors);
        }
    }
    
    private static List<Entry<Integer, Set<Integer>>> getOrderedMap(Set<Entry<Integer, Set<Integer>>> entrySet) {
        List<Entry<Integer, Set<Integer>>> list = new ArrayList<>(entrySet);
        
        Collections.sort(list, new Comparator<Entry<Integer, Set<Integer>>>() {
            @Override
            public int compare(Entry<Integer, Set<Integer>> p1, Entry<Integer, Set<Integer>> p2) {
                return p1.getKey().compareTo(p2.getKey());
            }
        });
        
        return list;
    }
    
    private static void printMapleWorldVicinityXmlHeader() {
        printWriter.println("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>");
        printWriter.println("<imgdir name=\"MapNeighbors.img\">");
        
    }
    
    private static void printMapleWorldVicinityXmlFooter() {
        printWriter.println("</imgdir>");
        
    }
    
    private static void printMapleWorldVicinitySql() {
        try {
            printWriter = new PrintWriter(libPath + "/MapNeighbors.img.xml", "UTF-8");
            
            printMapleWorldVicinityXmlHeader();
            
            List<Entry<Integer, Set<Integer>>> sortedEntries = getOrderedMap(worldmapNeighbors.entrySet());
            for (Entry<Integer, Set<Integer>> e : sortedEntries) {
                List<Integer> list = new ArrayList<>(e.getValue());
                
                if (!list.isEmpty()) {
                    int mapid = e.getKey();
                    printWriter.println("  <imgdir name=\"" + mapid + "\">");
                    
                    Collections.sort(list);
                    
                    int count = 0;
                    for (Integer neighborid : list) {
                        printWriter.println("    <int name=\"" + count + "\" value=\"" + neighborid + "\"/>");
                        count++;
                    }
                    
                    printWriter.println("  </imgdir>");
                }
            }
            
            printMapleWorldVicinityXmlFooter();
            
            printWriter.close();
        } catch (IOException ioe) {
            ioe.printStackTrace();
        }
    }
    
    public static void main(String[] args) {
        generateMapleWorldPath();
        runMapleWorldVicinityScanner();
        printMapleWorldVicinitySql();
    }
    
}
