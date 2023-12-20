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

def compare_words_algorithm2(input1, input2):
    start_time = time.time()

    set1 = set(input1)
    set2 = set(input2)

    common_words = set1.intersection(set2)

    end_time = time.time()
    return (end_time - start_time) * 1000

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
    algorithm2_times.append(compare_words_algorithm2(locals()[input_name], input2))

# Plot the line chart
plt.plot(range(1, 11), algorithm1_times, label='Algorithm 1')
plt.plot(range(1, 11), algorithm2_times, label='Algorithm 2')
plt.xlabel('Input Set')
plt.ylabel('Execution Time (milliseconds)')
plt.title('Comparison of Algorithm Execution Times')
plt.legend()
plt.show()