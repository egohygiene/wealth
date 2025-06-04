#!/bin/sh
if [ -z "$husky_skip_init" ]; then
  debug() {
    [ -n "$HUSKY_DEBUG" ] && echo "husky:debug $1"
  }
  readonly hook_name="$(basename "$0")"
  debug "starting $hook_name..."
  if [ -f ~/.huskyrc ]; then
    debug "sourcing ~/.huskyrc"
    . ~/.huskyrc
  fi
  export husky_skip_init=1
  sh "$0" "$@"
  exitCode="$?"
  debug "exit code $exitCode"
  exit $exitCode
fi
