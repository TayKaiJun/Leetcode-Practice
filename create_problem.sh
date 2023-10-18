#!/bin/bash

# Extract the problem name from the command-line argument
problem_name=$1

# Define the paths for the new problem's files
problem_dir="${problem_name}"
solution_file="${problem_dir}/solution.py"
problem_file="${problem_dir}/problem.txt"
input_file="${problem_dir}/input.txt"
expected_file="${problem_dir}/expected.txt"

# Create the problem directory
mkdir "$problem_dir"

# Create the problem.txt file
touch "$problem_file"

# Create the solution.py file with a skeleton code
cat << EOF > "$solution_file"
class Solution(object):
    def problem(self):
        # TODO: Implement your solution here
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.problem("")) # insert input in the quotes
EOF

# Print a success message
echo "New problem directory '$problem_dir' created with the necessary files."
