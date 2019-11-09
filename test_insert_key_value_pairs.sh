test -e ssshtest || curl https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest -o ssshtest

source ssshtest


run data_file_not_found python insert_key_value_pairs.py \
--data_structure binary \
--dataset no_file.txt \
--data_points 20
assert_exit_code 1
assert_in_stdout 'dataset file could not be found'


run wrong_data_structure python insert_key_value_pairs.py \
--data_structure tree \
--dataset sorted.txt \
--data_points 20
assert_exit_code 1
assert_in_stdout '--data_structure must be binary, hash, or avl'


run sample_input_binary python insert_key_value_pairs.py \
--data_structure binary \
--dataset sorted.txt \
--data_points 20
assert_exit_code 0


run sample_input_hash python insert_key_value_pairs.py \
--data_structure hash \
--dataset sorted.txt \
--data_points 20
assert_exit_code 0


run sample_input_avl python insert_key_value_pairs.py \
--data_structure avl \
--dataset sorted.txt \
--data_points 20
assert_exit_code 0
