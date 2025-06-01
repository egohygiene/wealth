#!/usr/bin/env bash
# Install devtools feature for a development container

# Move to the same directory as this script
set -euo pipefail
FEATURE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "${FEATURE_DIR}"

# -----------------------------------------------------------------------------
# Function: cmd::exists
#
# Description:
#   Checks if a command is available in the current environment's PATH.
#
# Usage:
#   if cmd::exists curl; then ...
#
# Arguments:
#   $1 - Command name to check.
#
# Returns:
#   Exit code 0 if the command exists, non-zero otherwise.
# -----------------------------------------------------------------------------
cmd::exists() {
  command -v "$1" >/dev/null 2>&1
}

# -----------------------------------------------------------------------------
# Function: realpath
#
# Description:
#   Resolves an absolute path. Uses the system realpath if available,
#   otherwise falls back to a POSIX-compliant implementation.
#
# Usage:
#   resolved=$(realpath ./relative/file)
#
# Arguments:
#   $1 - Path to resolve.
#
# Returns:
#   Prints the absolute path or exits non-zero on error.
# -----------------------------------------------------------------------------
realpath() {
    local path="$1"
    if cmd::exists realpath; then
        command realpath "$path"
    else
        # Fallback for POSIX systems (no symlink resolution)
        (cd "$(dirname "$path")" && printf "%s/%s\n" "$(pwd -P)" "$(basename "$path")")
    fi
}

# -----------------------------------------------------------------------------
# Function: trap::on_error
#
# Description:
#   Trap function triggered when a command fails under `set -e`.
#   Prints error details (line number and exit code) to stderr and exits.
#
# Usage:
#   trap 'trap::on_error $LINENO' ERR
#
# Arguments:
#   $1 - Line number where the error occurred.
#
# Returns:
#   Exits with the same exit code that caused the trap.
# -----------------------------------------------------------------------------
trap::on_error() {
  local exit_code=$?
  local line_no=$1
  printf "❌ Error on line %s. Exit code: %d\n" "$line_no" "$exit_code" >&2
  exit "$exit_code"
}

# -----------------------------------------------------------------------------
# Function: trap::on_exit
#
# Description:
#   Trap function triggered on script exit, successful or not.
#   Can be used for cleanup or logging.
#
# Usage:
#   trap trap::on_exit EXIT
#
# Arguments:
#   None
#
# Returns:
#   Nothing (exit proceeds).
# -----------------------------------------------------------------------------
trap::on_exit() {
  local exit_code=$?
  printf "📤 Script exited with code %d\n" "$exit_code" >&2
}

# -----------------------------------------------------------------------------
# Function: trap::on_interrupt
#
# Description:
#   Trap function triggered by Ctrl+C (SIGINT).
#   Prints a message and exits with code 130 (SIGINT convention).
#
# Usage:
#   trap trap::on_interrupt INT
#
# Arguments:
#   None
#
# Returns:
#   Exits with status 130.
# -----------------------------------------------------------------------------
trap::on_interrupt() {
  printf "🚫 Interrupted by user (Ctrl+C)\n" >&2
  exit 130
}

# -----------------------------------------------------------------------------
# Function: trap::setup
#
# Description:
#   Installs standard traps for error handling, interrupt signals, and clean exit.
#
# Usage:
#   trap::setup
#
# Arguments:
#   None
#
# Returns:
#   Registers traps globally for ERR, EXIT, and INT.
# -----------------------------------------------------------------------------
trap::setup() {
  trap 'trap::on_error $LINENO' ERR
  trap trap::on_exit EXIT
  trap trap::on_interrupt INT
}

# -----------------------------------------------------------------------------
# Function: color::reset
#
# Description:
#   Resets all terminal formatting (color, bold, etc.) to default.
#
# Usage:
#   printf "$(color::reset)"
#
# Returns:
#   ANSI escape sequence to reset formatting.
# -----------------------------------------------------------------------------
color::reset() {
  printf '\033[0m'
}

# -----------------------------------------------------------------------------
# Function: color::bold
#
# Description:
#   Returns the ANSI escape code to start bold text formatting.
#
# Usage:
#   printf "$(color::bold)Bold text$(color::reset)"
#
# Returns:
#   ANSI escape sequence for bold formatting.
# -----------------------------------------------------------------------------
color::bold() {
  printf '\033[1m'
}

# -----------------------------------------------------------------------------
# Function: color::dim
#
# Description:
#   Returns the ANSI escape code to start dim (faint) text formatting.
#
# Usage:
#   printf "$(color::dim)Dim text$(color::reset)"
#
# Returns:
#   ANSI escape sequence for dim formatting.
# -----------------------------------------------------------------------------
color::dim() {
  printf '\033[2m'
}

# -----------------------------------------------------------------------------
# Function: color::underline
#
# Description:
#   Returns the ANSI escape code for underlined text.
#
# Usage:
#   printf "$(color::underline)Underlined$(color::reset)"
#
# Returns:
#   ANSI escape sequence for underlining.
# -----------------------------------------------------------------------------
color::underline() {
  printf '\033[4m'
}

# -----------------------------------------------------------------------------
# Function: color::red
#
# Description:
#   Returns the ANSI escape code for red text in bold.
#
# Usage:
#   printf "%sRed text%s\n" "$(color::red)" "$(color::reset)"
#
# Returns:
#   ANSI escape sequence for red text in bold.
# -----------------------------------------------------------------------------
color::red() {
  printf '\033[1;31m'
}

# -----------------------------------------------------------------------------
# Function: color::green
#
# Description:
#   Returns the ANSI escape code for green text in bold.
#
# Usage:
#   printf "%sGreen text%s\n" "$(color::green)" "$(color::reset)"
#
# Returns:
#   ANSI escape sequence for green text in bold.
# -----------------------------------------------------------------------------
color::green() {
  printf '\033[1;32m'
}

# -----------------------------------------------------------------------------
# Function: color::yellow
#
# Description:
#   Returns the ANSI escape code for yellow text in bold.
#
# Usage:
#   printf "%sYellow text%s\n" "$(color::yellow)" "$(color::reset)"
#
# Returns:
#   ANSI escape sequence for yellow text in bold.
# -----------------------------------------------------------------------------
color::yellow() {
  printf '\033[1;33m'
}

# -----------------------------------------------------------------------------
# Function: color::blue
#
# Description:
#   Returns the ANSI escape code for blue text in bold.
#
# Usage:
#   printf "%sBlue text%s\n" "$(color::blue)" "$(color::reset)"
#
# Returns:
#   ANSI escape sequence for blue text in bold.
# -----------------------------------------------------------------------------
color::blue() {
  printf '\033[1;34m'
}

# -----------------------------------------------------------------------------
# Function: color::gray
#
# Description:
#   Returns the ANSI escape code for dim gray (light black) text.
#
# Usage:
#   printf "%sDebug text%s\n" "$(color::gray)" "$(color::reset)"
#
# Returns:
#   ANSI escape sequence for dim gray text.
# -----------------------------------------------------------------------------
color::gray() {
  printf '\033[0;90m'
}

# -----------------------------------------------------------------------------
# Function: terminal::is_term
#
# Description:
#   Determines if stdout is connected to a TTY.
#
# Usage:
#   if terminal::is_term; then echo "Terminal"; fi
#
# Arguments:
#   None
#
# Returns:
#   Exit code 0 if stdout is a terminal, non-zero otherwise.
# -----------------------------------------------------------------------------
terminal::is_term() {
  [[ -t 1 && -n "${TERM:-}" ]] || return 1
}

# -----------------------------------------------------------------------------
# Function: log::__print
#
# Description:
#   Internal logging engine. Handles formatting, color, emoji, and file output.
#
# Usage:
#   log::__print "info" "🔹" "$(color::blue)" "Starting process..."
#
# Arguments:
#   $1 - Log level (e.g., "info", "warn")
#   $2 - Emoji symbol
#   $3 - ANSI color string (e.g., "$(color::red)")
#   $@ - Message to log
#
# Returns:
#   Prints the formatted log line to stderr, and to $LOG_FILE if defined.
# -----------------------------------------------------------------------------
log::__print() {
  local level="$1"
  local emoji="$2"
  local color="$3"
  shift 3
  local message="$*"

  local timestamp
  timestamp="$(date '+%Y-%m-%d %H:%M:%S')"

  local upper_level
  upper_level="$(printf "%s" "$level" | tr '[:lower:]' '[:upper:]')"

  local prefix="${emoji} ${upper_level}:"

  local log_line_console log_line_file

  if terminal::is_term; then
    log_line_console=$(printf "%s %b%-12s%b %s" \
      "$timestamp" \
      "$color" "$prefix" "$(color::reset)" \
      "$message")
  else
    log_line_console=$(printf "%s %-12s %s" "$timestamp" "$prefix" "$message")
  fi

  log_line_file=$(printf "%s %-12s %s" "$timestamp" "$prefix" "$message")

  printf "%s\n" "$log_line_console" >&2
  if [[ -n "${LOG_FILE:-}" && -n "${LOG_FILE// }" ]]; then
    printf "%s\n" "$log_line_file" >> "$LOG_FILE"
  fi
}

# -----------------------------------------------------------------------------
# Function: log::emoji_for
#
# Description:
#   Returns an emoji for a given log level keyword.
#
# Usage:
#   emoji="$(log::emoji_for info)"
#
# Arguments:
#   $1 - Log level (info, warn, error, success, debug)
#
# Returns:
#   Prints the corresponding emoji to stdout.
# -----------------------------------------------------------------------------
log::emoji_for() {
  case "$1" in
    info)    printf "🔹" ;;
    warn)    printf "⚠️ " ;;
    error)   printf "❌" ;;
    success) printf "✅" ;;
    debug)   printf "🐞" ;;
    *)       printf "➖" ;;
  esac
}

# -----------------------------------------------------------------------------
# Function: log::info
# Description: Logs an informational message (blue).
# -----------------------------------------------------------------------------
log::info() {
  log::__print "info" "$(log::emoji_for info)" "$(color::blue)" "$@"
}

# -----------------------------------------------------------------------------
# Function: log::warn
# Description: Logs a warning message (yellow).
# -----------------------------------------------------------------------------
log::warn() {
  log::__print "warn" "$(log::emoji_for warn)" "$(color::yellow)" "$@"
}

# -----------------------------------------------------------------------------
# Function: log::error
# Description: Logs an error message (red).
# -----------------------------------------------------------------------------
log::error() {
  log::__print "error" "$(log::emoji_for error)" "$(color::red)" "$@"
}

# -----------------------------------------------------------------------------
# Function: log::success
# Description: Logs a success message (green).
# -----------------------------------------------------------------------------
log::success() {
  log::__print "success" "$(log::emoji_for success)" "$(color::green)" "$@"
}

# -----------------------------------------------------------------------------
# Function: log::debug
# Description: Logs a debug message (gray).
# -----------------------------------------------------------------------------
log::debug() {
  log::__print "debug" "$(log::emoji_for debug)" "$(color::gray)" "$@"
}

# -----------------------------------------------------------------------------
# Function: log
# Description: Alias for log::info.
# -----------------------------------------------------------------------------
log() {
  log::info "$@"
}

# -----------------------------------------------------------------------------
# Function: date::now
#
# Description:
#   Returns the current UTC timestamp in seconds since the Unix epoch.
#
# Usage:
#   date::now
#
# Arguments:
#   None
#
# Returns:
#   Prints the UTC timestamp to stdout.
#   Exits with non-zero status if `date` fails.
#
# Example:
#   timestamp="$(date::now)"
# -----------------------------------------------------------------------------
date::now() {
  local now

  # Use `-u` for portability instead of `--universal`
  now="$(date -u +%s)" || return $?

  printf "%s\n" "${now}"
}

# -----------------------------------------------------------------------------
# Function: os::operating_system
#
# Description:
#   Detects the host operating system and returns it as a lowercase string.
#
# Usage:
#   os="$(os::operating_system)"
#
# Arguments:
#   None
#
# Returns:
#   Prints the OS name (e.g., "linux", "darwin", "cygwin") to stdout.
#
# Example:
#   if [[ "$(os::operating_system)" == "linux" ]]; then echo "Running on Linux"; fi
# -----------------------------------------------------------------------------
os::operating_system() {
  uname -s 2>/dev/null | tr '[:upper:]' '[:lower:]'
}

# -----------------------------------------------------------------------------
# Function: os::architecture
#
# Description:
#   Detects the CPU architecture and normalizes it into a standard name.
#
# Usage:
#   arch="$(os::architecture)"
#
# Arguments:
#   None
#
# Returns:
#   Prints the normalized architecture (e.g., "amd64", "arm64").
#   Exits with error and logs a message if unsupported.
#
# Example:
#   if [[ "$(os::architecture)" == "arm64" ]]; then echo "ARM machine"; fi
# -----------------------------------------------------------------------------
os::architecture() {
  local raw_arch
  raw_arch="$(uname -m 2>/dev/null || true)"

  case "${raw_arch}" in
    x86_64)   printf "amd64\n" ;;
    aarch64 | arm64) printf "arm64\n" ;;
    *)
      log "❌ Unsupported architecture: ${raw_arch}"
      return 1
      ;;
  esac
}

# -----------------------------------------------------------------------------
# Function: os::detect
#
# Description:
#   Detects the host operating system and architecture, sets global OS and ARCH
#   variables, and logs the result.
#
# Usage:
#   os::detect
#
# Arguments:
#   None
#
# Returns:
#   Sets global variables OS and ARCH.
#   Exits with error if the architecture is unsupported.
#
# Example:
#   os::detect
#   echo "Detected: $OS / $ARCH"
# -----------------------------------------------------------------------------
os::detect() {
  OS="$(os::operating_system)"
  ARCH="$(os::architecture)" || exit 1
  log "🖥️  OS: ${OS}, Arch: ${ARCH}"
}

# -----------------------------------------------------------------------------
# Function: os::is_linux
#
# Description:
#   Checks if the current operating system is Linux.
#
# Usage:
#   if os::is_linux; then echo "Linux host"; fi
#
# Arguments:
#   None
#
# Returns:
#   Exit code 0 if Linux, non-zero otherwise.
# -----------------------------------------------------------------------------
os::is_linux() {
  [[ "$(os::operating_system)" == "linux" ]]
}

# -----------------------------------------------------------------------------
# Function: os::is_macos
#
# Description:
#   Checks if the current operating system is macOS (Darwin).
#
# Usage:
#   if os::is_macos; then echo "macOS host"; fi
#
# Arguments:
#   None
#
# Returns:
#   Exit code 0 if macOS, non-zero otherwise.
# -----------------------------------------------------------------------------
os::is_macos() {
  [[ "$(os::operating_system)" == "darwin" ]]
}

# -----------------------------------------------------------------------------
# Function: os::is_windows
#
# Description:
#   Checks if the current environment is Windows via Cygwin or MinGW.
#
# Usage:
#   if os::is_windows; then echo "Windows environment"; fi
#
# Arguments:
#   None
#
# Returns:
#   Exit code 0 if detected as Windows, non-zero otherwise.
# -----------------------------------------------------------------------------
os::is_windows() {
  local os
  os="$(os::operating_system)"
  [[ "${os}" == "cygwin" || "${os}" == mingw* ]]
}

# -----------------------------------------------------------------------------
# Function: os::is_wsl
#
# Description:
#   Checks if the system is running under Windows Subsystem for Linux (WSL).
#
# Usage:
#   if os::is_wsl; then echo "WSL environment"; fi
#
# Arguments:
#   None
#
# Returns:
#   Exit code 0 if WSL, non-zero otherwise.
# -----------------------------------------------------------------------------
os::is_wsl() {
  os::is_linux && grep -qi 'microsoft' /proc/version 2>/dev/null
}

# -----------------------------------------------------------------------------
# Function: os::is_debian
#
# Description:
#   Checks if the system is Debian-based by looking for /etc/debian_version.
#
# Usage:
#   if os::is_debian; then echo "Debian-like system"; fi
#
# Arguments:
#   None
#
# Returns:
#   Exit code 0 if Debian-like system, non-zero otherwise.
# -----------------------------------------------------------------------------
os::is_debian() {
  [[ -f /etc/debian_version ]]
}

# -----------------------------------------------------------------------------
# Function: os::is_ubuntu
#
# Description:
#   Checks if the system is specifically Ubuntu.
#
# Usage:
#   if os::is_ubuntu; then echo "Ubuntu detected"; fi
#
# Arguments:
#   None
#
# Returns:
#   Exit code 0 if Ubuntu, non-zero otherwise.
# -----------------------------------------------------------------------------
os::is_ubuntu() {
  [[ -f /etc/lsb-release ]] && grep -q "DISTRIB_ID=Ubuntu" /etc/lsb-release
}

# -----------------------------------------------------------------------------
# Function: os::id_like
#
# Description:
#   Extracts the ID_LIKE value from /etc/os-release to determine OS family.
#
# Usage:
#   family="$(os::id_like)"
#
# Arguments:
#   None
#
# Returns:
#   Prints the ID_LIKE string (e.g., "debian", "rhel") or nothing if unavailable.
# -----------------------------------------------------------------------------
os::id_like() {
  [[ -f /etc/os-release ]] && grep '^ID_LIKE=' /etc/os-release | cut -d= -f2 | tr -d '"'
}

# -----------------------------------------------------------------------------
# Function: os::is_supported
#
# Description:
#   Validates that both OS and ARCH are supported.
#
# Usage:
#   if os::is_supported; then proceed; else exit 1; fi
#
# Arguments:
#   None
#
# Returns:
#   Exit code 0 if both OS and ARCH are valid, non-zero otherwise.
# -----------------------------------------------------------------------------
os::is_supported() {
  os::operating_system &>/dev/null && os::architecture &>/dev/null
}

# -----------------------------------------------------------------------------
# Function: os::info
#
# Description:
#   Outputs OS and architecture information as a JSON-like string.
#
# Usage:
#   os::info
#
# Arguments:
#   None
#
# Returns:
#   Prints: {"os":"linux","arch":"amd64"}
# -----------------------------------------------------------------------------
os::info() {
  printf '{"os":"%s","arch":"%s"}\n' "$(os::operating_system)" "$(os::architecture)"
}

# -----------------------------------------------------------------------------
# Function: bash::version
#
# Description:
#   Returns the full Bash version string.
#
# Usage:
#   ver="$(bash::version)"
#
# Returns:
#   e.g., "5.2.15(1)-release"
# -----------------------------------------------------------------------------
bash::version() {
  printf "%s\n" "${BASH_VERSION:-unknown}"
}

# -----------------------------------------------------------------------------
# Function: bash::major_version
#
# Description:
#   Returns the major Bash version number (as a number).
#
# Usage:
#   major="$(bash::major_version)"
#
# Returns:
#   e.g., "5"
# -----------------------------------------------------------------------------
bash::major_version() {
  printf "%s\n" "${BASH_VERSINFO[0]:-0}"
}

# -----------------------------------------------------------------------------
# Function: bash::minor_version
#
# Description:
#   Returns the minor Bash version number (as a number).
#
# Usage:
#   minor="$(bash::minor_version)"
#
# Returns:
#   e.g., "2"
# -----------------------------------------------------------------------------
bash::minor_version() {
  printf "%s\n" "${BASH_VERSINFO[1]:-0}"
}

# -----------------------------------------------------------------------------
# Function: bash::path
#
# Description:
#   Returns the path to the Bash binary being used.
#
# Usage:
#   path="$(bash::path)"
#
# Returns:
#   e.g., "/bin/bash"
# -----------------------------------------------------------------------------
bash::path() {
  printf "%s\n" "${BASH:-$(command -v bash)}"
}

# -----------------------------------------------------------------------------
# Function: bash::is_interactive
#
# Description:
#   Checks if the current shell session is interactive.
#
# Usage:
#   if bash::is_interactive; then echo "Interactive shell"; fi
#
# Returns:
#   Exit code 0 if interactive, non-zero otherwise.
# -----------------------------------------------------------------------------
bash::is_interactive() {
  [[ $- == *i* ]]
}

# -----------------------------------------------------------------------------
# Function: bash::is_strict_mode_enabled
#
# Description:
#   Checks if Bash strict mode is enabled by verifying the status of:
#     - `set -e`   (exit on error)
#     - `set -u`   (treat unset variables as error)
#     - `set -o pipefail` (fail pipeline if any command fails)
#
# Usage:
#   if bash::is_strict_mode_enabled; then
#     echo "Strict mode active"
#   fi
#
# Arguments:
#   None
#
# Returns:
#   Exit code 0 if all strict mode options are active, non-zero otherwise.
# -----------------------------------------------------------------------------
bash::is_strict_mode_enabled() {
  set -o | grep -qE '^errexit +on' &&
  set -o | grep -qE '^nounset +on' &&
  set -o pipefail &>/dev/null && set -o | grep -qE '^pipefail +on'
}

# -----------------------------------------------------------------------------
# Function: bash::options
#
# Description:
#   Displays a filtered list of currently enabled Bash options.
#   This is useful for debugging or introspecting the shell's behavior.
#
# Usage:
#   bash::options
#
# Arguments:
#   None
#
# Returns:
#   Prints all `set -o` options that are currently "on".
# -----------------------------------------------------------------------------
bash::options() {
  set -o | grep -E 'on$'
}

# -----------------------------------------------------------------------------
# Function: bash::print_info
#
# Description:
#   Logs full Bash environment details using the `log` function, including:
#     - Version and version components
#     - Binary path
#     - Interactivity
#     - Strict mode status
#     - Enabled shell options
#
# Usage:
#   bash::print_info
#
# Arguments:
#   None
#
# Returns:
#   Logs a structured set of Bash environment attributes.
# -----------------------------------------------------------------------------
bash::print_info() {
  log "🔍 Bash Info:"
  log "   • Version         : $(bash::version)"
  log "   • Major Version   : $(bash::major_version)"
  log "   • Minor Version   : $(bash::minor_version)"
  log "   • Path            : $(bash::path)"

  if bash::is_interactive; then
    log "   • Interactive     : Yes"
  else
    log "   • Interactive     : No"
  fi

  if bash::is_strict_mode_enabled; then
    log "   • Strict Mode     : Enabled (set -euo pipefail)"
  else
    log "   • Strict Mode     : Disabled"
  fi

  log "   • Enabled Options :"
  while IFS= read -r line; do
    log "     - ${line}"
  done < <(bash::options)
}

init() {
  trap::setup

  os::detect
}

main() {
    init "$@"

    # Ensure we are in the correct directory
    cd "$(realpath "${FEATURE_DIR}")"

    # Set up logging file if needed
    # LOG_FILE="${LOG_FILE:-/dev/null}"

    log "   • Version         : $(bash::version)"
    log "   • Major Version   : $(bash::major_version)"
    log "   • Minor Version   : $(bash::minor_version)"
    log "   • Path            : $(bash::path)"
    log::info "Starting setup..."
    log::warn "This might take a while"
    log::error "Something went wrong"
    log::success "All done!"
    log::debug "Path: $PATH"
}

main "$@"
