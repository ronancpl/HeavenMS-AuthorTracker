scripts/event/BalrogBattle.js
javax.script.ScriptException: ReferenceError: "importPackage" is not defined in <eval> at line number 26
	at jdk.nashorn.api.scripting.NashornScriptEngine.throwAsScriptException(NashornScriptEngine.java:470)
	at jdk.nashorn.api.scripting.NashornScriptEngine.evalImpl(NashornScriptEngine.java:454)
	at jdk.nashorn.api.scripting.NashornScriptEngine.evalImpl(NashornScriptEngine.java:406)
	at jdk.nashorn.api.scripting.NashornScriptEngine.evalImpl(NashornScriptEngine.java:402)
	at jdk.nashorn.api.scripting.NashornScriptEngine.eval(NashornScriptEngine.java:150)
	at javax.script.AbstractScriptEngine.eval(AbstractScriptEngine.java:249)
	at scripting.AbstractScriptManager.getInvocable(AbstractScriptManager.java:74)
	at scripting.event.EventScriptManager.<init>(EventScriptManager.java:54)
	at net.server.channel.Channel.<init>(Channel.java:144)
	at net.server.Server.initWorld(Server.java:405)
	at net.server.Server.init(Server.java:870)
	at net.server.Server.main(Server.java:911)
Caused by: <eval>:26 ReferenceError: "importPackage" is not defined
	at jdk.nashorn.internal.runtime.ECMAErrors.error(ECMAErrors.java:57)
	at jdk.nashorn.internal.runtime.ECMAErrors.referenceError(ECMAErrors.java:319)
	at jdk.nashorn.internal.runtime.ECMAErrors.referenceError(ECMAErrors.java:291)
	at jdk.nashorn.internal.objects.Global.__noSuchProperty__(Global.java:1441)
	at jdk.nashorn.internal.scripts.Script$35$\^eval\_.:program(<eval>:26)
	at jdk.nashorn.internal.runtime.ScriptFunctionData.invoke(ScriptFunctionData.java:637)
	at jdk.nashorn.internal.runtime.ScriptFunction.invoke(ScriptFunction.java:494)
	at jdk.nashorn.internal.runtime.ScriptRuntime.apply(ScriptRuntime.java:393)
	at jdk.nashorn.api.scripting.NashornScriptEngine.evalImpl(NashornScriptEngine.java:449)
	... 10 more

---------------------------------
