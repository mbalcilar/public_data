for file in ./*  
do mv "$file" "$(tr '[:upper:]' '[:lower:]' <<<"$file")" 
done
