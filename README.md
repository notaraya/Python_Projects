# 50 Python Projects

A structured roadmap of 50 projects for learning Python, organised into five
tiers so skills build up progressively — from fundamentals to full-stack and
systems work.

Each project is its own folder with a small self-contained setup:
`project-01/`, `project-02/`, and so on.

## Ground rules

1. Say which project number you're starting; you'll get a nudge on where to
   begin — not the solution.
2. When stuck, describe what you tried and what broke; you'll be pointed toward
   the concept, not handed the fix.
3. After each project, paste the code for a review of bugs, style, and better
   approaches.

---

## Tier 1 — Fundamentals (1–10)

Small, single-file scripts. Focus on syntax, control flow, functions, and
data structures.

1. Number guessing game
2. Simple calculator (CLI)
3. Temperature converter
4. Mad Libs generator
5. Rock-Paper-Scissors
6. Basic to-do list (in-memory)
7. Dice roll simulator
8. Password strength checker
9. Unit converter (length/weight)
10. Simple quiz app

## Tier 2 — Core Skills (11–20)

Files, loops, and functions working together.

11. To-do list with file persistence (txt/json)
12. Contact book (CRUD, file-based)
13. Word counter for a text file
14. Simple encryption (Caesar cipher)
15. Hangman game
16. Tic-Tac-Toe (2-player CLI)
17. Expense tracker
18. Countdown timer
19. Basic text-based adventure game
20. CSV data cleaner/parser

## Tier 3 — OOP & Intermediate Logic (21–30)

Structuring data and systems: classes, modules, and modelling entities.

21. Library management system
22. Bank account simulator (OOP)
23. Inventory management system
24. Simple chess piece movement validator
25. Recipe manager with search
26. Student grade tracker with statistics
27. Deck of cards / card game engine
28. Basic ATM simulator
29. Employee management system
30. Simple state machine (traffic light simulation)

## Tier 4 — APIs, Web, Data (31–40)

Talking to the outside world: HTTP, serialisation, and persistence.

31. Weather app (using a public API)
32. Currency converter (live rates API)
33. Web scraper (headlines from a news site)
34. URL shortener (web framework)
35. Simple REST API
36. Personal blog backend (CRUD API)
37. Twitter/X-style CLI bot (API)
38. Data visualisation dashboard
39. CSV → SQLite database importer
40. Simple chat app (sockets)

## Tier 5 — Advanced (41–50)

Concurrency, performance, and putting it all together.

41. Multi-threaded file downloader
42. Basic web crawler with depth limit
43. Markdown to HTML converter
44. Command-line task scheduler (cron-like)
45. Simple machine learning model (e.g. spam classifier)
46. Chatbot using a language model API
47. Basic compiler/interpreter for a toy language
48. REST API with authentication (JWT)
49. Real-time dashboard (WebSockets)
50. Full-stack project: your own idea, using everything above

---

## Requirements

Python 3.11+ and a virtual environment tool (`venv` is built in; `uv` is
faster if you have it).

```bash
python3 --version
```

## Usage

Tier 1–3 are plain scripts:

```bash
cd project-01
python3 main.py
```

From Tier 4 on, each project is a package with its own venv:

```bash
cd project-31
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

Useful commands:

```bash
python3 -m venv .venv   # create environment
pip install -r requirements.txt
python3 -m pip list     # what's installed
python3 -m compileall . # syntax check
python3 -m pytest       # tests (from Tier 3 on)
ruff check .            # lints
ruff format .           # format
```

## Starting a project

```bash
mkdir project-01 && cd project-01
python3 -m venv .venv && source .venv/bin/activate
```

Keep each program small and focused, and add a short explaining the concept the project was meant
to teach and anything that tripped you up.

## Dependencies

Tier 1–3 need only the standard library — try solving them with `builtins`
before reaching for packages. From Tier 4 onward you'll pull in packages like
`requests`, `httpx`, `pandas`, `flask`/`fastapi`, `sqlalchemy`, and `asyncio`;
look each one up on [PyPI](https://pypi.org) or [Real Python](https://realpython.com)
when you meet it.
