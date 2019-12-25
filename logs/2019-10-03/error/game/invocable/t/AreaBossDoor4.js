scripts/event/AreaBossDoor4.js
javax.script.ScriptException: <eval>:1:23 Missing space after numeric literal
java.io.FileReader@6537ac
                       ^ in <eval> at line number 1 at column number 23
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
Caused by: jdk.nashorn.internal.runtime.ParserException: <eval>:1:23 Missing space after numeric literal
java.io.FileReader@6537ac
                       ^
	at jdk.nashorn.internal.parser.Lexer.error(Lexer.java:1700)
	at jdk.nashorn.internal.parser.Lexer.scanNumber(Lexer.java:1135)
	at jdk.nashorn.internal.parser.Lexer.lexify(Lexer.java:1614)
	at jdk.nashorn.internal.parser.AbstractParser.getToken(AbstractParser.java:132)
	at jdk.nashorn.internal.parser.AbstractParser.nextToken(AbstractParser.java:211)
	at jdk.nashorn.internal.parser.AbstractParser.nextOrEOL(AbstractParser.java:170)
	at jdk.nashorn.internal.parser.AbstractParser.next(AbstractParser.java:157)
	at jdk.nashorn.internal.parser.Parser.parse(Parser.java:281)
	at jdk.nashorn.internal.parser.Parser.parse(Parser.java:249)
	at jdk.nashorn.internal.runtime.Context.compile(Context.java:1286)
	at jdk.nashorn.internal.runtime.Context.compileScript(Context.java:1253)
	at jdk.nashorn.internal.runtime.Context.compileScript(Context.java:625)
	at jdk.nashorn.api.scripting.NashornScriptEngine.compileImpl(NashornScriptEngine.java:532)
	... 10 more

---------------------------------

