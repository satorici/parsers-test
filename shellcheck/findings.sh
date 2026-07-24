#!/bin/sh
# Intentional shellcheck findings: error / warning / info / style

# SC1035 (error) — missing spaces in [ ]
if [$FLAG=1]; then
  # SC2086 (warning/info depending on version) — unquoted expansion
  echo $FLAG
  # SC2116 (style) — useless echo in command substitution
  value=$(echo hello)
fi

# SC2034 (warning) — unused variable
UNUSED=1

# SC2006 (style) — obsolete backtick substitution
old=`date`
