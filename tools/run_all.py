"""Run every assignment program and save genuine stdout and verification status."""
from pathlib import Path
import subprocess
import sys
import json

ROOT = Path(__file__).resolve().parents[1]
JOBS = {
    'Task01': ['demo.py'],
    'Task02': ['interactive.py', 'complete_code.py'],
    'Task03': ['demo.py'],
    'Task04': ['demo.py'],
    'Task05': ['demo.py'],
    'Task06': ['demo.py'],
    'Task07': ['milkrate.py', 'use_module.py'],
    'Task08': ['demo.py'],
    'Task09': ['tests.py'],
    'Task10': ['benchmark.py'],
    'Task11': ['demo.py'],
    'Task12': ['tests.py'],
}

def main():
    """Fail on any program error, then save all successful execution output."""
    results = []
    for task, programs in JOBS.items():
        chunks = []
        for program in programs:
            relative = f'{task}/{program}'
            run = subprocess.run([sys.executable, relative], cwd=ROOT,
                                 capture_output=True, text=True, check=True)
            chunks.append(f'$ python3 {relative}\n{run.stdout}')
            if run.stderr:
                chunks.append('STDERR:\n' + run.stderr)
            results.append({'program': relative, 'exit_code': run.returncode})
        (ROOT / task / 'output.txt').write_text('\n'.join(chunks), encoding='utf-8')
        print(task, 'PASS')
    for input_name, output_name in [('input.txt', 'cli_output.txt'),
                                     ('invalid_input.txt', 'invalid_output.txt')]:
        run = subprocess.run([sys.executable, 'Task09/cli.py'], cwd=ROOT,
                             input=(ROOT/'Task09'/input_name).read_text(),
                             text=True, capture_output=True, check=True)
        if input_name == 'invalid_input.txt':
            assert run.stdout.count('Rejected:') == 2
            assert 'Rs 300.00' in run.stdout
        else:
            assert 'Rs 583.90' in run.stdout
        (ROOT/'Task09'/output_name).write_text(run.stdout)
        results.append({'program': f'Task09/cli.py < Task09/{input_name}',
                        'exit_code': run.returncode})
    (ROOT/'verification.json').write_text(json.dumps(
        {'python': sys.version, 'results': results}, indent=2)+'\n')
    print('All programs and both CLI scenarios passed.')

if __name__ == '__main__':
    main()
