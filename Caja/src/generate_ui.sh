for file in $( ls ./ui/ )
do
    name=$(echo $file | cut -d "." -f 1)
    pyuic5 -o ./tmp/${name}.py ./ui/$file
done
