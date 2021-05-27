/*
Max Scott
2020-2021 school year
this is a school project for numerical analysis, homewrok 6 part 5 
***the partitiond trapozoidal method for finding intargals*** 
*/
public class trapezoidal method {
    public static void main(String[] args) {
        double a = 1.0;
        double b = 1.5;
        double n = 4;  
        double h = (b-a)/n;
        double computTrap = f(a);
        for(int i =1; i < n; i++){
            double x = a + i*h;
            computTrap += 2*f(x);
        }
        computTrap += f(b);
        
        computTrap = computTrap*h/2;
        System.out.println("the aria is: " + computTrap);
    }

    public static double f(double x){
        return Math.pow(x,2)*Math.log(x);

    }
    
    
}
