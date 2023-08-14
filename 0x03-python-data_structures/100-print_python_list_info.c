#include <Python.h>
#include <listobject.h>
#include <object.h>
/**
 * print_python_list_info -  a C function that prints some basic info
 * about Python lists.
 * @p: object list
 */
void print_python_list_info(PyObject *p)
{
	int allocation, size, i;
	PyObject *object;

	allocation = ((PyListObject *)p)->allocated;
	size = PyList_SIZE(p);
	printf("[*] SIze of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocation);
	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		object = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(object)->tp_name)
	}
}
