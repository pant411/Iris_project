path='*.jpg'
for f in $path; do 
    echo $f
    tesseract -l tha+eng "$f" stdout >> "$f".txt
done