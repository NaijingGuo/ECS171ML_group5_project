# ECS171ML_group5_project
## Data Visulaization and Pre-Processing
**Summary: all catagorical values to numerical values and min_max normalization for all parameters**

i. Gender
=> For this column, we simply mapped as follows:
Female = 0
Male = 1

ii. Age 
=> For this column, we did min_max normalization so that all values are between 0 & 1.

iii. Height
=> For this column, we did min_max normalization so that all values are between 0 & 1.

iv. Weight
=> For this column, we did min_max normalization so that all values are between 0 & 1.

v. family_history_with_overweight
=> This column has yes/no (binary) values. So we mapped the data as follows:
yes = 1
no = 0

vi. FAVC
=> This column has yes/no (binary) values. So we mapped the data as follows:
yes = 1
no = 0

vii. FCVC
=> For this column, we did min_max normalization so that all values are between 0 & 1.

viii. NCP
=> This column basically has yes/no (binary) values. So we mapped the data as follows:
yes = 1
no = 0

ix. CAEC
=> In this column, we are mapped the data as follows:


&nbsp;&nbsp;&nbsp;&nbsp;no = 0;
sometimes = 1;
frequently = 2;
Always = 3;


&nbsp;&nbsp;&nbsp;&nbsp;and then we did min_max normalization so that all values are between 0 & 1.

x. Smoke
=> This column has yes/no (binary) values. So we mapped the data as follows:
yes = 1
no = 0

xi. CH2O
=> For this column, we did min_max normalization so that all values are between 0 & 1.

xii. SCC
=> This column has yes/no(binary) values. So we mapped the data as follows:
yes = 1
no = 0

xiii. FAF
=> For this column, we did min_max normalization so that all values are between 0 & 1.

xiv. TUE
=> For this column, we did min_max normalization so that all values are between 0 & 1.

xv. CALC
=> In this column, we are mapping the data as follows:

&nbsp;&nbsp;&nbsp;&nbsp;no = 0;
Sometimes = 1;
Frequently = 2;
Always = 3

&nbsp;&nbsp;&nbsp;&nbsp;and then we did min_max normalization so that all values are between 0 & 1.

xvi. MTRANS
=> In this column, we mapped the catagories to numbers as follows:

&nbsp;&nbsp;&nbsp;&nbsp;Automobile = 0
Motorbike = 1
Public_transportaion = 2
Bike = 3
Walking = 4

&nbsp;&nbsp;&nbsp;&nbsp;and then we did min_max normalization so that all values are between 0 & 1.

xvii. NObeyesdad
=> In this column, we mapped the catagories to numbers as follows:

&nbsp;&nbsp;&nbsp;&nbsp;Insufficient_Weight = 0
Normal_Weight = 1;
Overweight_Level_I = 2;
Overweight_Level_II = 3;
Overweight_Level_III = 4;


&nbsp;&nbsp;&nbsp;&nbsp;Obesity_Type_I = 5;
Obesity_Type_II = 6;
Obesity_Type_III = 7;

