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
import java.util.HashMap;
import java.util.Map;

/**
 *
 * @author RonanLana
 */
public class MapleMapNameReader {
    
    static InputStreamReader fileReader = null;
    static BufferedReader bufferedReader = null;
    
    static String stringMapWzXml = "../../../HeavenMS/wz/String.wz/Map.img.xml";
    
    static int initialStringLength = 250;
    static byte status;
    
    static String curStreetName;
    static String curMapName;
    static Integer curMapId;
    static Map<Integer, Pair<String, String>> mapNames = new HashMap<>();
    
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
    
    private static void translateToken(String token) {
        if(token.contains("/imgdir")) {
            status -= 1;
            
            if (status == 2) {
                mapNames.put(curMapId, new Pair<>(curMapName, curStreetName));
            }
        }
        else if(token.contains("imgdir")) {
            status += 1;
            
            if (status == 3) {
                curMapId = Integer.valueOf(getName(token));
            }
        }
        else {
            if (status == 3) {
                String d = getName(token);
                
                switch (d) {
                    case "mapName":
                        curMapName = getValue(token);
                        break;
                        
                    case "streetName":
                        curStreetName = getValue(token);
                        break;
                }
            }
        }
    }
    
    private static void parseMapNamesFile(File file) {
        // This will reference one line at a time
        String line = null;
        
        try {
            curMapName = "";
            curStreetName = "";
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
    
    public static void parseMapNames() {
        parseMapNamesFile(new File(stringMapWzXml));
    }
    
    public static String getMapName(int mapid) {
        try {
            return mapNames.get(mapid).getLeft();
        } catch (NullPointerException npe) {
            return "" + mapid;
        }
    }
}
