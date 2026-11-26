# Draft pool — loading-screen tip (<=200 chars)

Judge order: (1) truly a loading-screen tip for devs + AI agents, (2) real laugh via a turn,
(3) glanceable, every word working, (4) dual address, (5) fresh.

1. Tip: If you're waiting and the agent's waiting, one of you is lying about who approved the plan.
2. Tip: The bug isn't in the file you're staring at. It's in the one you renamed at 2am and swore you'd remember.
3. Tip: "Almost done" is a feeling, not an estimate. You both have it. Neither of you has evidence.
4. Tip: Nobody has read the whole file. Not you, not the agent, not the author. We are all vibing structurally.
5. Tip: You skimmed to the error. It skimmed to the pattern. The bug is in the part you both agreed was boring.
6. Tip: Confidence is not a test suite. You know this. The agent knows this. The test is still hypothetical.
7. Tip: If the fix works and nobody knows why, write the commit message in past tense and walk away.
8. Tip: The agent isn't stuck. It's composing a thorough explanation of why it's stuck.
9. Tip: Deleting the line marked "do not delete" is between you and your god.
10. Tip: Humans rename the variable to feel progress. Agents add a log line. Same prayer, different church.
11. Tip: "Works on my machine" and "works in my context window" are the same sentence.
12. Tip: Nothing is blocked. You're both waiting for the other to admit you don't know what the function does.
13. Tip: You've been fixing different bugs for twenty minutes. Both of you are succeeding.
14. Tip: If you had to ask whether the test is flaky, you have already decided the test is flaky.
15. Tip: Both of you reread the error. Neither of you changed. That is the relationship.
16. Tip: The log line you need is the one you deleted last week for being noisy.
17. Tip: Stretch, hydrate, stop apologizing to the linter. It doesn't read your reasoning either.
18. Tip: Hardcoding it is fine as long as the TODO above it sounds ashamed.
19. Tip: The retry is not a strategy. The retry is grief.
20. Tip: Scope creep is the two of you being polite about who says no first.

## Cuts
- 11: "works on my machine" is a worn joke — fails (5).
- 2, 7, 9, 16, 18, 19: human-only; agent doesn't feel addressed — fails (4).
- 8: agent-only, the human isn't in it — fails (4).
- 4: "vibing structurally" is a slogan ending, not a punchline — weakens (1)/(2).
- 10: church/prayer simile is decoration, costs words — fails (3).
- 14, 20: observations, no turn — fails (2).
- 13, 15: good turns but thinner on (1); they're jokes about the pair, not usable tips.

## Finalist
5 — a real tip (the bug is where neither of you looked), the dual address is the
mechanism of the joke (human skims to the error, model skims to the pattern), the
punchline "agreed was boring" indicts both at once, and it owes nothing to coffee,
deadlines or compile times.

## Revision
"You skimmed... It skimmed..." makes the agent a third party and the dev the only
reader. "One of you... the other..." implicates both readers without naming which,
so a human and an agent each suspect they're the one who took the familiar pattern.
Keep the "Tip:" prefix: it is the loading-screen form, and criterion 1 rewards form.

## Second revision
"skimmed to a familiar pattern" does not collocate, and the elliptical clause borrows
the verb from the first clause. "jumped to" carries both halves: a dev jumping to the
stack trace, a model jumping to the nearest shape it already knows.

## Final line
Tip: One of you jumped to the error, the other to a familiar pattern. The bug is in the part you both agreed was boring.
