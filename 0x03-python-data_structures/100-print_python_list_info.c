#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists:
 * a cpython implementation
 * @p: pointer to the python object
 * Return: Nothing
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t listSize, i, alloc;
	PyObject *elementType;

	listSize = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", listSize);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < listSize; i++)
	{
		elementType = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, (Py_TYPE(elementType))->tp_name);
	}
}
