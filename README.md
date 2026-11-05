# CSA08 Assignment 1 - worked solution

Name: PROBIR SAHA SHOHOM
Register number: 1911260319
GitHub repository: https://github.com/Probir127/CSA08-1911260319-Assignment1

This package contains worked solutions for all 12 tasks. Read SOLUTIONS.md first.
It is a study/reference solution: understand, adapt and execute it yourself.

Course: CSA08 - Python Programming

[Download the PDF report](CSA08_Complete_Solution.pdf)

Requires Python 3.10 or later; only standard-library modules are used.
The exact verification Python version and measurements are in Task10/output.txt.

From this folder, run:

```text
python3 Task01/demo.py
python3 Task02/interactive.py
python3 Task02/complete_code.py
python3 Task03/demo.py
python3 Task04/demo.py
python3 Task05/demo.py
python3 Task06/demo.py
python3 Task07/milkrate.py
python3 Task07/use_module.py
python3 Task08/demo.py
python3 Task09/tests.py
python3 Task09/cli.py < Task09/input.txt
python3 Task10/benchmark.py
python3 Task11/demo.py
python3 Task12/tests.py
```

Each task's output.txt contains output captured from an actual execution.
Task09 also includes sample input and separate CLI output.
The report explains the result of each task, assumptions and complexity.
Output images in each task folder are rendered directly from actual captured stdout and are labelled as rendered transcripts. They are not terminal screenshots. If the faculty specifically requires terminal screenshots, the student should run the listed commands and capture those screenshots.

## Re-run all tasks

Run `python3 tools/run_all.py` to execute every program, re-run the assertions and both CLI scenarios, and refresh the output files and `verification.json`.

## Submission status

The source, report, sample inputs, captured output and labelled output images are included. The student must review and understand the solution, confirm the stated business-rule assumptions, and submit the repository URL to the faculty. Faculty sharing or collaborator invitation requires the faculty's GitHub identity and has not been performed.

## Results by task

| Task | Result |
|---|---|
| 1 | Structured collection record and data analysis |
| 2 | Decimal total 33400.30; float representation issue reproduced |
| 3 | Naming, dynamic typing and swapping demonstrated |
| 4 | Step-count, precedence and truncation differences reproduced |
| 5 | Invalid input rejected and aligned output demonstrated |
| 6 | Exact rates and delivery payouts calculated |
| 7 | Completed module produces expected table; import has no table side effect |
| 8 | Three-entry hand trace totals 917.50 |
| 9 | Expected payouts and rejections pass; five-entry total 1213.50 |
| 10 | Totals and timings measured for 300, 6000 and 150000 payments |
| 11 | JSON rate configuration loaded and validated |
| 12 | Seasonal, fractional-reading, bonus and period-boundary assertions pass |
