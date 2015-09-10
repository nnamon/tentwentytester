#!/usr/bin/python2

import os
import subprocess
import argparse
import difflib


divider = "-" * 30


def get_dir_data(directory):
    data_sets = {}
    dir_files = os.listdir(directory)
    for i in dir_files:
        with open(directory + i, "r") as tmp_file:
            data_sets[i] = tmp_file.read()
    return data_sets


def get_inputs(inp_dir):
    return get_dir_data(inp_dir)


def get_outputs(oup_dir):
    return get_dir_data(oup_dir)


def get_data(inp_dir, oup_dir):
    inp_data = get_inputs(inp_dir)
    oup_data = get_outputs(oup_dir)
    merged = {}
    for i in inp_data.keys():
        common_pre = i.split(".")[0]
        merged[common_pre] = (inp_data[common_pre + ".in"],
                              oup_data[common_pre + ".out"])
    return merged


def run_instance(class_file, data_in, data_out):
    result = False
    cwd = os.getcwd()
    class_path = os.path.realpath(class_file)
    class_name = os.path.basename(class_path).split(".")[0]
    class_dir = os.path.dirname(class_path)
    os.chdir(class_dir)
    proc = subprocess.Popen(["java", class_name], stdout=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    proc.stdin.write(data_in)
    proc.stdin.flush()
    proc_output = proc.stdout.read()
    if data_out == proc_output:
        result = True
    os.chdir(cwd)
    return (result, proc_output)


def enumerate_tests(class_file, input_path, output_path):
    data_set = get_data(input_path, output_path)
    result_set = {}
    for i in data_set.keys():
        data = data_set[i]
        result = run_instance(class_file, data[0], data[1])
        result_set[i] = (result[0], result[1], data[1])
    return result_set


def display_results(results):
    keys_sorted = results.keys()
    keys_sorted.sort()
    print "Results:"
    print divider
    for i in keys_sorted:
        print "%s - %s" % (i, results[i][0])
    print divider + "\n"


def display_diff(results):
    keys_sorted = results.keys()
    keys_sorted.sort()
    for i in keys_sorted:
        if not results[i][0]:
            print divider
            print "%s Analysis" % i
            print divider
            youroutput = results[i][1]
            testcase = results[i][2]
            print "".join(difflib.context_diff(youroutput, testcase,
                                               "Your Output",
                                               "Test Case"))


def main():
    parser = argparse.ArgumentParser("Runs a java class for all test cases")
    parser.add_argument("classf", help="java class to run")
    parser.add_argument("inputd", help="input cases directory")
    parser.add_argument("outputd", help="output cases directory")
    parser.add_argument("--diff", action="store_true",
                        help="run diff on invalid cases")
    args = parser.parse_args()
    results = enumerate_tests(args.classf, args.inputd, args.outputd)
    display_results(results)
    if args.diff:
        display_diff(results)

if __name__ == "__main__":
    main()
