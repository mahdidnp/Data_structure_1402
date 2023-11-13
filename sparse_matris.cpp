#include <iostream>
using namespace std;



int main_to_sparse(int n,int main[][3])
{
	
	
	int size = 0;
	int m = 0;
	
	
	
	for (int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			if (main[i][j]!=0)
			{
				size++;
			}
		}
	}
	
	int sparse[size][3];
	
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			sparse[m][0] = i;
            sparse[m][1] = j;
            sparse[m][2] = main[i][j];
            m++;
		}
	}
	
	cout << n <<"\t"<< n <<"\t"<< size << endl;

	for (int i = 0; i < size; i++)
    {
        cout << sparse[i][0] << "\t";
        cout << sparse[i][1] << "\t";
        cout << sparse[i][2] << endl;
    }
}

int main() {

	
	int main[3][3] = {{1,1,1,},{2,2,2}, {3,3,3}};
	main_to_sparse(3,main);
	
	
	
	
	
	return 0;
}