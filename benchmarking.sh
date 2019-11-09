#!/bin/bash
echo SORTED DATASET
echo
echo Binary results for small search
python insert_key_value_pairs.py \
--data_structure binary \
--dataset sorted.txt \
--data_points 100
echo Binary results for large search
python insert_key_value_pairs.py \
--data_structure binary \
--dataset sorted.txt \
--data_points 9000

echo
echo Hash results for small search
python insert_key_value_pairs.py \
--data_structure hash \
--dataset sorted.txt \
--data_points 100
echo Hash results for large search
python insert_key_value_pairs.py \
--data_structure hash \
--dataset sorted.txt \
--data_points 9000

echo
echo AVL results for small search
python insert_key_value_pairs.py \
--data_structure avl \
--dataset sorted.txt \
--data_points 100
echo AVL results for large search
python insert_key_value_pairs.py \
--data_structure avl \
--dataset sorted.txt \
--data_points 9000

echo
echo
echo RANDOM DATASET
echo
echo Binary results for small search
python insert_key_value_pairs.py \
--data_structure binary \
--dataset rand.txt \
--data_points 100
echo Binary results for large search
python insert_key_value_pairs.py \
--data_structure binary \
--dataset rand.txt \
--data_points 9000

echo
echo Hash results for small search
python insert_key_value_pairs.py \
--data_structure hash \
--dataset rand.txt \
--data_points 100
echo Hash results for large search
python insert_key_value_pairs.py \
--data_structure hash \
--dataset rand.txt \
--data_points 9000

echo
echo AVL results for small search
python insert_key_value_pairs.py \
--data_structure avl \
--dataset rand.txt \
--data_points 100
echo AVL results for large search
python insert_key_value_pairs.py \
--data_structure avl \
--dataset rand.txt \
--data_points 9000
