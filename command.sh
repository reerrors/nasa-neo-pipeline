#!/bin/bash
set -e  # para o script se qualquer comando falhar

PROJETO="$HOME/nasa-neo-pipeline"
LOG="$PROJETO/pipeline.log"

# Muda para o diretório do projeto
cd "$PROJETO"

# Executa o Python do ambiente virtual, redirecionando saída e erros para o log
"$PROJETO/.venv/bin/python" "$PROJETO/src/pipeline.py" >> "$LOG" 2>&1






