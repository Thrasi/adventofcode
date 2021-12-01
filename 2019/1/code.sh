awk '{sum+=int($1/3)} END {print sum}' input.txt
