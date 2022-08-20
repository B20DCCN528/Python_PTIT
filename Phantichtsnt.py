

import java.util.Scanner;

public class Phantichtsnt {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for(int z = 1; z <= t; z++) {
            int n = sc.nextInt();
            System.out.printf("Test %d: ", z);
            for(int i = 2; i * i <= n; i++) {
                int s = 0;
                while (n % i == 0) {
                    s++;
                    n /= i;
                }
                if(s > 0) {
                    System.out.printf("%d(%d) ", i, s);
                }
            }
            if(n > 1) {
                System.out.printf("%d(1)", n);
            }
            System.out.println();
        }
    }
}
