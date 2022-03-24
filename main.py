import sort_algorithms
import utils
classes = 1
arquivos = 1
algoritmos = 1
"""100, 200,500,1000,2000,5000,7500,10000,15000,30000,50000, """
file_arrays = [ 2000000]
classes = ['a']


if __name__ == '__main__':
    for i in range(0, len(classes)):
        for j in range(0, len(file_arrays)):

            filename = utils.mount_filename(classes[i], file_arrays[j])
            array = utils.open_file(filename)

            results = sort_algorithms.bubble(array)
            utils.write_file("bubble.txt", results)

            results = sort_algorithms.selection(array)
            utils.write_file("Selection.txt", results)
            
            results = sort_algorithms.insertion(array)
            utils.write_file("Insertion.txt", results)

            results = sort_algorithms.merge_sort(array)
            utils.write_file("MergeSort.txt", results)

            results = sort_algorithms.quick_sort(array)
            utils.write_file("QuickSort.txt", results)
            
            results = sort_algorithms.count_sort(array)
            utils.write_file("CountSort.txt", results)
            
            results = sort_algorithms.bucket_sort(array)
            utils.write_file("Bucket_sort.txt", results)
