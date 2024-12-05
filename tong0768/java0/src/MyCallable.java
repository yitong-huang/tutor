package java0.src;

import java.util.Random;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.FutureTask;

public class MyCallable implements Callable<Integer> {
    public static void main(String[] args) {
        var myCallable = new MyCallable();
        var futureTask = new FutureTask<>(myCallable);
        new Thread(futureTask).start();

        try {
            System.out.println("result: " + futureTask.get());
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }
    }

    @Override
    public Integer call() throws Exception {
        return new Random().nextInt();
    }
}