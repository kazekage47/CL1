#include <iostream>
using namespace std;

int main()
{
	int cost[6][6],g1[8],g2[6][6],g3[6][6],v[5],minarr[8],visited[8];
	int i,j,k,min,calc;
	#pragma omp parallel for
	for(i=1;i<=4;i++)
	{
		visited[i]=0;
	}
	for(i=1;i<=4;i++)
	{
		#pragma omp parallel for
		for(j=1;j<=4;j++)
		{
			if(j==i)
			{
				cost[i][j]=0;
				continue;
			}
			else
			{
				cout<<"Enter cost of path between "<<i<<" and "<<j<<"=";
				cin>>cost[i][j];
			}
		}
	}

	#pragma omp parallel for
	for(i=2;i<=4;i++)
	{
		g1[i]=cost[i][1];
		cout<<"\ng1 : "<<i<<"= "<<g1[i];
	}
	#pragma omp parallel for
	for(i=2;i<=4;i++)
	{
		#pragma omp parallel for
		for(j=2;j<=4;j++)
		{
			if(j==i)
			continue;
			else
			{
			g2[i][j]=cost[i][j]+g1[j];
			}

			cout<<"\ng2 : "<<i<<","<<j<<" = "<<g2[i][j];
		}
	}
	
	for(i=2;i<=4;i++)
	{
		min=999;
		for(j=2;j<=4;j++)
		{
			if(j==i)
				continue;
			else
			{
				#pragma omp parallel for
				for(k=2;k<=4;k++)
				{
					if(k!=i && k!=j)
					{
						g3[i][j]=cost[i][j]+g2[j][k];
					}
				}
			}
			if(g3[i][j]<min)
			{
				min=g3[i][j];
				minarr[i]=g3[i][j];
				v[i]=j;
			}
			cout<<"\ng3 : "<<i<<","<<j<<","<<(--k)<<" = "<<g3[i][j]<<"\n v["<<i<<"] = "<<v[i];
		}
	}

	min=999;

	#pragma omp parallel for
	for(i=2;i<=4;i++)
	{
		calc=cost[1][i]+minarr[i];
		cout<<"\ng3[1 ,"<<i<<"] = "<<calc;
		if(calc<min)
		{
			min=calc;
			g3[1][i]=calc;
			v[1]=i;
		}
	}

	i=1;j=1;
	cout<<"\n";
	while(visited[i]!=1)
	{
		cout<<i<<"-----";

		visited[i]=1;
		i=v[i];
	}
	#pragma omp parallel for
	for(i=1;i<=4;i++)
	{
		if(visited[i]==0)
		cout<<"-----"<<i;
	}

	cout<<"-----1";
	return 0;
}
