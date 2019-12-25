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
package maplecontentdescriptionnormalizer;

import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.tree.ParseTree;

import antlr.DescriptionCodeLexer;
import antlr.DescriptionCodeParser;
import antlr.DescriptionPatchLexer;
import antlr.DescriptionPatchParser;
import java.io.BufferedReader;

import java.io.File;
import java.io.FileInputStream;
import java.io.InputStreamReader;

import java.io.IOException;
import java.io.PrintWriter;
import org.antlr.v4.runtime.tree.ParseTreeWalker;

/**
 *
 * @author RonanLana
 * 
 * This application solves several syntax issues from the item contents within
 * Consume.img.xml, generating a replica with normalized contents.
 * 
 * Estimated parse time: 10 seconds
 * 
 */
public class MapleContentDescriptionNormalizer {
    
    static PrintWriter printWriter = null;
    static InputStreamReader fileReader;
    static BufferedReader bufferedReader;
    
    static int initialLength = 200;
    static int initialStringLength = 500;
    
    static byte status = 0;
    
    static int currentItemid;
    static String currentName;
    static String currentDescription;
    
    private static String getType(String token) {
        int i, j;
        char[] dest;
        String d;

        i = token.indexOf("<") + 1;
        j = token.indexOf("name", i);     //upper bound

        dest = new char[initialStringLength];
        token.getChars(i, j, dest, 0);

        d = new String(dest);
        return(d.trim());
    }
    
    private static String getName(String token) {
        int i, j;
        char[] dest;
        String d;

        i = token.indexOf("name");
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

        i = token.indexOf("value");
        i = token.indexOf("\"", i) + 1; //lower bound of the string
        j = token.indexOf("\"", i);     //upper bound

        dest = new char[initialStringLength];
        token.getChars(i, j, dest, 0);

        d = new String(dest);
        return(d.trim());
    }
    
    private static void writeItemDescription() {
        printWriter.println(patchItemDescription("name", currentName));
        printWriter.println(patchItemDescription("desc", currentDescription));
    }
    
    private static void translateToken(String token) {
        if(token.contains("/imgdir")) {
            status -= 1;
            
            if (status == 1) {
                writeItemDescription();
            }
        }
        else if(token.contains("imgdir")) {
            status += 1;
            
            if (status == 2) {
                currentItemid = Integer.valueOf(getName(token));
                currentName = "";
                currentDescription = "";
            }
        }
        else {
            if (status == 2) {
                if (getName(token).contentEquals("desc")) {
                    currentDescription = getValue(token) + currentDescription;
                } else if (getType(token).startsWith("null")) {
                    String description = getName(token);
                    currentDescription += (description.startsWith("[") ? " " : "") + description;
                } else {
                    currentName = getValue(token);
                }
                
                return;
            }
        }
        
        printWriter.println(token);
    }
    
    private static String patchItemDescription(String name, String desc) {
        String res = parseDescriptionLineContent(desc, !name.contentEquals("name"));
        res = parseCodeLineContent(res);
        
        return "    <string name=\"" + name + "\" value=\"" + res + "\"/>";
    }
    
    private static String parseDescriptionPatches(String content, PatchDescriptionMetadata patches, boolean description) {
        String res = "";
        
        int idx = 0;
        for (int i = 0; i < patches.getPatchPos().size(); i++) {
            int curPos = patches.getPatchPos().get(i);
            int curLastSize = patches.getPatchLastSize().get(i);
            String curPatch = patches.getPatchContent().get(i);
            
            res += content.substring(idx, curPos);
            res += curPatch;
            idx = curPos + curLastSize;
        }
        
        res += content.substring(idx, content.length());
        
        if (description && !(res.matches(".*[.!?:;\\]]#*$"))) {
            res += ".";
        }
        
        return res;
    }
    
    private static String parseCodeLineContent(String content)  {
        DescriptionCodeLexer lexer = new DescriptionCodeLexer(CharStreams.fromString(content));
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        DescriptionCodeParser parser = new DescriptionCodeParser(tokens);
        
        ParseTree tree = parser.compilationUnit();
        DescriptionCodeListener listener = new DescriptionCodeListener(currentItemid);
        ParseTreeWalker walker = new ParseTreeWalker();
        walker.walk(listener, tree);
        
        String codePatch = parseDescriptionPatches(content, listener.exportDescriptionPatches(), false);
        return codePatch;
    }
    
    private static String parseDescriptionLineContent(String content, boolean description)  {
        DescriptionPatchLexer lexer = new DescriptionPatchLexer(CharStreams.fromString(content));
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        DescriptionPatchParser parser = new DescriptionPatchParser(tokens);
        
        ParseTree tree = parser.compilationUnit();
        DescriptionPatchListener listener = new DescriptionPatchListener(currentItemid, description);
        ParseTreeWalker walker = new ParseTreeWalker();
        walker.walk(listener, tree);
        
        String patchContent = parseDescriptionPatches(content, listener.exportDescriptionPatches(), description);
        return patchContent;
    }
    
    private static void parseDescriptionFile(String filePath, String outputFilePath) {
        try {
            File file = new File(filePath);
            
            printWriter = new PrintWriter(outputFilePath, "UTF-8");
            fileReader = new InputStreamReader(new FileInputStream(file), "UTF-8");
            bufferedReader = new BufferedReader(fileReader);

            String line;
            while((line = bufferedReader.readLine()) != null) {
                translateToken(line);
            }

            bufferedReader.close();
            fileReader.close();
            printWriter.close();
        } catch (IOException ioe) {
            ioe.printStackTrace();
        }
    }
    
    private static void deleteTemporaryFile(String filePath) {
        File file = new File(filePath);
        file.delete();
    }
    

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        parseDescriptionFile("../../../HeavenMS/wz/String.wz/Consume.img.xml", "temp.txt");
        parseDescriptionFile("temp.txt", "result.txt");   // normalize double-tangled description issues
        deleteTemporaryFile("temp.txt");
    }
    
}
