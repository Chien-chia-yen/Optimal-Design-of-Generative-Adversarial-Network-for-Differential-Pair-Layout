# Optimal-Design-of-Generative-Adeversarial-Network-for-Differential-Pair-Layout
By Chia-Yen Chien

## Purpose
In the initial phase of this project, extensive meetings were convened to deliberate upon various design considerations that engineers take into account during the process of conducting differential pair layout design. Additionally, machine learning techniques were employed to perform inductive analysis on existing data related to differential pair layout, with the aim of generating integrated and consistent layout results for differential pairs. These results were aligned with design constraints and common routing logic.

The Loss Function incorporated into the model design criteria, conforming to the requirements for a single differential pair, consists of the following components:

1. Verification of whether the starting point and end point of the generated line segment matrix meet the specified requirements.  
2. Examination of whether the line segment surpasses the boundaries (bumps).  
3. Evaluation of three conditions related to whether the corner of the line adheres to the regulations.  
4. Consideration of the shortest path.  
5. Experimental findings demonstrate that these four design criteria, applicable to this project, effectively fulfill their intended design purposes in achieving the routing constraints within the final layout of the differential pair.  

## Result Test：
### Model training is conducted with nine sets of differential pair layouts as the target.
#### Input Data:
- Package Size: 12.6 x 12.2 mm  
- Starting and ending coordinate positions of each differential pair trace  
- Ball Information: BALL_X, BALL_Y  
- Bump Information: BUMP_X, BUMP_Y  
- Each group of differential pair traces contains two starting point coordinates and two ending point coordinates  
- Die Information (Size, Coordination)
#### Result Graph:
![image](https://github.com/Chien-chia-yen/Optimal-Design-of-Generative-Adversarial-Network-for-Differential-Pair-Layout/blob/main/pic/pic3.png)
