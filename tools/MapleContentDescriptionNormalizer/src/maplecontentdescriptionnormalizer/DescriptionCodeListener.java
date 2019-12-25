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

import antlr.DescriptionCodeParser;
import antlr.DescriptionCodeParserBaseListener;
import org.antlr.v4.runtime.ParserRuleContext;
import org.antlr.v4.runtime.tree.TerminalNode;

import java.util.List;

/**
 *
 * @author RonanLana
 */
public class DescriptionCodeListener extends DescriptionCodeParserBaseListener {
    
    private int currentItemid;
    private String currentDescription;
    
    private int patchCursor = 0;
    
    private PatchDescriptionMetadata patches = new PatchDescriptionMetadata();
    
    private List<Integer> patchPos = patches.getPatchPos();
    private List<Integer> patchLastSize = patches.getPatchLastSize();
    private List<String> patchContent = patches.getPatchContent();
    
    public DescriptionCodeListener(int itemid) {
        super();
        setDescriptionPatchMetadata(itemid);
    }
    
    private void setDescriptionPatchMetadata(int itemid) {
        currentItemid = itemid;
    }
    
    private String patchCodeTokenSpecText(DescriptionCodeParser.CodeTokenSpecContext ctx) {
        if (ctx.TOKEN_AMP() != null) return "&";
        if (ctx.TOKEN_APOS()!= null) return "\'";
        if (ctx.TOKEN_QUOT() != null) return "\"";
        return "";
    }
    
    @Override
    public void enterCodeTokenSpec(DescriptionCodeParser.CodeTokenSpecContext ctx) {
        String patch = patchCodeTokenSpecText(ctx);
        //System.out.println("code: '" + ctx.getText() + "' in '" + currentDescription + "' >> '" + patch + "'");
        addPatch(ctx, patch);
        
        updatePatchCursor(ctx);
    }
    
    @Override
    public void enterIgnoreSpec(DescriptionCodeParser.IgnoreSpecContext ctx) {
        //System.out.println("ignore: '" + ctx.getText() + "'");
        updatePatchCursor(ctx);
    }
    
    @Override
    public void enterCompilationUnit(DescriptionCodeParser.CompilationUnitContext ctx) {
        currentDescription = ctx.getText();
    }
    
    private void updatePatchCursor(ParserRuleContext ctx) {
        patchCursor += ctx.getText().length();
    }
    
    private void addPatch(ParserRuleContext ctx, String patch) {
        String text = ctx.getText();
        if (text.isEmpty()) {
            return;
        }
        
        patchPos.add(patchCursor);
        patchLastSize.add(text.length());
        patchContent.add(patch);
    }
    
    public PatchDescriptionMetadata exportDescriptionPatches() {
        return patches;
    }
    
}
