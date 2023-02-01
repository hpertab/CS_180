import argparse as ap

def find_mean(array):
    sum = 0.0
    for cur_num in array:
        sum += float(cur_num)
    mean = float(sum / float(len(array)))
    return mean

def find_variance(array, mean):
    sum = 0.0
    for cur_num in array:
        cur_var = float(cur_num) - mean
        cur_var = cur_var**2
        sum += float(cur_var)
    variance = float(sum / float(len(array)))
    return variance

def main(array):
    # Write the compute the variance and the mean of a given list of numbers

    # Make sure that your terminal output matches the terminal output of the 
    # example given on the instructions.

    mean = find_mean(array)
    variance = find_variance(array, mean)

    print("mean =", round(mean, 16))
    print("variance =", round(variance, 16))

    return None

if __name__ == "__main__":
    argParse = ap.ArgumentParser("Variance and Mean Calculator")
    argParse.add_argument("--array", nargs="+", type=int, help="Input a list of numbers to compute the variance and mean of")
    parsedArgs = argParse.parse_args()
    main(parsedArgs.array)