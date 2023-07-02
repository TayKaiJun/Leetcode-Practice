#!/bin/bash

# Extract the problem name from the command-line argument
problem_name=$1

# Define the paths for the problem's files
problem_dir="${problem_name}"
solution_file="${problem_dir}/solution.py"
input_file="${problem_dir}/input.txt"
expected_file="${problem_dir}/expected.txt"

# Check if the problem directory exists
if [ ! -d "$problem_dir" ]; then
    echo "Problem directory '$problem_dir' does not exist."
    exit 1
fi

# Check if the solution file exists
if [ ! -f "$solution_file" ]; then
    echo "Solution file '$solution_file' does not exist."
    exit 1
fi

# Check if the input file exists
if [ ! -f "$input_file" ]; then
    echo "Input file '$input_file' does not exist."
    exit 1
fi

# Check if the expected file exists
if [ ! -f "$expected_file" ]; then
    echo "Expected file '$expected_file' does not exist."
    exit 1
fi

# Execute the solution.py file with input from input.txt and store the output in a variable
output=$(python "$solution_file" < "$input_file")

# Read the expected results from expected.txt into an array
mapfile -t expected_results < "$expected_file"

# Calculate the number of test cases
test_case_count=${#expected_results[@]}

# Initialize the number of passed test cases
passed_count=0

# Iterate over each test case and compare the computation result with the expected result
for ((i = 0; i < test_case_count; i++)); do
    expected_result="${expected_results[i]}"
    computation_result=$(echo "$output" | sed -n "$((i+1))p")

    if [ "$computation_result" == "$expected_result" ]; then
        passed_count=$((passed_count + 1))
    fi
done

# Print the result summary
echo "Result Summary:"
echo "Passed (${passed_count}/${test_case_count})"
