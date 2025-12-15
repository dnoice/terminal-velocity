<!--
✒ Metadata
    - Title: Docstring Standards Guide (digiSpace Edition - v1.0)
    - File Name: DOCSTRING_STANDARDS.md
    - Relative Path: docs/standards/DOCSTRING_STANDARDS.md
    - Artifact Type: docs
    - Version: 1.0.0
    - Date: 2025-11-24
    - Update: Monday, November 24, 2025
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature:  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!

✒ Description:
    The definitive docstring standards guide for ALL artifacts across ALL projects—
    past, present, and future. This is not project-specific. This is not optional.
    Every file that leaves your keyboard carries this header. No exceptions. No ambiguity.

✒ Key Features:
    - Feature 1: Universal standard for ALL projects—past, present, and future
    - Feature 2: Language-specific comment syntax adaptations with examples
    - Feature 3: Section-by-section breakdown with usage guidance
    - Feature 4: Complete examples for 12+ common file formats
    - Feature 5: Copy-paste ready templates for rapid artifact creation
    - Feature 6: Conditional section guidelines (when to include/omit)
    - Feature 7: Metadata field specifications with valid values
    - Feature 8: Best practices for description writing
    - Feature 9: Version numbering conventions (SemVer)
    - Feature 10: Integration guidance for IDEs and linters

✒ Usage Instructions:
    This document serves as the authoritative reference for artifact documentation.

    How to use:
        1. Identify your file type from the examples below
        2. Copy the appropriate template
        3. Fill in ALL metadata fields (no placeholders in production)
        4. Include/omit conditional sections based on artifact type
        5. Write descriptions in plain English—no fluff, no filler

✒ Examples:
    - Example 1: Python CLI script with full argument documentation
    - Example 2: JavaScript ES6 module with export descriptions
    - Example 3: HTML page with semantic structure notes
    - Example 4: CSS stylesheet with design system references
    - Example 5: Bash script with environment requirements
    - Example 6: YAML config with schema validation notes
    - Example 7: TOML configuration with section breakdowns
    - Example 8: SQL migration with rollback procedures
    - Example 9: Markdown documentation (meta example)
    - Example 10: TypeScript with type definitions

✒ Other Important Information:
    - Dependencies: None (documentation only)
    - Compatible platforms: Universal (all text editors, IDEs)
    - File format handling: Applies to all text-based file formats
    - Scope: ALL artifacts, ALL projects, ALL time (past, present, future)
    - Performance notes: N/A
    - Security considerations: Do not include secrets in headers
    - Known limitations: Binary files cannot use this standard

    This document is the CONTRACT. Memorize it. Live it. Never ship without it.
---------
-->

# 📜 Docstring Standards Guide

## Universal Artifact Header Standard

> **Philosophy:** *"Aim Twice, Shoot Once"* — Every artifact ships with complete,
> professional documentation. No exceptions. No excuses. ALL projects. ALL files.

---

## Table of Contents

- [📜 Docstring Standards Guide](#-docstring-standards-guide)
  - [Universal Artifact Header Standard](#universal-artifact-header-standard)
  - [Table of Contents](#table-of-contents)
  - [1. Core Template Structure](#1-core-template-structure)
  - [2. Metadata Field Specifications](#2-metadata-field-specifications)
    - [Version Numbering Convention (SemVer)](#version-numbering-convention-semver)
  - [3. Section Guidelines](#3-section-guidelines)
    - [Always Include](#always-include)
    - [Include When Applicable](#include-when-applicable)
    - [Omit When Not Applicable](#omit-when-not-applicable)
  - [4. Language-Specific Examples](#4-language-specific-examples)
    - [4.1 Python (.py)](#41-python-py)
    - [4.2 JavaScript (.js)](#42-javascript-js)
    - [4.3 TypeScript (.ts)](#43-typescript-ts)
    - [4.4 HTML (.html)](#44-html-html)
    - [4.5 CSS (.css)](#45-css-css)
    - [4.6 Bash/Shell (.sh)](#46-bashshell-sh)
    - [4.7 YAML (.yaml/.yml)](#47-yaml-yamlyml)
    - [4.8 TOML (.toml)](#48-toml-toml)
    - [4.9 JSON (JSONC)](#49-json-jsonc)
    - [4.10 SQL (.sql)](#410-sql-sql)
    - [4.11 Markdown (.md)](#411-markdown-md)
    - [4.12 INI/Config (.ini/.cfg)](#412-iniconfig-inicfg)
  - [5. Conditional Sections Reference](#5-conditional-sections-reference)
  - [6. Quick Reference Card](#6-quick-reference-card)
    - [Comment Syntax by Language](#comment-syntax-by-language)
    - [Signature Line (Copy-Paste Ready)](#signature-line-copy-paste-ready)
  - [Final Word](#final-word)

---

## 1. Core Template Structure

Every artifact header follows this exact structure. Adapt the comment syntax;
never alter the section order or naming.

```text
[COMMENT_START]
✒ Metadata
    - Title: {Tool Name} ({Project-Name} Edition - v{X.Y})
    - File Name: {file_name}.{ext}
    - Relative Path: {relative/path/to/project/root}
    - Artifact Type: {script | library | CLI | config | docs | notebook | test | other}
    - Version: {X.Y.Z}
    - Date: {YYYY-MM-DD}
    - Update: {Day, Month DD, YYYY}
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: {AI-Platform} - {AI-Model (long form)}
    - Signature:  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!

✒ Description:
    {2-3 sentences. What it does. When to use it. What problem it solves.}

✒ Key Features:
    - Feature 1: {Description}
    - Feature 2: {Description}
    {... continue as needed, aim for 8-12 for substantial artifacts}

✒ Usage Instructions:
    {Context-specific usage guidance with examples}

✒ Examples:
    {5-10 realistic examples covering major use cases}

✒ Command-Line Arguments: (if applicable)
    {Grouped by category: Input, Processing, Output}

✒ Other Important Information:
    - Dependencies: {list}
    - Compatible platforms: {list}

✒ {Additional Relevant Sections}:
    {Add any other sections that make sense for the specific artifact type}
---------
[COMMENT_END]
```

---

## 2. Metadata Field Specifications

| Field | Format | Example | Required |
|-------|--------|---------|----------|
| **Title** | `{Tool Name} ({Project-Name} Edition - v{X.Y})` | `TextProcessor (PySnip Edition - v2.1)` | ✅ Yes |
| **File Name** | `{file_name}.{ext}` | `text_processor.py` | ✅ Yes |
| **Relative Path** | Unix-style path from project root | `src/tools/text_processor.py` | ✅ Yes |
| **Artifact Type** | One of: `script`, `library`, `CLI`, `config`, `docs`, `notebook`, `test`, `other` | `CLI` | ✅ Yes |
| **Version** | Semantic Versioning `{X.Y.Z}` | `1.2.3` | ✅ Yes |
| **Date** | ISO 8601 `{YYYY-MM-DD}` | `2025-11-24` | ✅ Yes |
| **Update** | Full written date `{Day, Month DD, YYYY}` | `Monday, November 24, 2025` | ✅ Yes |
| **Author** | Name with handle | `Dennis 'dnoice' Smaltz` | ✅ Yes |
| **A.I. Acknowledgement** | `{AI-Platform} - {AI-Model (long form)}` | `Anthropic - Claude Opus 4.5` | ✅ Yes |
| **Signature** | Exactly as shown | `︻デ═—··· 🎯 = Aim Twice, Shoot Once!` | ✅ Yes |

### Version Numbering Convention (SemVer)

- **MAJOR (X):** Breaking changes, incompatible API modifications
- **MINOR (Y):** New features, backward-compatible additions
- **PATCH (Z):** Bug fixes, minor improvements, documentation updates

---

## 3. Section Guidelines

### Always Include

- ✒ Metadata (complete, no placeholders)
- ✒ Description (2-3 sentences, no exceptions)
- ✒ Key Features (minimum 3, aim for 8-12)
- ✒ Other Important Information (at minimum: Dependencies, Platforms)

### Include When Applicable

- ✒ Usage Instructions — Always for executable code
- ✒ Examples — Always for scripts, CLIs, libraries
- ✒ Command-Line Arguments — Only for CLIs

### Omit When Not Applicable

- Command-Line Arguments for non-CLI artifacts
- Examples section for simple configs (unless complex)

---

## 4. Language-Specific Examples

### 4.1 Python (.py)

Python uses triple-quoted docstrings. Include shebang and encoding for scripts.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
✒ Metadata
    - Title: {Tool Name} ({Project-Name} Edition - v{X.Y})
    - File Name: {file_name}.py
    - Relative Path: {relative/path/to/file}.py
    - Artifact Type: {script | library | CLI | config | docs | notebook | test | other}
    - Version: {X.Y.Z}
    - Date: {YYYY-MM-DD}
    - Update: {Day, Month DD, YYYY}
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: {AI-Platform} - {AI-Model (long form)}
    - Signature:  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!

✒ Description:
    Automatically organizes files in a directory by type, date, or custom rules.
    Use it to declutter downloads folders, sort project assets, or archive old files.
    Supports dry-run mode, undo operations, and configurable rule sets.

✒ Key Features:
    - Feature 1: Sort files by extension into categorized folders
    - Feature 2: Date-based organization (year/month/day hierarchy)
    - Feature 3: Custom rule definitions via YAML config
    - Feature 4: Dry-run mode to preview changes without execution
    - Feature 5: Undo functionality with operation logging
    - Feature 6: Recursive directory processing
    - Feature 7: Duplicate detection and handling
    - Feature 8: Progress bar with rich terminal output
    - Feature 9: Cross-platform path handling
    - Feature 10: Configurable ignore patterns (gitignore syntax)

✒ Usage Instructions:
    Run from command line with source directory as argument.

    Basic usage:
        $ python file_organizer.py /path/to/messy/folder

    With options:
        $ python file_organizer.py ~/Downloads --by-date --dry-run

✒ Examples:
    $ python file_organizer.py ~/Downloads
    $ python file_organizer.py ~/Downloads --by-type
    $ python file_organizer.py ~/Downloads --by-date --format "%Y/%m"
    $ python file_organizer.py ~/Desktop --dry-run --verbose
    $ python file_organizer.py /data --config rules.yaml
    $ python file_organizer.py ~/Photos --recursive --ignore "*.tmp"
    $ python file_organizer.py . --undo
    $ python file_organizer.py /archive --move-to /sorted --by-type

✒ Command-Line Arguments:
    Input Options:
        source_dir               Directory to organize (required)
        --config FILE            Custom rules config file (YAML)

    Organization Options:
        --by-type                Group files by extension (default)
        --by-date                Group files by modification date
        --format FMT             Date format string (default: %Y-%m-%d)
        --recursive, -r          Process subdirectories

    Safety Options:
        --dry-run, -n            Preview changes without executing
        --undo                   Reverse last organization operation
        --backup                 Create backup before organizing

    Output Options:
        --move-to DIR            Target directory (default: in-place)
        --verbose, -v            Detailed operation logging
        --quiet, -q              Suppress all output except errors

✒ Other Important Information:
    - Dependencies:
        Required: pathlib, argparse, shutil (stdlib)
        Optional: rich (terminal UI), pyyaml (config files)
    - Compatible platforms: Linux, Windows, macOS, Termux
    - File format handling: All file types (organization only, no content parsing)
    - Performance notes: Handles 10,000+ files efficiently; memory scales with file count
    - Security considerations: Never follows symlinks outside source directory
    - Known limitations: Cannot undo operations across sessions without log file
---------
"""

import argparse
from pathlib import Path
# ... rest of implementation
```

---

### 4.2 JavaScript (.js)

JavaScript uses block comments `/* */` for the header.

```javascript
/*
 * ============================================================================
 * ✒ Metadata
 *     - Title: {Tool Name} ({Project-Name} Edition - v{X.Y})
 *     - File Name: {file_name}.js
 *     - Relative Path: {relative/path/to/file}.js
 *     - Artifact Type: {script | library | CLI | config | docs | notebook | test | other}
 *     - Version: {X.Y.Z}
 *     - Date: {YYYY-MM-DD}
 *     - Update: {Day, Month DD, YYYY}
 *     - Author: Dennis 'dnoice' Smaltz
 *     - A.I. Acknowledgement: {AI-Platform} - {AI-Model (long form)}
 *     - Signature:  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!
 *
 * ✒ Description:
 *     Lightweight DOM manipulation utilities for vanilla JavaScript projects.
 *     Provides jQuery-like convenience without the bloat or dependencies.
 *     Drop-in replacement for common DOM operations in modern browsers.
 *
 * ✒ Key Features:
 *     - Feature 1: Chainable element selection with CSS selectors
 *     - Feature 2: Event delegation with automatic cleanup
 *     - Feature 3: Smooth animations without external libraries
 *     - Feature 4: AJAX wrapper with Promise support
 *     - Feature 5: Local storage helpers with JSON serialization
 *     - Feature 6: Debounce and throttle utilities
 *     - Feature 7: Responsive breakpoint detection
 *     - Feature 8: Accessibility helpers (focus trapping, ARIA updates)
 *
 * ✒ Usage Instructions:
 *     Import the module in your JavaScript entry point:
 *         import { $, $$, on, ajax } from './dom-utils.js';
 *
 *     Or include via script tag (exposes global `DOMUtils` object):
 *         <script src="dom-utils.js"></script>
 *
 * ✒ Examples:
 *     // Select single element
 *     const header = $('#main-header');
 *
 *     // Select multiple elements
 *     const buttons = $$('.btn-primary');
 *
 *     // Event delegation
 *     on(document, 'click', '.menu-item', (e) => handleClick(e));
 *
 *     // AJAX request
 *     const data = await ajax.get('/api/users');
 *
 *     // Animate element
 *     animate(element, { opacity: 0, y: -20 }, 300);
 *
 *     // Debounced handler
 *     const debouncedSearch = debounce(search, 250);
 *
 * ✒ Other Important Information:
 *     - Dependencies: None (vanilla JavaScript)
 *     - Compatible platforms: All modern browsers (ES6+), Node.js (partial)
 *     - Performance notes: Minified size ~4KB gzipped
 *     - Security considerations: Sanitizes innerHTML by default
 *     - Known limitations: No IE11 support
 * ----------------------------------------------------------------------------
 */

// Module implementation
export const $ = (selector, context = document) => context.querySelector(selector);
export const $$ = (selector, context = document) => [...context.querySelectorAll(selector)];
// ... rest of implementation
```

---

### 4.3 TypeScript (.ts)

TypeScript follows JavaScript conventions with type annotation notes.

```typescript
/*
 * ============================================================================
 * ✒ Metadata
 *     - Title: {Tool Name} ({Project-Name} Edition - v{X.Y})
 *     - File Name: {file_name}.ts
 *     - Relative Path: {relative/path/to/file}.ts
 *     - Artifact Type: {script | library | CLI | config | docs | notebook | test | other}
 *     - Version: {X.Y.Z}
 *     - Date: {YYYY-MM-DD}
 *     - Update: {Day, Month DD, YYYY}
 *     - Author: Dennis 'dnoice' Smaltz
 *     - A.I. Acknowledgement: {AI-Platform} - {AI-Model (long form)}
 *     - Signature:  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!
 *
 * ✒ Description:
 *     Type-safe HTTP client wrapper for REST API communication.
 *     Handles authentication, request/response interceptors, and error normalization.
 *     Built on fetch API with full TypeScript generics support.
 *
 * ✒ Key Features:
 *     - Feature 1: Full TypeScript generics for request/response typing
 *     - Feature 2: Automatic JWT token refresh and injection
 *     - Feature 3: Request/response interceptor pipeline
 *     - Feature 4: Configurable retry logic with exponential backoff
 *     - Feature 5: Request cancellation via AbortController
 *     - Feature 6: Response caching with TTL support
 *     - Feature 7: Error normalization to consistent format
 *     - Feature 8: Request deduplication for identical concurrent calls
 *     - Feature 9: Offline queue with sync on reconnect
 *     - Feature 10: OpenAPI schema validation (dev mode)
 *
 * ✒ Usage Instructions:
 *     Import and instantiate with base configuration:
 *         import { ApiClient } from './api-client';
 *         const api = new ApiClient({ baseUrl: 'https://api.example.com' });
 *
 *     Use typed methods for CRUD operations:
 *         const user = await api.get<User>('/users/123');
 *
 * ✒ Examples:
 *     // Basic GET with type inference
 *     const users = await api.get<User[]>('/users');
 *
 *     // POST with body
 *     const newUser = await api.post<User>('/users', { name: 'John' });
 *
 *     // With query parameters
 *     const results = await api.get<SearchResult>('/search', { params: { q: 'test' } });
 *
 *     // File upload
 *     await api.upload('/files', formData, { onProgress: (p) => console.log(p) });
 *
 *     // Cancellable request
 *     const controller = new AbortController();
 *     api.get('/slow-endpoint', { signal: controller.signal });
 *     controller.abort();
 *
 * ✒ Other Important Information:
 *     - Dependencies: None (uses native fetch)
 *     - Compatible platforms: Browser (ES2020+), Node.js 18+, Deno
 *     - Type definitions: Included (no @types package needed)
 *     - Performance notes: Connection pooling in Node.js via undici
 *     - Security considerations: Credentials never logged; token storage configurable
 *     - Known limitations: Streaming responses require manual handling
 * ----------------------------------------------------------------------------
 */

interface ApiClientConfig {
    baseUrl: string;
    timeout?: number;
    headers?: Record<string, string>;
}

export class ApiClient {
    // ... implementation
}
```

---

### 4.4 HTML (.html)

HTML uses `<!-- -->` comment blocks.

```html
<!--
✒ Metadata
    - Title: {Tool Name} ({Project-Name} Edition - v{X.Y})
    - File Name: {file_name}.html
    - Relative Path: {relative/path/to/file}.html
    - Artifact Type: {script | library | CLI | config | docs | notebook | test | other}
    - Version: {X.Y.Z}
    - Date: {YYYY-MM-DD}
    - Update: {Day, Month DD, YYYY}
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: {AI-Platform} - {AI-Model (long form)}
    - Signature:  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!

✒ Description:
    Main dashboard page template with responsive grid layout.
    Serves as the primary user interface after authentication.
    Includes widget slots, navigation, and notification areas.

✒ Key Features:
    - Feature 1: Responsive 12-column grid system
    - Feature 2: Collapsible sidebar navigation
    - Feature 3: Widget drag-and-drop zones
    - Feature 4: Real-time notification bell
    - Feature 5: Dark/light theme toggle
    - Feature 6: Breadcrumb navigation
    - Feature 7: Keyboard navigation support
    - Feature 8: Print-optimized styles

✒ Usage Instructions:
    This template is loaded by the router for authenticated users.

    Integration points:
        - Header: Include via {% include 'partials/header.html' %}
        - Sidebar: Dynamic menu loaded from user permissions
        - Main content: Widget grid populated by JavaScript

    Required scripts:
        - dashboard.js (widget management)
        - notifications.js (real-time updates)

✒ Other Important Information:
    - Dependencies: Tailwind CSS 3.x, Alpine.js 3.x
    - Compatible platforms: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
    - Accessibility: WCAG 2.1 AA compliant
    - Performance notes: Critical CSS inlined; deferred script loading
    - Known limitations: Print layout hides interactive elements
---------
-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard | digiSpace</title>
</head>
<body>
    <!-- Content -->
</body>
</html>
```

---

### 4.5 CSS (.css)

CSS uses `/* */` block comments.

```css
/*
 * ============================================================================
 * ✒ Metadata
 *     - Title: {Tool Name} ({Project-Name} Edition - v{X.Y})
 *     - File Name: {file_name}.css
 *     - Relative Path: {relative/path/to/file}.css
 *     - Artifact Type: {script | library | CLI | config | docs | notebook | test | other}
 *     - Version: {X.Y.Z}
 *     - Date: {YYYY-MM-DD}
 *     - Update: {Day, Month DD, YYYY}
 *     - Author: Dennis 'dnoice' Smaltz
 *     - A.I. Acknowledgement: {AI-Platform} - {AI-Model (long form)}
 *     - Signature:  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!
 *
 * ✒ Description:
 *     CSS custom properties (variables) defining the digiSpace design system.
 *     Single source of truth for colors, typography, spacing, and animations.
 *     Import at the root of your stylesheet cascade.
 *
 * ✒ Key Features:
 *     - Feature 1: Complete color palette with semantic naming
 *     - Feature 2: Typography scale (modular scale ratio 1.25)
 *     - Feature 3: Spacing scale (4px base unit)
 *     - Feature 4: Shadow elevation system (5 levels)
 *     - Feature 5: Border radius tokens
 *     - Feature 6: Animation timing functions
 *     - Feature 7: Z-index management layers
 *     - Feature 8: Dark mode variants (prefers-color-scheme)
 *     - Feature 9: Responsive breakpoint references
 *     - Feature 10: Focus ring standardization
 *
 * ✒ Usage Instructions:
 *     Import at the top of your main stylesheet:
 *         @import 'tokens.css';
 *
 *     Use variables in your styles:
 *         .button { background: var(--color-primary-500); }
 *
 *     Override in component scope if needed:
 *         .card { --color-primary-500: #custom; }
 *
 * ✒ Examples:
 *     /* Using color tokens */
 *     .alert-error { color: var(--color-error-600); }
 *
 *     /* Using spacing tokens */
 *     .card { padding: var(--space-4); margin: var(--space-6); }
 *
 *     /* Using typography tokens */
 *     h1 { font-size: var(--text-4xl); line-height: var(--leading-tight); }
 *
 *     /* Using elevation tokens */
 *     .modal { box-shadow: var(--shadow-xl); }
 *
 *     /* Using animation tokens */
 *     .fade-in { transition: opacity var(--duration-300) var(--ease-out); }
 *
 * ✒ Other Important Information:
 *     - Dependencies: None (pure CSS)
 *     - Compatible platforms: All modern browsers with CSS custom properties
 *     - Performance notes: Variables computed once, cached by browser
 *     - Known limitations: IE11 requires PostCSS fallback processing
 * ----------------------------------------------------------------------------
 */

:root {
    /* Color Tokens */
    --color-primary-500: #3b82f6;
    --color-primary-600: #2563eb;

    /* Spacing Tokens */
    --space-1: 0.25rem;
    --space-2: 0.5rem;
    --space-4: 1rem;

    /* Typography Tokens */
    --text-base: 1rem;
    --text-lg: 1.125rem;

    /* Animation Tokens */
    --duration-300: 300ms;
    --ease-out: cubic-bezier(0.33, 1, 0.68, 1);
}
```

---

### 4.6 Bash/Shell (.sh)

Bash uses `#` line comments. The header appears after the shebang.

```bash
#!/usr/bin/env bash
# ==============================================================================
# ✒ Metadata
#     - Title: {Tool Name} ({Project-Name} Edition - v{X.Y})
#     - File Name: {file_name}.sh
#     - Relative Path: {relative/path/to/file}.sh
#     - Artifact Type: {script | library | CLI | config | docs | notebook | test | other}
#     - Version: {X.Y.Z}
#     - Date: {YYYY-MM-DD}
#     - Update: {Day, Month DD, YYYY}
#     - Author: Dennis 'dnoice' Smaltz
#     - A.I. Acknowledgement: {AI-Platform} - {AI-Model (long form)}
#     - Signature:  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!
#
# ✒ Description:
#     Bootstraps development environment for PySnip on fresh Linux installs.
#     Installs system dependencies, Python packages, and configures shell.
#     Idempotent: safe to run multiple times without side effects.
#
# ✒ Key Features:
#     - Feature 1: Detects package manager (apt, dnf, pacman, brew)
#     - Feature 2: Installs Python 3.11+ with pyenv
#     - Feature 3: Sets up virtual environment with poetry
#     - Feature 4: Installs CLI tools (ripgrep, fd, eza, bat, starship)
#     - Feature 5: Configures bashrc/zshrc with aliases
#     - Feature 6: Generates SSH key if not present
#     - Feature 7: Installs VS Code extensions (optional)
#     - Feature 8: Validates installation with health checks
#
# ✒ Usage Instructions:
#     Make executable and run:
#         $ chmod +x setup-env.sh
#         $ ./setup-env.sh
#
#     With options:
#         $ ./setup-env.sh --no-vscode --skip-ssh
#
# ✒ Examples:
#     $ ./setup-env.sh                      # Full installation
#     $ ./setup-env.sh --dry-run            # Preview changes
#     $ ./setup-env.sh --minimal            # Core tools only
#     $ ./setup-env.sh --no-vscode          # Skip VS Code setup
#     $ ./setup-env.sh --python-only        # Only Python toolchain
#     $ ./setup-env.sh --verify             # Run health checks only
#
# ✒ Command-Line Arguments:
#     Installation Modes:
#         --minimal              Install only essential tools
#         --full                 Install everything (default)
#         --python-only          Python toolchain only
#
#     Skip Options:
#         --no-vscode            Skip VS Code extension installation
#         --skip-ssh             Skip SSH key generation
#         --skip-shell           Don't modify shell config
#
#     Utility Options:
#         --dry-run              Show what would be installed
#         --verify               Run health checks without installing
#         --verbose              Detailed output
#         --help                 Show this help message
#
# ✒ Other Important Information:
#     - Dependencies: curl, git (will install if missing)
#     - Compatible platforms: Ubuntu 20.04+, Debian 11+, Fedora 38+,
#                             Arch Linux, macOS 12+, Termux
#     - Estimated time: 10-15 minutes on fast connection
#     - Security considerations: Review script before running with sudo
#     - Known limitations: WSL2 requires Windows Terminal for full experience
# ==============================================================================

set -euo pipefail

# Script implementation
main() {
    echo "Setting up environment..."
}

main "$@"
```

---

### 4.7 YAML (.yaml/.yml)

YAML uses `#` line comments.

```yaml
# ==============================================================================
# ✒ Metadata
#     - Title: {Tool Name} ({Project-Name} Edition - v{X.Y})
#     - File Name: {file_name}.yaml
#     - Relative Path: {relative/path/to/file}.yaml
#     - Artifact Type: {script | library | CLI | config | docs | notebook | test | other}
#     - Version: {X.Y.Z}
#     - Date: {YYYY-MM-DD}
#     - Update: {Day, Month DD, YYYY}
#     - Author: Dennis 'dnoice' Smaltz
#     - A.I. Acknowledgement: {AI-Platform} - {AI-Model (long form)}
#     - Signature:  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!
#
# ✒ Description:
#     Master configuration file for PySnip tool suite.
#     Controls default behaviors, paths, and feature toggles.
#     Override with environment variables: PYSNIP_[KEY]=[value]
#
# ✒ Key Features:
#     - Feature 1: Hierarchical configuration with dot notation access
#     - Feature 2: Environment variable overrides
#     - Feature 3: Profile-based configurations (dev, prod, test)
#     - Feature 4: Sensitive value encryption support
#     - Feature 5: JSON Schema validation
#     - Feature 6: Hot-reload capability
#
# ✒ Usage Instructions:
#     Place in one of these locations (priority order):
#         1. ./pysnip.yaml (project root)
#         2. ~/.config/pysnip/config.yaml
#         3. /etc/pysnip/config.yaml
#
#     Validate before use:
#         $ pysnip config validate
#
# ✒ Other Important Information:
#     - Dependencies: PyYAML 6.0+
#     - Compatible platforms: All (Python 3.9+)
#     - Schema location: schemas/pysnip-config.schema.json
#     - Known limitations: Arrays cannot be overridden via env vars
# ==============================================================================

# Application settings
app:
  name: PySnip
  version: 1.0.0
  debug: false
  log_level: INFO

# Path configurations
paths:
  data_dir: ~/.pysnip/data
  cache_dir: ~/.pysnip/cache
  output_dir: ./output

# Feature toggles
features:
  rich_output: true
  auto_update: false
  telemetry: false
```

---

### 4.8 TOML (.toml)

TOML uses `#` line comments.

```toml
# ==============================================================================
# ✒ Metadata
#     - Title: {Tool Name} ({Project-Name} Edition - v{X.Y})
#     - File Name: {file_name}.toml
#     - Relative Path: {relative/path/to/file}.toml
#     - Artifact Type: {script | library | CLI | config | docs | notebook | test | other}
#     - Version: {X.Y.Z}
#     - Date: {YYYY-MM-DD}
#     - Update: {Day, Month DD, YYYY}
#     - Author: Dennis 'dnoice' Smaltz
#     - A.I. Acknowledgement: {AI-Platform} - {AI-Model (long form)}
#     - Signature:  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!
#
# ✒ Description:
#     Python project configuration following PEP 517/518/621 standards.
#     Defines build system, dependencies, and tool configurations.
#     Used by pip, poetry, and build tools for package management.
#
# ✒ Key Features:
#     - Feature 1: PEP 621 compliant project metadata
#     - Feature 2: Poetry dependency management
#     - Feature 3: Development dependency groups
#     - Feature 4: Tool configurations (black, ruff, mypy, pytest)
#     - Feature 5: Entry point definitions
#     - Feature 6: Optional dependency extras
#
# ✒ Usage Instructions:
#     Install with poetry:
#         $ poetry install
#
#     Build package:
#         $ poetry build
#
#     Run tools:
#         $ poetry run pytest
#
# ✒ Other Important Information:
#     - Dependencies: Poetry 1.5+ or pip 21+
#     - Compatible platforms: All (Python project)
#     - Schema: https://packaging.python.org/en/latest/specifications/
#     - Known limitations: Some tools require their own config files
# ==============================================================================

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[project]
name = "pysnip"
version = "1.0.0"
description = "Comprehensive Python utility toolkit"
readme = "README.md"
requires-python = ">=3.9"

[tool.poetry.dependencies]
python = "^3.9"
rich = "^13.0"
typer = "^0.9"

[tool.black]
line-length = 100
target-version = ["py39"]

[tool.ruff]
line-length = 100
select = ["E", "F", "W", "I", "N"]
```

---

### 4.9 JSON (JSONC)

Standard JSON doesn't support comments. Use JSONC (JSON with Comments) or place
the header in a separate file. For JSONC-supporting tools:

```jsonc
/*
 * ============================================================================
 * ✒ Metadata
 *     - Title: {Tool Name} ({Project-Name} Edition - v{X.Y})
 *     - File Name: {file_name}.json
 *     - Relative Path: {relative/path/to/file}.json
 *     - Artifact Type: {script | library | CLI | config | docs | notebook | test | other}
 *     - Version: {X.Y.Z}
 *     - Date: {YYYY-MM-DD}
 *     - Update: {Day, Month DD, YYYY}
 *     - Author: Dennis 'dnoice' Smaltz
 *     - A.I. Acknowledgement: {AI-Platform} - {AI-Model (long form)}
 *     - Signature:  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!
 *
 * ✒ Description:
 *     VS Code workspace configuration for digiSpace projects.
 *     Standardizes editor behavior, formatting, and extension settings.
 *     Overrides user settings when workspace is open.
 *
 * ✒ Key Features:
 *     - Feature 1: Consistent code formatting (Prettier integration)
 *     - Feature 2: Python/TypeScript language server settings
 *     - Feature 3: File associations and exclusions
 *     - Feature 4: Debug configurations
 *     - Feature 5: Task definitions
 *
 * ✒ Usage Instructions:
 *     Automatically loaded when opening the workspace folder.
 *     Team members should not modify without PR review.
 *
 * ✒ Other Important Information:
 *     - Dependencies: VS Code 1.80+, recommended extensions in extensions.json
 *     - Known limitations: Some settings may conflict with user preferences
 * ----------------------------------------------------------------------------
 */
{
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "python.defaultInterpreterPath": ".venv/bin/python",
    "typescript.preferences.importModuleSpecifier": "relative"
}
```

**Alternative for pure JSON:** Create a companion `settings.json.md` or include
metadata in a `_metadata` key that your application ignores.

---

### 4.10 SQL (.sql)

SQL uses `--` for line comments or `/* */` for blocks.

```sql
-- ==============================================================================
-- ✒ Metadata
--     - Title: {Tool Name} ({Project-Name} Edition - v{X.Y})
--     - File Name: {file_name}.sql
--     - Relative Path: {relative/path/to/file}.sql
--     - Artifact Type: {script | library | CLI | config | docs | notebook | test | other}
--     - Version: {X.Y.Z}
--     - Date: {YYYY-MM-DD}
--     - Update: {Day, Month DD, YYYY}
--     - Author: Dennis 'dnoice' Smaltz
--     - A.I. Acknowledgement: {AI-Platform} - {AI-Model (long form)}
--     - Signature:  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!
--
-- ✒ Description:
--     Creates the core user management tables for authentication.
--     Includes users, roles, permissions, and session tracking.
--     Designed for PostgreSQL 14+ with UUID and JSONB support.
--
-- ✒ Key Features:
--     - Feature 1: UUID primary keys for distributed systems
--     - Feature 2: Soft delete with deleted_at timestamps
--     - Feature 3: Audit columns (created_at, updated_at, created_by)
--     - Feature 4: Role-based access control schema
--     - Feature 5: Session management with device tracking
--     - Feature 6: Indexes optimized for common query patterns
--     - Feature 7: Row-level security policies prepared
--
-- ✒ Usage Instructions:
--     Run via migration tool:
--         $ alembic upgrade head
--
--     Or manually:
--         $ psql -U admin -d appdb -f 001_create_users.sql
--
-- ✒ Examples:
--     -- Apply migration
--     $ psql -d myapp -f 001_create_users.sql
--
--     -- Rollback (use down migration)
--     $ psql -d myapp -f 001_create_users.down.sql
--
--     -- Verify tables created
--     SELECT table_name FROM information_schema.tables
--     WHERE table_schema = 'public';
--
-- ✒ Other Important Information:
--     - Dependencies: PostgreSQL 14+, uuid-ossp extension
--     - Rollback: 001_create_users.down.sql
--     - Performance notes: Indexes on email, username, session tokens
--     - Security considerations: Passwords stored as bcrypt hashes only
--     - Known limitations: Requires superuser for uuid-ossp extension
-- ==============================================================================

-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) NOT NULL UNIQUE,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at TIMESTAMPTZ
);

-- Create indexes
CREATE INDEX idx_users_email ON users(email) WHERE deleted_at IS NULL;
CREATE INDEX idx_users_username ON users(username) WHERE deleted_at IS NULL;
```

---

### 4.11 Markdown (.md)

Markdown uses HTML comment blocks for hidden headers or visible text sections.

```markdown
<!--
✒ Metadata
    - Title: {Tool Name} ({Project-Name} Edition - v{X.Y})
    - File Name: {file_name}.md
    - Relative Path: {relative/path/to/file}.md
    - Artifact Type: {script | library | CLI | config | docs | notebook | test | other}
    - Version: {X.Y.Z}
    - Date: {YYYY-MM-DD}
    - Update: {Day, Month DD, YYYY}
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: {AI-Platform} - {AI-Model (long form)}
    - Signature:  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!

✒ Description:
    Complete REST API reference for digiSpace backend services.
    Documents all endpoints, request/response formats, and error codes.
    Intended audience: frontend developers and API consumers.

✒ Key Features:
    - Feature 1: OpenAPI 3.0 specification included
    - Feature 2: Authentication flow documentation
    - Feature 3: Rate limiting policies
    - Feature 4: Webhook event schemas
    - Feature 5: SDK code examples (Python, JavaScript, cURL)

✒ Usage Instructions:
    Read online at docs.digispace.dev/api or build locally:
        $ npm run docs:build

    Import OpenAPI spec into Postman/Insomnia for testing.

✒ Other Important Information:
    - Dependencies: None (documentation only)
    - Live examples: Available at api.digispace.dev/playground
    - Update frequency: Synced with each API release
---------
-->

# digiSpace API Documentation

## Overview

Welcome to the digiSpace API. This document covers...
```

---

### 4.12 INI/Config (.ini/.cfg)

INI files use `;` or `#` for comments.

```ini
; ==============================================================================
; ✒ Metadata
;     - Title: {Tool Name} ({Project-Name} Edition - v{X.Y})
;     - File Name: {file_name}.ini
;     - Relative Path: {relative/path/to/file}.ini
;     - Artifact Type: {script | library | CLI | config | docs | notebook | test | other}
;     - Version: {X.Y.Z}
;     - Date: {YYYY-MM-DD}
;     - Update: {Day, Month DD, YYYY}
;     - Author: Dennis 'dnoice' Smaltz
;     - A.I. Acknowledgement: {AI-Platform} - {AI-Model (long form)}
;     - Signature:  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!
;
; ✒ Description:
;     Legacy configuration file for applications using configparser.
;     Provides backward compatibility with older Python systems.
;     Prefer YAML or TOML for new projects.
;
; ✒ Key Features:
;     - Feature 1: Section-based organization
;     - Feature 2: Environment variable interpolation
;     - Feature 3: Default value fallbacks
;     - Feature 4: Multi-line value support
;
; ✒ Usage Instructions:
;     Load with Python configparser:
;         config = configparser.ConfigParser()
;         config.read('config.ini')
;         value = config.get('section', 'key')
;
; ✒ Other Important Information:
;     - Dependencies: Python stdlib (configparser)
;     - Compatible platforms: All (Python 3.x)
;     - Known limitations: No nested structures; limited type support
; ==============================================================================

[general]
app_name = PySnip
version = 1.0.0
debug = false

[paths]
data_dir = ~/.pysnip/data
log_file = /var/log/pysnip.log

[database]
host = localhost
port = 5432
name = pysnip_db
```

---

## 5. Conditional Sections Reference

| Section | Include When | Omit When |
|---------|--------------|-----------|
| **Command-Line Arguments** | Artifact is a CLI tool | Library, config, docs, non-executable |
| **Examples** | Code artifact with multiple use cases | Simple configs, single-purpose scripts |
| **Usage Instructions** | Any executable or importable code | Pure documentation |
| **Key Features** | Always include | Never omit (minimum 3 features) |
| **Dependencies** | Any external requirements exist | Pure stdlib or standalone |

---

## 6. Quick Reference Card

### Comment Syntax by Language

| Language | Block Comment | Line Comment |
|----------|--------------|--------------|
| Python | `"""..."""` or `'''...'''` | `#` |
| JavaScript/TypeScript | `/* ... */` | `//` |
| HTML/XML | `<!-- ... -->` | N/A |
| CSS | `/* ... */` | N/A |
| Bash/Shell | N/A (use block of `#`) | `#` |
| YAML | N/A (use block of `#`) | `#` |
| TOML | N/A (use block of `#`) | `#` |
| SQL | `/* ... */` | `--` |
| INI | N/A (use block of `;`) | `;` or `#` |
| Markdown | `<!-- ... -->` | N/A |

### Signature Line (Copy-Paste Ready)

```text
︻デ═—··· 🎯 = Aim Twice, Shoot Once!
```

---

## Final Word

This is not optional. This is not a suggestion. This is not project-specific.
Every artifact leaving your keyboard—past, present, and future—carries this
standard. When you open a file six months from now, you'll know exactly what
it does, who made it, and why it exists.

︻デ═—··· 🎯 = Aim Twice, Shoot Once!

---

> *Document generated: Monday, November 24, 2025*
