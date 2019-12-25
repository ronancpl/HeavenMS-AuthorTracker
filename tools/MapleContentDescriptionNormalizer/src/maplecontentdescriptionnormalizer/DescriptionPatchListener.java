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

import antlr.DescriptionPatchParser;
import antlr.DescriptionPatchParserBaseListener;
import java.util.Collections;
import org.antlr.v4.runtime.ParserRuleContext;
import org.antlr.v4.runtime.tree.TerminalNode;

import java.util.List;
import java.util.LinkedList;

/**
 *
 * @author RonanLana
 */
public class DescriptionPatchListener extends DescriptionPatchParserBaseListener {
    
    private int currentItemid;
    private boolean currentSkillUpgradeBook;
    private boolean currentIsDescription;
    private String currentDescription;
    
    private int patchCursor = 0;
    
    private PatchDescriptionMetadata patches = new PatchDescriptionMetadata();
    
    private List<Integer> patchPos = patches.getPatchPos();
    private List<Integer> patchLastSize = patches.getPatchLastSize();
    private List<String> patchContent = patches.getPatchContent();
    
    private boolean hasDanglingR, pruneDanglingR;
    private boolean hasDanglingN, pruneDanglingN;
    
    public DescriptionPatchListener(int itemid, boolean description) {
        super();
        setDescriptionPatchMetadata(itemid, description);
    }
    
    private void setDescriptionPatchMetadata(int itemid, boolean description) {
        currentItemid = itemid;
        currentSkillUpgradeBook = (itemid >= 2280000 && itemid < 2300000);
        currentIsDescription = description;
    }
    
    private boolean mergeDanglingRIntoTextSpec(DescriptionPatchParser.PotentialConflictSpecContext ctx) {
        DescriptionPatchParser.ExpectedLineBreakSpecContext ectx = ctx.lineBreakMaybeCodeSpec().expectedLineBreakSpec();
        return ectx.expectedCarriageReturnSpec() != null && ectx.expectedCarriageReturnSpec().TARGET_BACKSLASH() == null;
    }
    
    private boolean mergeDanglingNIntoTextSpec(DescriptionPatchParser.PotentialConflictSpecContext ctx) {
        return ctx.whitespaceOrLineBreakSpec().get(0).expectedLineBreakSpec() != null;
    }
    
    private String patchTextSpec(DescriptionPatchParser.TextSpecContext ctx) {
        return ctx.getText();
    }
    
    private String patchExpectedLineBreakSpec(DescriptionPatchParser.ExpectedLineBreakSpecContext ctx) {
        String patch = "";
        if (ctx.expectedCarriageReturnSpec() != null) {
            if (pruneDanglingR) {
                pruneDanglingR = false;
            } else {
                patch += "\\r";
            }
        }
        patch += "\\n";
        
        return patch;
    }
    
    private String patchDOT(List<DescriptionPatchParser.DotSpecContext> dot) {
        int dotSize = dot.size();
        
        if (dotSize < 1) {
            return currentSkillUpgradeBook ? "" : ".";
        } else {
            String dotType = dot.get(0).getText();
            
            if (dotSize < 3) {
                return dotType;
            } else {
                return dotType + dotType + dotType;
            }
        }
    }
    
    private String patchSIGN(List<TerminalNode> dot) {
        int dotSize = dot.size();
        
        if (dotSize < 1) {
            return ".";
        } else {
            String dotType = dot.get(0).getText();
            
            if (dotSize < 3) {
                return dotType;
            } else {
                return dotType + dotType + dotType;
            }
        }
    }
    
    private String patchLineBreakContent(DescriptionPatchParser.ExpectedLineBreakSpecContext ctx) {
        String patch = "";
        
        if (ctx.expectedCarriageReturnSpec() != null) {
            if (ctx.expectedCarriageReturnSpec().TARGET_BACKSLASH() == null) {
                patch += "\\";
            }
            
            patch += ctx.expectedCarriageReturnSpec().getText();
        }
        
        if (ctx.expectedLineForwardSpec().TARGET_BACKSLASH() == null) {
            patch += "\\";
        }

        patch += ctx.expectedLineForwardSpec().getText();
        return patch;
    }
    
    private List<String> patchWhitespaceOrLineBreakContent(List<DescriptionPatchParser.WhitespaceOrLineBreakSpecContext> ctxList, boolean dot) {
        String patch = "", text = "";
        
        if (!ctxList.isEmpty()) {
            int st = 0;
            if (pruneDanglingN) {
                pruneDanglingN = false;
                text = "";
                st = 1;
            } else {
                if (!dot) {
                    text = ctxList.get(0).getText();
                    st = 1;
                }
            }
            
            for (int i = st; i < ctxList.size(); i++) {
                DescriptionPatchParser.WhitespaceOrLineBreakSpecContext ctx = ctxList.get(i);
                
                if (ctx.expectedLineBreakSpec() != null) {
                    patch += patchLineBreakContent(ctx.expectedLineBreakSpec());
                }
            }
        }
        
        final String patchStr = patch, textStr = text;
        return new LinkedList<String>(){{add(textStr); add(patchStr);}};
    }
    
    private String patchWhitespaceBeforeKeywordSpecText(DescriptionPatchParser.WhitespaceBeforeKeywordSpecContext ctx) {
        return ctx != null ? " " : "";
    }
    
    private String patchCodeSpecText(DescriptionPatchParser.CodeSpecContext ctx) {
        return ctx != null ? "#c" : "";
    }
    
    private String patchLineBreakMaybeCodeSpecText(DescriptionPatchParser.LineBreakMaybeCodeSpecContext ctx) {
        return patchExpectedLineBreakSpec(ctx.expectedLineBreakSpec()) + patchCodeSpecText(ctx.codeSpec());
    }
    
    private boolean potentialConflictSpecParsePath(DescriptionPatchParser.PotentialConflictSpecContext ctx) {
        return ctx.dotSpec().isEmpty() && ctx.whitespaceOrLineBreakSpec().isEmpty() && ctx.whitespaceBeforeKeywordSpec() != null;
    }
    
    private String patchPotentialConflictSpecText(DescriptionPatchParser.PotentialConflictSpecContext ctx) {
        String patch = patchTextSpec(ctx.textSpec());
        
        if (!potentialConflictSpecParsePath(ctx)) {
            pruneDanglingR = hasDanglingR;
            if (hasDanglingR) {
                patch += "r";
            } else {
                pruneDanglingN = hasDanglingN;
                if (hasDanglingN) {
                    patch += "n";
                }
            }
            
            if (!(ctx.anyKeywordSpec().NUMBER() != null && ctx.whitespaceBeforeKeywordSpec() == null && ctx.whitespaceOrLineBreakSpec().isEmpty())) {
                List<String> wslbContent = patchWhitespaceOrLineBreakContent(ctx.whitespaceOrLineBreakSpec(), ctx.dotSpec().size() > 0);
                patch += "";
                patch += patchDOT(ctx.dotSpec());
                patch += wslbContent.get(1);
            }
            
            patch += patchLineBreakMaybeCodeSpecText(ctx.lineBreakMaybeCodeSpec());
        } else {
            patch += patchLineBreakMaybeCodeSpecText(ctx.lineBreakMaybeCodeSpec());
            patch += patchWhitespaceBeforeKeywordSpecText(ctx.whitespaceBeforeKeywordSpec());
        }
        
        patch += ctx.anyKeywordSpec().getText();
        
        return patch;
    }
    
    @Override
    public void enterPotentialConflictSpec(DescriptionPatchParser.PotentialConflictSpecContext ctx) {
        hasDanglingR = false;
        hasDanglingN = false;
        
        if (ctx.dotSpec().isEmpty()) {
            if (currentSkillUpgradeBook) {
                updatePatchCursor(ctx);
                return;
            }
            
            if (ctx.whitespaceBeforeKeywordSpec() != null) {    // is white-spaced
                if (ctx.whitespaceOrLineBreakSpec().isEmpty()) {
                    updatePatchCursor(ctx);
                    return;
                }
            } else {
                if (ctx.whitespaceOrLineBreakSpec().isEmpty()) {
                    if (mergeDanglingRIntoTextSpec(ctx)) {
                        hasDanglingR = true;
                    }
                } else {
                    if (mergeDanglingNIntoTextSpec(ctx)) {
                        hasDanglingN = true;
                    }
                }
            }
            
            String patch = patchPotentialConflictSpecText(ctx);
            //System.out.println("missing DOT: '" + ctx.getText() + "' " + (hasDanglingR ? "(r is text) " : "") + (hasDanglingN ? "(n is text) " : "") + "in '" + currentDescription + "' >> '" + patch + "'");
            addPatch(ctx, patch);
        } else {
            String patch = patchPotentialConflictSpecText(ctx);
            //System.out.println("missing '\\': '" + ctx.getText() + "' in '" + currentDescription + "' >> '" + patch + "'");
            addPatch(ctx, patch);
        }
        
        updatePatchCursor(ctx);
    }
    
    private String patchSignMaybeWhitespaceSpecText(DescriptionPatchParser.SignMaybeWhitespaceSpecContext ctx) {
        return patchSIGN(ctx.SIGN());
    }
    
    private String patchSignConflictSpecText(DescriptionPatchParser.SignConflictSpecContext ctx) {
        String patch = patchTextSpec(ctx.textSpec());
        
        pruneDanglingR = hasDanglingR;
        if (hasDanglingR) {
            patch += "r";
        } else {
            pruneDanglingN = hasDanglingN;
            if (hasDanglingN) {
                patch += "n";
            }
        }
        
        List<String> wslbContent = patchWhitespaceOrLineBreakContent(ctx.whitespaceOrLineBreakSpec(), ctx.signMaybeWhitespaceSpec().SIGN().size() > 0);
        
        patch += wslbContent.get(0);
        patch += patchSignMaybeWhitespaceSpecText(ctx.signMaybeWhitespaceSpec());
        patch += (wslbContent.get(1).isEmpty() ? " " : wslbContent.get(1));
        patch += ctx.anyKeywordSpec().getText();
        
        return patch;
    }
    
    @Override
    public void enterSignConflictSpec(DescriptionPatchParser.SignConflictSpecContext ctx) {
        hasDanglingR = false;
        
        String patch = patchSignConflictSpecText(ctx);
        //System.out.println("missing '\\n': '" + ctx.getText() + "' in '" + currentDescription + "' >> '" + patch + "'");
        addPatch(ctx, patch);
        
        updatePatchCursor(ctx);
    }
    
    private String getSignedToken(DescriptionPatchParser.MoreConflictSpecContext ctx) {
        if (ctx.TARGET_PLUS() != null) {
            return ctx.TARGET_PLUS().getText();
        } else {
            return ctx.TARGET_MINUS().getText();
        }
    }
    
    private String patchMoreConflictSpecText(DescriptionPatchParser.MoreConflictSpecContext ctx) {
        String patch = "";
        
        if (ctx.WS() != null) {
            patch += " ";
        } else if (ctx.NUMBER() == null) {
            patch += patchDOT(ctx.dotSpec());
        } else {
            if (ctx.dotSpec().size() > 0) {
                patch += ctx.dotSpec().get(0).getText();
                patch += " ";
            }
            
            patch += getSignedToken(ctx) + ctx.NUMBER();
            
            if (ctx.spacedDotSpec() != null) {
                patch += patchDOT(Collections.singletonList(ctx.spacedDotSpec().dotSpec()));
            }
        }
        
        return patch;
    }
    
    @Override
    public void enterMoreConflictSpec(DescriptionPatchParser.MoreConflictSpecContext ctx) {
        String patch = patchMoreConflictSpecText(ctx);
        //System.out.println("conflict: '" + ctx.getText() + "' in '" + currentDescription + "' >> '" + patch + "'");
        addPatch(ctx, patch);
        
        updatePatchCursor(ctx);
    }
        
    @Override
    public void enterIgnoreSpec(DescriptionPatchParser.IgnoreSpecContext ctx) {
        //System.out.println("ignore: '" + ctx.getText() + "'");
        updatePatchCursor(ctx);
    }
    
    @Override
    public void enterCompilationUnit(DescriptionPatchParser.CompilationUnitContext ctx) {
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
