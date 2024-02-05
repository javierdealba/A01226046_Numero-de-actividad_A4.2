"""
This is a statistics module for:
    - Mean
    - Median
    - Mode
    - Standard Deviation
    - Varience
"""
import sys
import time

def calculate_mean(data):
    """
    Mean calculation
    """
    result =  sum(data) / len(data)
    return result

def calculate_median(data):
    """
    Median calculation
    """
    data.sort()
    n = len(data)
    median = data[n // 2]

    if n % 2 == 0:
        second_median = data[n // 2 - 1]
        median = (median + second_median) / 2
    return median

def calculate_mode(data):
    """
    Mode calculation
    """
    freqencies = {}
    for value in data:
        freqencies[value] = freqencies.get(value, 0) + 1

    modes = ["#N/A"]
    max_frequency = 1

    for value, frequency in freqencies.items():
        if frequency > max_frequency:
            modes = [value]
            max_frequency = frequency
        elif frequency == max_frequency and frequency > 1:
            modes.append(value)

    if len(modes) == 1:
        modes = modes[0]

    return modes

def calculate_varience(data, p_variance = False):
    """
    Varience calculation
    """
    if p_variance:
        n = len(data)
    else:
        n = len(data) - 1

    mean = calculate_mean(data)
    sum_squared_diff = sum((x - mean) ** 2 for x in data)
    variance = sum_squared_diff / n

    return variance

def calculate_stdev(data):
    """
    Standard deviation calculation
    """
    variance = calculate_varience(data, True)
    stdev = variance ** 0.5

    return stdev

def display_results(all_files_stats):
    """
    Function to display results and save them in a
    """
    print("\t".join(["MEAN"] + [str(stat["mean"]) for stat in all_files_stats]))
    print("\t".join(["MEDIAN"] + [str(stat["median"]) for stat in all_files_stats]))
    print("\t".join(["MODE"] + [str(stat["mode"]) for stat in all_files_stats]))
    print("\t".join(["STANDARD DEVIATION"] + [str(stat["stdev"]) for stat in all_files_stats]))
    print("\t".join(["VARIENCE"] + [str(stat["variance"]) for stat in all_files_stats]))

    with open("StatisticsResults.txt", 'w', encoding='utf-8') as result_file:
        result_file.write("\t".join(["MEAN"] +
            [str(stat["mean"]) for stat in all_files_stats]) + "\n")
        result_file.write("\t".join(["MEDIAN"] +
            [str(stat["median"]) for stat in all_files_stats]) + "\n")
        result_file.write("\t".join(["MODE"] +
            [str(stat["mode"]) for stat in all_files_stats]) + "\n")
        result_file.write("\t".join(["STANDARD DEVIATION"] +
            [str(stat["stdev"]) for stat in all_files_stats]) + "\n")
        result_file.write("\t"
                            .join(
                                ["VARIENCE"] + [str(stat["variance"]) for stat in all_files_stats]
                                ) + "\n"
                            )

def compute_statistics(filename):
    """
    Function to calculate all the statistics
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = [float(line.strip()) for line in file if line.strip().replace('.', '').isdigit()]
            if not data:
                raise ValueError("Error: Empty data set. Unable to convert numbers.")
            file_stats = {}
            file_stats["mean"] = calculate_mean(data)
            file_stats["median"] = calculate_median(data)
            file_stats["mode"] = calculate_mode(data)
            file_stats["stdev"] = calculate_stdev(data)
            file_stats["variance"] = calculate_varience(data)

    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError:
        print("Error: Value error.")

    return file_stats


if __name__ == "__main__":
    time_start = time.time()

    if len(sys.argv) < 2:
        raise ValueError("Error: Invalid number of arguments. Please provide a file path.")
    all_stats = []
    for i in range(1,len(sys.argv)):
        file_path = sys.argv[i]
        stats = compute_statistics(file_path)
        all_stats.append(stats)

    display_results(all_stats)

    elapsed_time = time.time() - time_start
    print(f"Time elapsed: {elapsed_time} s")
