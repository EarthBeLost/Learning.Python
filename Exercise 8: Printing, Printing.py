formatter = "%r %r %r %r" # Forgot to wrap the variable in quotes...

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % ("I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight!"
	)

# === STUDY DRILLS ===
# 1. Do your checks, write down your mistakes, and try not to make the same mistakes on the next exercise.
# 2. Notice that the last line of output uses both single-quotes and double-quotes for individual pieces. Why do you think that is?
