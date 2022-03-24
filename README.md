# Sort Algorithms

![image](https://img.shields.io/github/languages/top/stopasola/minimum-cost-graph)


## Introduction

In this work, was implemented BubbleSort, SelectionSort, InsertionSort, MergeSort, QuickSort, CountSort and BucketSort algorithms. Three approaches was used sekking to mesure the effectiveness of the methods implemented. 
The methods used consisted of the number of comparisons, swaps (value exchanges) and the execution time of all implemented algorithms. 

## Hardware Methods and Configurations

It was used python 3.7 programming language and a computer with the following specs:

- Operating System: Windows 10 Professional, 64-bit
- Processor: Intel Core i5-4200U CPU @ 1.60GHz
- RAM memory: 8.00GB
- SSD: 230 GB

The analyzed datasets consist of 12 files containing partially sorted, ascending sorted, dsescending sorted and random values. The sizes of analyzed datasets consist of `100, 200, 500, 1000, 2000, 5000,7 500, 10000, 15000, 30000, 50000 and 2000000`. All files were executed and further studied.

## Results and discussion

In the quadratic algorithms, the Bubble and Selection present behaviors
similar, due to the number of comparisons being very close and they are the most
expensive, right after they are Quick and Insertion, respectively, Insertion
does not pay comparisons. In relation to the others, the Bucket is the most expensive, so
after that comes Merge and Count, which like Insertion also doesn't pay
comparisons.

Bubble and Selection are the same, they have the same number
of comparisons and are the most expensive, not only among the quadratics, but among
all, followed by Quick and Insertion. In the others, the Bucket is the most expensive,
followed by Merge and Count.

Selection has the highest cost because it performs the
greater number of comparisons, followed by the Bubble that presents a value
very close to the cost of Selection, then the most expensive are Quick and
Insertion. For others, Bucket pays the most comparisons
followed by Merge and Count.

For the partially ordered values, from the quadratic algorithms we have that
Selection has the highest cost, followed by Bubble which has a
close behavior, with relatively close comparison values,
the next most expensive among them in the number of comparisons is Quick
followed by Insertion. In relation to the others, Bucket is the most expensive followed
of Merge and Count.
