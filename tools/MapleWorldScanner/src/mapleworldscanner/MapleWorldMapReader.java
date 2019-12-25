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
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 *
 * @author RonanLana
 */
public class MapleWorldMapReader {
    
    static InputStreamReader fileReader = null;
    static BufferedReader bufferedReader = null;
    
    static String worldmapWzPath = "../../../HeavenMS/wz/Map.wz/WorldMap";
    
    static int initialStringLength = 250;
    static byte status;
    
    static Integer curWorldmap;
    static Pair<Integer, Integer> curSpot;
    static Set<Integer> curMapids;
    static Map<Integer, Map<Integer, WorldMapSpot>> worldmapAreas = new HashMap<>();
    
    public static class WorldMapSpot {
        protected Pair<Integer, Integer> pos;
        
        protected WorldMapSpot(Pair<Integer, Integer> spot) {
            pos = spot;
        }
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
    
    private static Pair<Integer, Integer> getVector(String token) {
        int i, j;
        i = token.lastIndexOf("x=");
        i = token.indexOf("\"", i) + 1; //lower bound of the string
        j = token.indexOf("\"", i);     //upper bound
        int x = Integer.valueOf(token.substring(i, j));
        
        token = token.substring(j + 1);
        
        i = token.lastIndexOf("y=");
        i = token.indexOf("\"", i) + 1; //lower bound of the string
        j = token.indexOf("\"", i);     //upper bound
        int y = Integer.valueOf(token.substring(i, j));
        
        return new Pair<>(x, y);
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
        if(token.contains("/imgdir")) {
            status -= 1;
            
            if (status == 2) {
                if (!curMapids.isEmpty()) {
                    WorldMapSpot spot = new WorldMapSpot(curSpot);
                    
                    for (Integer i : curMapids) {
                        Map<Integer, WorldMapSpot> worldPos = worldmapAreas.get(i);
                        if (worldPos == null) {
                            worldPos = new HashMap<>(3);
                            worldmapAreas.put(i, worldPos);
                        }
                        
                        worldPos.put(curWorldmap, spot);
                    }
                }
            }
        }
        else if(token.contains("imgdir")) {
            status += 1;
            
            if (status == 2) {
                String d = getName(token);
                if (!d.contentEquals("MapList")) {
                    forwardCursor(status);
                }
            } else if (status == 3) {
                curSpot = null;
                curMapids = new HashSet<>();
            } else if (status == 4) {
                String d = getName(token);
                if (!d.contentEquals("mapNo")) {
                    forwardCursor(status);
                }
            }
        }
        else {
            if (status == 4) {
                curMapids.add(Integer.valueOf(getValue(token)));
            } else if (status == 3) {
                if (getName(token).contentEquals("spot")) {
                    curSpot = getVector(token);
                }
            }
        }
    }
    
    private static int getWorldMapId(String filename) {
        try {
            return Integer.valueOf(filename.substring(8, filename.indexOf(".img")));
        } catch (NumberFormatException nfe) {
            return -1;
        }
    }
    
    public static void parseWorldMapFile(File file) {
        // This will reference one line at a time
        String line = null;
        
        try {
            curWorldmap = getWorldMapId(file.getName());
            status = 0;
            
            fileReader = new InputStreamReader(new FileInputStream(file), "UTF-8");
            bufferedReader = new BufferedReader(fileReader);

            while((line = bufferedReader.readLine()) != null) {
                translateToken(line);
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
            if (file.isFile()) {
                files.add(file);
            }
        }
    }
    
    public static Map<Integer, Map<Integer, WorldMapSpot>> parseWorldMapAreas() {
        System.out.println("Parsing World Maps");
        worldmapAreas.clear();
        
        ArrayList<File> files = new ArrayList<>();
        listFiles(worldmapWzPath, files);
        
        for (File f : files) {
            parseWorldMapFile(f);
        }
        
        return worldmapAreas;
    }
}
