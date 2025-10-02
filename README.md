
# Easy Modular Scripts

This repository contains a collection of modular scripts and tools for AI-assisted development. Below is a list of available commands (aliases) and their functions.

## Setup
Run `update-aliases` or `emsupdate` to set up the aliases in your shell.

## Commands

### AI Tools
- **`ask`** - Send a prompt to an AI model and get a response. Usage: `ask <prompt>`
- **`runit`** - Run a shell script (likely related to the ask-app).
- **`gmfp`** - Get multifile prompt. Copies the contents of specified files to clipboard in a formatted way. Usage: `gmfp <file1> <file2> ...` or `gmfp 1 "file1" "file2" ...`
- **`mkfiles`** - Takes clipboard content and creates a multifile project.
- **`mcoder`** or **`mc`** - Main multicoder tool for AI-assisted code generation and management.

### Multicoder Subcommands (use with `mcoder` or `mc`)
- **`mc get <llm_count> <pattern> [-r] [user_instructions]`** - Generate code using AI for files matching the pattern. `-r` for recursive search.
- **`mc write <response_number>`** - Write the AI-generated code from a specific response to files.
- **`mc write list`** - List all available responses.
- **`mc open`** - Display all response files.
- **`mc rollback [version]`** - Rollback to a specific version (default: latest).
- **`mc clear`** - Clear the multicoder workspace (requires confirmation unless `-y` flag).
- **`mc backup <name>`** - Create a manual backup with the given name.
- **`mc undo`** - Undo the last write operation.
- **`mc ignore <pattern>`** - Add a pattern to the ignore list (e.g., `__pycache__`).
- **`mc rmignore <pattern>`** - Remove a pattern from the ignore list.
- **`mc lsignores`** or **`mc lsignore`** - List all ignored patterns.
- **`mc model`** - Change the AI model for AI_TOOLS_MODEL or ASK_APP_MODEL in the .env file.

### Meta Commands
- **`update-aliases`** or **`emsupdate`** - Update shell aliases and environment variables.

## Environment Variables
- `EasyModularScriptsDir` - Set to the root directory of this project.
- `MODEL` - AI model to use (default: varies by tool).
- `OPENROUTER_API_KEY` - API key for OpenRouter (required for AI functionality).

## Configuration
- Aliases are defined in `aliases_config.py`.
- Multicoder settings are in `.mcoder-workspace/.mcignore` for ignored files.
- Environment variables can be set in `.env` files throughout the project.
