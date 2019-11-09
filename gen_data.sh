(for i in `seq 1 10000`; do
    echo -e "$RANDOM";
done )> rand.txt

(for i in `seq 1 10000`; do
    echo -e $i;
done )> sorted.txt
