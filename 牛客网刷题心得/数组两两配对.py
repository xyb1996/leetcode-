#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
    int num;
    cin >> num;
    int *data = new int[num];
    for (int i = 0; i < num; i++) {
        cin >> data[i];
    }
    sort(data, data + num);//对输入的数排序
    int *Sum = new int[num/2];
    for (int i = 0; i < num/2; i++) {
        Sum[i] = data[i] + data[num - 1 - i];//排序后两头的相加
    }
    sort(Sum, Sum + num / 2);//再排序，取最大和最小值
    int count=Sum[num/2-1]-Sum[0];
    cout << count;
    return 0;
}