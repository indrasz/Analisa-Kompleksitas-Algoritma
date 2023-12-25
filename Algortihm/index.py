import time
import matplotlib.pyplot as plt

def compare_words_algorithm1(input1, input2):
    start_time = time.time()

    for word1 in input1:
        for word2 in input2:
            if word1 == word2:
                end_time = time.time()
                return (end_time - start_time) * 1000

    end_time = time.time()
    return (end_time - start_time) * 1000

def compare_words_recursive(input1, input2, index1=0, index2=0):
    # Base case: if either index reaches the end of its respective input
    if index1 == len(input1) or index2 == len(input2):
        return 0

    start_time = time.time()

    # Check if the current words are the same
    if input1[index1] == input2[index2]:
        # If yes, calculate the time difference and move to the next words
        end_time = time.time()
        time_difference = (end_time - start_time) * 1000
        return time_difference + compare_words_recursive(input1, input2, index1 + 1, index2 + 1)
    else:
        # If not, move to the next word in input2
        end_time = time.time()
        time_difference = (end_time - start_time) * 1000
        return time_difference + compare_words_recursive(input1, input2, index1, index2 + 1)

# Example usage
input1 = ["saya", "suka", "dengan", "anda", "sebagainya"]
input2 = ["aku", "dan", "kamu", "tidak", "cocok", "anda"]

input3 = ["saya", "suka", "dengan", "anda", "sebagainya", "saya", "suka", "dengan", "anda", "sebagainya"]
input4 = ["aku", "dan", "kamu", "tidak", "cocok", "aku", "dan", "kamu", "tidak", "cocok", "anda"]

input5 = ["saya", "suka", "dengan", "anda", "sebagainya", "saya", "suka", "dengan", "anda", "sebagainya", "saya", "suka", "dengan", "anda", "sebagainya"]
input6 = ["aku", "dan", "kamu", "tidak", "cocok", "aku", "anda", "dan", "kamu", "tidak", "cocok", "aku", "dan", "kamu", "tidak", "cocok"]

input7 = ["saya", "suka", "dengan", "anda", "sebagainya", "saya", "suka", "dengan", "anda", "sebagainya", "saya", "suka", "dengan", "anda", "sebagainya", "saya", "suka", "dengan", "anda", "sebagainya"]
input8 = ["aku", "dan", "kamu", "tidak", "cocok", "aku", "dan", "anda", "kamu", "tidak", "cocok", "aku", "dan", "kamu", "tidak", "cocok", "aku", "dan", "kamu", "tidak", "cocok"]

input9 = ["saya", "suka", "dengan", "anda", "sebagainya", "saya", "suka", "dengan", "anda", "sebagainya", "saya", "suka", "dengan", "anda", "sebagainya", "saya", "suka", "dengan", "anda", "sebagainya", "saya", "suka", "dengan", "anda", "sebagainya"]
input10 = ["aku", "dan", "kamu", "tidak", "cocok", "aku", "dan", "anda", "kamu", "tidak", "cocok", "aku", "dan", "kamu", "tidak", "cocok", "aku", "dan", "kamu", "tidak", "cocok", "aku", "dan", "kamu", "tidak", "cocok"]

# Create lists to store execution times for each algorithm
algorithm1_times = []
algorithm2_times = []


# Run the algorithms and store execution times
for i in range(1, 11):
    input_name = "input" + str(i)
    algorithm1_times.append(compare_words_algorithm1(locals()[input_name], input2))
    algorithm2_times.append(compare_words_recursive(locals()[input_name], input2))

# Plot the line chart
plt.plot(range(1, 11), algorithm1_times, label='Algorithm 1')
plt.plot(range(1, 11), algorithm2_times, label='Algorithm 2 (Recursive)')
plt.xlabel('Input Set')
plt.ylabel('Execution Time (milliseconds)')
plt.title('Comparison of Algorithm Execution Times')
plt.legend()
plt.show()