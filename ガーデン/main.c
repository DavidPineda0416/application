#include<bits/stdc++.h>
using namespace std;

int main(){
    //食材個数
    intcow_meat_200=3;
    intcow_meat_150=2;
    intchicken=1;
    intsausage=1;
    intbacon_200=3;
    intbacon_150=2;


    //予約人数を入力
    int N;

    cout<<"人数を入力してください：";
    cin> N;

    intplate_6=0;
    intplate_5=0;

    if(N>6){
        plate_6=N/6;          //6人分の皿の数を計算
        if(N%6>0){              //余りがある場合
            plate_6++;
        }
    }else{
        plate_5 = 1;
    }

    cout<<"皿の数は5枚が" <<plate_5<< "枚、6枚が"<<plate_6<< "枚です。"<<endl;

    cout<<"合計の牛肉は" <<cow_meat_200 * 200<<"g（200gが"<<cow_meat_200 <<"個、150gが" <<cow_meat_150<<"個）です。"<<endl;
    cout<<"合計の豚肉は" <<bacon_200 * 200<<"g（200gが"<<bacon_200 <<"個、150gが" <<bacon_150<<"個）です。"<<endl;

}