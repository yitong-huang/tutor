package java0.src;

import java.util.concurrent.TimeUnit;

public class RepeatThread extends Thread {

    @Override
    public void run() {
        for (var i = 0; i < 10; i++) {
            System.out.println("hello from thread, second " + i);
            try {
                TimeUnit.SECONDS.sleep(1);
            } catch (InterruptedException e) {
                // ignore
            }
        }
    }
}


