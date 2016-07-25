#include <stdio.h>

int sample_fnc(double n,double result)
{
	double i,j;
	for(i=0;i<n;i++)
  	{
  		for(j=0;j<n;j++)
  		{
  			result++;
  		}
  	}
  	return result;
}

int main(void) 
{
  double n;
  
  double result;
  n=1e5;
  result = 0;

  sample_fnc(n,result);
  return 0;
}