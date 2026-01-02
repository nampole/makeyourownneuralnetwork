# Copilot / AI Agent Instructions

Purpose: help AI coding agents quickly understand and safely edit this small MNIST neural-network project (notebooks + a few scripts and datasets).

Big picture
- Single-project educational codebase implementing a simple feed-forward neural network for MNIST and user images.
- Primary code lives in `neuralNetwork.ipynb` (defines `neuralNetwork` class, usage examples) and `neural_network_for_mnist.py` (script variant). Data lives in `mnist_dataset/` and `my_own_images/`.

Key files to read first
- `neuralNetwork.ipynb` — core `neuralNetwork` class, weight init, `train()` and `query()` examples (includes many print-debug statements and Korean comments).
- `neural_network_for_mnist.py` — standalone script usage patterns (if present).
- `mnist_dataset/` — CSV and example datasets (`mnist_train_100.csv`, `mnist_test_10.csv`). Some notebooks expect a gzip `mnist_train.gz` file.
- `my_own_images/` — example images and readme for running custom inference.
- `README.md` and `test.py` — lightweight project docs and quick-run helpers.

Concrete architecture notes (what to preserve)
- The `neuralNetwork` class initializes weights with gaussian noise using: `numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))` and uses `scipy.special.expit` as the sigmoid activation. Preserve these numeric shapes and the API: `__init__(inputnodes, hiddennodes, outputnodes, learningrate)`.
- Data scaling is performed in notebooks with: `scaled_input = (pixels / 255.0 * 0.99) + 0.01`. Keep that exact mapping when adapting data pre-processing to scripts/tests.
- Notebooks use Jupyter-specific magics (e.g. `%matplotlib inline`) and gzip-based dataset reads. Avoid removing those without replacing with an equivalent in scripts.

Developer workflows & commands
- Notebook development: open `neuralNetwork.ipynb` in JupyterLab / VS Code Notebook and run cells interactively.
- Run script examples: `python3 neural_network_for_mnist.py` or `python3 test.py` (no test-suite present). If you add dependencies, update or add `requirements.txt`.

Project conventions & editing guidance for AI agents
- Minimal, focused edits: change a single notebook or small script per PR. Do not reformat whole notebooks or strip print/debug lines unless requested.
- Preserve Korean comments and existing print output semantics; if converting prints to logging, do it in a separate, clearly scoped change and add a `requirements.txt` entry for `logging` usage (std lib is fine).
- When changing numeric behavior (weight init, activation, scaling), point to the exact lines in `neuralNetwork.ipynb` and include a short unit-run example (use the existing `myNeural = neuralNetwork(...)` snippet as a smoke test).

Integration points and external deps
- Requires: `numpy`, `scipy`, `matplotlib`, and `jupyter`/notebook environment for notebooks. Some cells use `gzip` to read compressed training files.
- Data I/O: code expects CSV-style MNIST rows and, in places, a `mnist_train.gz` file. When adding file I/O changes, keep relative paths (project root → `mnist_dataset/`) and update README.

What an agent should do first when asked to change behavior
1. Open `neuralNetwork.ipynb` and locate the `neuralNetwork` class cells (look for `class neuralNetwork:`). Verify shapes for `wih` and `who` before changing layer sizes.
2. Run the minimal smoke example at the bottom of the notebook (`myNeural = neuralNetwork(3,3,3,0.3)` → `train()` → `query()`) to ensure no regressions.
3. If adding scripts or tests, provide a short runnable example and add/modify `requirements.txt`.

Avoid assumptions
- There is no test harness or CI in the repo. Do not assume existing test coverage. Any request to add tests should include a runnable example and instructions to run them.

When to ask the human
- If a change touches dataset format, global scaling, or reduces/increases network sizes — ask which dataset (CSV vs gz) and whether notebooks or scripts should be authoritative.
- If adding dependencies or converting notebooks to scripts — ask whether to add `requirements.txt` and update `README.md`.

Contact / feedback
- After making changes, include a short smoke-run description and exact commands used. Ask for confirmation before broader refactors.

End of instructions.
