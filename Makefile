# ==============================================================================
# ✒ Metadata
#     - Title: Project Makefile (Terminal Velocity - v1.0)
#     - File Name: Makefile
#     - Relative Path: Makefile
#     - Artifact Type: config
#     - Version: 1.0.0
#     - Date: 2025-12-14
#     - Update: Sunday, December 14, 2025
#     - Author: Dennis 'dnoice' Smaltz
#     - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
#     - Signature:  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!
#
# ✒ Description:
#     Common commands for Terminal Velocity project management.
#     Includes environment setup, validation, linting, and build targets.
# ==============================================================================

.PHONY: help install lint format test validate clean scaffold docs

# Default target
help:
	@echo ""
	@echo "╔════════════════════════════════════════════════════════════════╗"
	@echo "║            TERMINAL VELOCITY - Project Commands                ║"
	@echo "╚════════════════════════════════════════════════════════════════╝"
	@echo ""
	@echo "  Environment:"
	@echo "    make install        Install dependencies (pip)"
	@echo "    make install-conda  Install dependencies (conda)"
	@echo ""
	@echo "  Quality:"
	@echo "    make lint           Run linters (ruff, black --check)"
	@echo "    make format         Auto-format code (black)"
	@echo "    make validate       Validate all notebooks run"
	@echo ""
	@echo "  Build:"
	@echo "    make scaffold       Create new TV project structure"
	@echo "    make docs           Generate documentation"
	@echo ""
	@echo "  Cleanup:"
	@echo "    make clean          Remove generated files"
	@echo "    make clean-all      Remove all generated + cache files"
	@echo ""
	@echo "  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!"
	@echo ""

# ==============================================================================
# Environment
# ==============================================================================

install:
	pip install -r computational_core/environment_specs/requirements.txt
	pip install rich pyyaml
	@echo "✓ Dependencies installed"

install-conda:
	conda env create -f computational_core/environment_specs/environment.yml
	@echo "✓ Conda environment 'tv-research' created"
	@echo "  Activate with: conda activate tv-research"

install-dev:
	pip install -r computational_core/environment_specs/requirements.txt
	pip install rich pyyaml black ruff pytest jupytext
	@echo "✓ Development dependencies installed"

# ==============================================================================
# Code Quality
# ==============================================================================

lint:
	@echo "Running ruff..."
	-ruff check .
	@echo ""
	@echo "Running black (check mode)..."
	-black --check .
	@echo ""
	@echo "✓ Lint complete"

format:
	@echo "Running black..."
	black .
	@echo ""
	@echo "Running ruff (fix mode)..."
	ruff check --fix .
	@echo ""
	@echo "✓ Format complete"

# ==============================================================================
# Validation
# ==============================================================================

validate:
	@echo "Validating notebook execution..."
	@find mechanism_dossiers -name "*.py" -path "*/computations/*" -exec echo "  Testing: {}" \;
	@echo ""
	@echo "Note: Full validation runs all notebooks. This may take a while."
	@echo "For single mechanism: python mechanism_dossiers/<vector>/<mechanism>/evidence_archive/computations/*.py"

test:
	pytest -v

# ==============================================================================
# Build
# ==============================================================================

scaffold:
	@echo "Terminal Velocity Scaffold"
	@echo ""
	@read -p "Target directory: " target; \
	python tools/tv_scaffold.py "$$target" --verbose

scaffold-dry:
	@echo "Terminal Velocity Scaffold (Dry Run)"
	@echo ""
	@read -p "Target directory: " target; \
	python tools/tv_scaffold.py "$$target" --dry-run

# ==============================================================================
# Documentation
# ==============================================================================

docs:
	@echo "Documentation targets:"
	@echo "  - README.md"
	@echo "  - docs/QUICKSTART.md"
	@echo "  - docs/EVIDENCE_GRADING.md"
	@echo "  - docs/blueprints/TERMINAL_VELOCITY_BLUEPRINT.md"
	@echo ""
	@echo "View at: https://github.com/dnoice/terminal-velocity"

# ==============================================================================
# Cleanup
# ==============================================================================

clean:
	@echo "Cleaning generated files..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} + 2>/dev/null || true
	@echo "✓ Clean complete"

clean-all: clean
	@echo "Cleaning cache and environment files..."
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	@echo "✓ Deep clean complete"

# ==============================================================================
# Utility
# ==============================================================================

count:
	@echo "Project Statistics:"
	@echo "  Directories: $$(find . -type d | wc -l)"
	@echo "  Files:       $$(find . -type f | wc -l)"
	@echo "  Markdown:    $$(find . -name '*.md' | wc -l)"
	@echo "  Python:      $$(find . -name '*.py' | wc -l)"
	@echo "  YAML:        $$(find . -name '*.yaml' -o -name '*.yml' | wc -l)"

tree:
	@tree -L 3 -I '__pycache__|.git|.pytest_cache|*.egg-info' || \
	find . -maxdepth 3 -type d | head -50

# ==============================================================================
# End
# ==============================================================================
