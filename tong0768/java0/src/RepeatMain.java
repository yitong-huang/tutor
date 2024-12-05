package java0.src;

import java.util.concurrent.TimeUnit;

public class RepeatMain {

    public static void main(String[] args) {
        new Thread(new RepeatRunnable()).start();
        new RepeatThread().start();
        for (var i = 0; i < 10; i++) {
            System.out.println("hello from main, second " + i);
            try {
                TimeUnit.SECONDS.sleep(1);
            } catch (InterruptedException e) {
                // ignore
            }
        }
    }
}
