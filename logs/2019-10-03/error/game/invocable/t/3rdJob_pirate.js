scripts/event/3rdJob_pirate.js
javax.script.ScriptException: <eval>:1:18 Expected ; but found error
java.io.FileReader@e24ddd0
                  ^ in <eval> at line number 1 at column number 18
	at jdk.nashorn.api.scripting.NashornScriptEngine.throwAsScriptException(NashornScriptEngine.java:467)
	at jdk.nashorn.api.scripting.NashornScriptEngine.compileImpl(NashornScriptEngine.java:534)
	at jdk.nashorn.api.scripting.NashornScriptEngine.compileImpl(NashornScriptEngine.java:521)
	at jdk.nashorn.api.scripting.NashornScriptEngine.evalImpl(NashornScriptEngine.java:399)
	at jdk.nashorn.api.scripting.NashornScriptEngine.eval(NashornScriptEngine.java:155)
	at javax.script.AbstractScriptEngine.eval(Unknown Source)
	at scripting.AbstractScriptManager.getScriptEngine(AbstractScriptManager.java:92)
	at scripting.event.EventScriptManager.<init>(EventScriptManager.java:57)
	at net.server.channel.Channel.<init>(Channel.java:144)
	at net.server.Server.initWorld(Server.java:419)
	at net.server.Server.init(Server.java:917)
	at net.server.Server.main(Server.java:961)
Caused by: jdk.nashorn.internal.runtime.ParserException: <eval>:1:18 Expected ; but found error
java.io.FileReader@e24ddd0
                  ^
	at jdk.nashorn.internal.parser.AbstractParser.error(AbstractParser.java:292)
	at jdk.nashorn.internal.parser.AbstractParser.error(AbstractParser.java:277)
	at jdk.nashorn.internal.parser.AbstractParser.expectDontAdvance(AbstractParser.java:348)
	at jdk.nashorn.internal.parser.AbstractParser.expect(AbstractParser.java:335)
	at jdk.nashorn.internal.parser.Parser.endOfLine(Parser.java:3372)
	at jdk.nashorn.internal.parser.Parser.expressionStatement(Parser.java:1160)
	at jdk.nashorn.internal.parser.Parser.statement(Parser.java:967)
	at jdk.nashorn.internal.parser.Parser.sourceElements(Parser.java:773)
	at jdk.nashorn.internal.parser.Parser.program(Parser.java:709)
	at jdk.nashorn.internal.parser.Parser.parse(Parser.java:283)
	at jdk.nashorn.internal.parser.Parser.parse(Parser.java:249)
	at jdk.nashorn.internal.runtime.Context.compile(Context.java:1286)
	at jdk.nashorn.internal.runtime.Context.compileScript(Context.java:1253)
	at jdk.nashorn.internal.runtime.Context.compileScript(Context.java:625)
	at jdk.nashorn.api.scripting.NashornScriptEngine.compileImpl(NashornScriptEngine.java:532)
	... 10 more

---------------------------------

