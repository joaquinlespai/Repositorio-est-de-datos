import 'dart:math';
void main(){
  List<int> L = [3,4,7,9,8,5,1,2,5,7];
  print(L);

  List<int> L2 = List.generate(10, (index) => Random().nextInt((5)-5));
  print(L2);

}