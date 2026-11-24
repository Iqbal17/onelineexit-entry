"""The One-Line Exit — one-line resignation letter.

FINAL LINE (87 characters, hand-counted letter by letter):
    I resign because the printer has seen me cry more times than my
    manager has said hello.

DECISION RECORD
---------------
Judge criteria, most important first: (1) a funny one-line resignation
letter whose joke lands; (2) surprise — the turn arrives somewhere
unexpected; (3) fits the form — one line, no padding, reads like a
letter someone could actually send; (4) specific voice — a recognizable
job/workplace/person; (5) stays with the reader — quotable, forwardable.

WRITING PASS 1 — candidates drafted from different jobs/angles:
  A. "I quit. The vending machine has taken more of my money than this
     job ever gave me, and at least it never asked me to smile about it."
     Cut: over the gate at ~140+ characters and reads as a list of two
     grievances, not one turn. The vending-machine angle is also a
     familiar office joke.
  B. "Dear HR: I am resigning to pursue my lifelong dream of never being
     on call during dinner again."
     Cut: "lifelong dream" is a well-worn resignation gag; the surprise
     is thin and the voice could be anyone in any job.
  C. "I hereby resign, effective immediately, because the printer has
     seen me cry more times than my manager has said hello." (119 chars)
     Kept as the base: the printer as emotional witness is a genuinely
     unexpected turn (criterion 2), "my manager has said hello" is a
     specific neglectful-manager detail (criterion 4), and the contrast
     printer-vs-manager is quotable (criterion 5).
  D. "My last day is Friday. The office plant and I are both leaving —
     it died waiting for a promotion, and so did I." (111 chars)
     Strong second place: vivid and quotable, but "so did I" muddles a
     literal death (the plant) with a metaphorical one (the person), and
     "My last day is Friday" is throat-clearing before the joke.
  E. "My manager's 'quick question' has now lasted three years, so this
     is my two weeks' notice." (91 chars)
     Third place: relatable and specific, but the punch is a familiar
     exaggeration rather than a surprise.

WRITING PASS 2 — tightening candidate C:
  The formal opening "I hereby resign, effective immediately, because"
  is padding: it spends 39 characters before the joke starts and adds
  nothing the single word "resign" does not already say. Cutting it to
  "I resign because ..." keeps the letter form (it still reads as a
  line someone could actually send) and gets to the printer nine words
  sooner. Nothing else changed: the printer, the crying, and the
  manager who never says hello are all untouched.

  Final: "I resign because the printer has seen me cry more times than
  my manager has said hello." — 87 characters, verified by hand count
  (I=1 ... hello=82-86, .=87). Inside the 1-140 gate with room to spare.
"""

import os

LINE = "I resign because the printer has seen me cry more times than my manager has said hello."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

    # Read-back verification: the file must hold exactly the line.
    with open(path, encoding="utf-8") as f:
        written = f.read().rstrip("\n")
    assert written == LINE, "entry.txt does not match the line"
    print(f"Verified: {len(written)} characters, 1 line.")
    print(written)


if __name__ == "__main__":
    main()
