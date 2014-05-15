Success = {
	"success": 1
}

Advantage = {
	"advantage": 1
}

Triumph = {
	"success": 1,
	"triumph": 1
}

Failure = {
	"success": -1
}

Threat = {
	"advantage": -1
}

Despair = {
	"success": -1,
	"despair": 1
}

Dark = {
	"dark": 1
}

Light = {
	"light": 1
}

Blank = {
}

dieOptions = {
	"b": ((Blank,), (Blank,), (Success,), (Advantage,), (Advantage, Advantage,), (Advantage, Success,)),
	"a": ((Blank,), (Advantage, Advantage,), (Success,), (Advantage,), (Success, Success,), (Advantage, Success,), (Advantage,), (Success,)),
	"p": ((Blank,), (Success,), (Success,), (Success, Success,), (Success, Success,), (Advantage,), (Advantage, Success,), (Advantage, Success,), (Advantage, Success,), (Advantage, Advantage,), (Advantage, Advantage,), (Triumph,)),
	"s": ((Blank,), (Blank,), (Failure,), (Failure,), (Threat,), (Threat,)),
	"d": ((Blank,), (Threat,), (Threat, Threat,), (Threat,), (Threat,), (Threat,), (Threat, Threat,), (Failure, Threat,)),
	"c": ((Blank,), (Failure,), (Failure,), (Failure, Failure,), (Failure, Failure,), (Threat,), (Threat,), (Failure, Threat,), (Failure, Threat,), (Threat, Threat,), (Threat, Threat,), (Despair,)),
	"f": ((Dark,), (Dark,), (Dark,), (Dark,), (Dark,), (Dark,), (Dark, Dark,), (Light,), (Light,), (Light, Light,), (Light, Light,), (Light, Light,))
}