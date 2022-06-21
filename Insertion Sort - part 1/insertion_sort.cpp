#include <iostream>
using namespace std;

// Function to sort an array using insertion sort
void insertionSort(int array[], int size)
{
	int key, j;
	int one = array[size - 1];
	for (int i = 1; i < size; i++)
	{
		key = array[i];
		j = i - 1;
		while (j >= 0 && array[j] > key)
		{
			array[j + 1] = array[j];
			j = j - 1;
			cout << endl;
			for (int k = 0; k < size; k++)
				cout << array[k] << " ";
		}
		array[j + 1] = key;
	}
	cout << endl;
	for (int k = 0; k < size; k++)
		cout << array[k] << " ";
}

int main()
{
	// sample data to check the algorithm
	int sample_array[] = {1, 2, 4, 5, 3};
	int size = sizeof(sample_array) / sizeof(sample_array[0]);

	// array before sort
	cout << "Given array is";

	insertionSort(sample_array, size);

	return 0;
}